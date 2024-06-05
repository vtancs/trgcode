import re
import argparse

class BasicInterpreter:
    def __init__(self):
        self.variables = {}
        self.lines = []
        self.current_line = 0

    def parse_expression(self, expression):
        # Handle basic arithmetic and variables
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            print(f"Error evaluating expression '{expression}': {e}")
            return None

    def interpret_line(self, line):
        line = line.strip()  # Strip leading and trailing spaces
        if line.startswith("LET"):
            match = re.match(r"LET (\w+) = (.+)", line)
            if match:
                var_name, expression = match.groups()
                value = self.parse_expression(expression)
                if value is not None:
                    self.variables[var_name] = value
        elif line.startswith("PRINT"):
            match = re.match(r'PRINT "([^"]*)"', line)
            if match:
                # Print string literals
                print(match.group(1), end='')
            else:
                match = re.match(r"PRINT (.+)", line)
                if match:
                    expression = match.group(1)
                    value = self.parse_expression(expression)
                    if value is not None:
                        print(value, end='')
            # Handle new line if PRINT doesn't end with ;
            if not line.endswith(";"):
                print()
        elif line.startswith("FOR"):
            match = re.match(r"FOR (\w+) = (.+) TO (.+)", line)
            if match:
                var_name, start_expr, end_expr = match.groups()
                start_value = self.parse_expression(start_expr)
                end_value = self.parse_expression(end_expr)
                if start_value is not None and end_value is not None:
                    self.variables[var_name] = start_value
                    loop_start = self.current_line
                    loop_end = self.find_next_line("NEXT " + var_name)
                    if loop_end is not None:
                        while self.variables[var_name] <= end_value:
                            self.execute_block(loop_start + 1, loop_end - 1)
                            self.variables[var_name] += 1
                        self.current_line = loop_end  # Skip the NEXT line
        elif line.startswith("NEXT"):
            # NEXT is handled within FOR loop
            pass
        else:
            print(f"Unknown command: {line}")

    def find_next_line(self, keyword):
        for i in range(self.current_line + 1, len(self.lines)):
            if self.lines[i].strip().startswith(keyword):
                return i
        return None

    def execute_block(self, start, end):
        i = start
        while i <= end:
            self.current_line = i
            self.interpret_line(self.lines[i])
            i += 1

    def run(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.readlines()
            self.current_line = 0
            while self.current_line < len(self.lines):
                self.interpret_line(self.lines[self.current_line])
                self.current_line += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple BASIC interpreter.")
    parser.add_argument("filename", help="The BASIC file to interpret.")
    args = parser.parse_args()

    interpreter = BasicInterpreter()
    interpreter.run(args.filename)

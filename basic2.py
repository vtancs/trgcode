import re
import argparse

class BasicInterpreter:
    def __init__(self):
        self.variables = {}

    def parse_expression(self, expression):
        # Handle basic arithmetic and variables
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            print(f"Error evaluating expression '{expression}': {e}")
            return None

    def interpret_line(self, line):
        line = line.strip()
        if line.startswith("LET"):
            match = re.match(r"LET (\w+) = (.+)", line)
            if match:
                var_name, expression = match.groups()
                value = self.parse_expression(expression)
                if value is not None:
                    self.variables[var_name] = value
        elif line.startswith("PRINT"):
            match = re.match(r"PRINT (.+)", line)
            if match:
                expression = match.group(1)
                value = self.parse_expression(expression)
                if value is not None:
                    print(value)
        else:
            print(f"Unknown command: {line}")

    def run(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.interpret_line(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple BASIC interpreter.")
    parser.add_argument("filename", help="The BASIC file to interpret.")
    args = parser.parse_args()

    interpreter = BasicInterpreter()
    interpreter.run(args.filename)

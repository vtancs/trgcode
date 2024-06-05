def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence

def format_as_text_diagram(fibonacci_sequence):
    max_length = len(str(fibonacci_sequence[-1]))
    diagram = []
    for i, number in enumerate(fibonacci_sequence):
        num_str = str(number).rjust(max_length)
        diagram.append(f"Term {i+1}: {num_str}")
    return "\n".join(diagram)

def main():
    print("Fibonacci Sequence Text Diagram")
    n = int(input("Enter the number of terms: "))
    fibonacci_sequence = generate_fibonacci(n)
    diagram = format_as_text_diagram(fibonacci_sequence)
    print(diagram)

if __name__ == "__main__":
    main()

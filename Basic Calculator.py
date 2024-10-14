def add(*numbers):
    """Returns the sum of all numbers."""
    return sum(numbers)


def subtract(*numbers):
    """Returns the result of subtracting all numbers from the first one."""
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(*numbers):
    """Returns the product of all numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(*numbers):
    """Returns the result of dividing the first number by the others sequentially."""
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result


def get_numbers():
    """Prompt the user to input as many numbers as they wish."""
    try:
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required.")
        return numbers
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_numbers()


def main():
    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        numbers = get_numbers()

        if choice == '1':
            result = add(*numbers)
            print(f"Result: {result}")
        elif choice == '2':
            result = subtract(*numbers)
            print(f"Result: {result}")
        elif choice == '3':
            result = multiply(*numbers)
            print(f"Result: {result}")
        elif choice == '4':
            result = divide(*numbers)
            print(f"Result: {result}")
        else:
            print("Invalid option. Please select a valid operation.")


if __name__ == "__main__":
    main()

# This file contains intentional issues that SonarQube will detect.

def add_numbers(a, b):
    print("Calculating...")  # SonarQube: Remove debug prints
    result = a + b
    return result


def unused_function():
    x = 100  # SonarQube: unused variable
    y = 200  # SonarQube: unused variable
    return x + y


if __name__ == "__main__":
    value = add_numbers(5, 10)
    print("Result:", value)

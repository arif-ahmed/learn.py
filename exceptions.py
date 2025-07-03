def unhandled_exception():
    divide_by_zero = 1 / 0
    print(divide_by_zero)

# Exception Handling Using try...except


def handle_exception():
    numerator = 1
    denominator = 0

    try:
        result = numerator / denominator
        assert result != 0, "Result should not be zero."
        # If the assertion fails, it will raise an AssertionError
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    except:
        print("Error: Denominator cannot be 0.")
    else:
        print("Division successful.")
    finally:
        print("Execution completed, whether an exception occurred or not.")

# define Python user-defined exceptions


class InvalidAgeException(Exception):
    def __init__(self, message):
        self.message = message


def validate_age(age):
    "Raised when the input value is less than 18"
    if age < 0 or age > 120:
        raise InvalidAgeException(
            "Age cannot be negative or greater than 120.")
    else:
        print(f"Valid age: {age}")


def handle_custom_exception():
    try:
        validate_age(-5)
    except InvalidAgeException as e:
        print(f"Custom Exception: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Age validation successful.")
    finally:
        print("Custom exception handling completed.")


class SalaryNotInRangeException(Exception):
    """Exception raised when the salary is not in the specified range.

    Attributes:
        salary -- input salary which caused the exception
        message -- explanation of the error
    """

    def __init__(self, salary, message):
        self.salary = salary
        self.message = message


def validate_salary(salary):
    """Raised when the input salary is not in the range of 3000 to 10000"""
    if salary < 3000 or salary > 10000:
        raise SalaryNotInRangeException(
            salary, "Salary must be between 3000 and 10000.")
    else:
        print(f"Valid salary: {salary}")


def handle_salary_exception():
    salary = int(input("Enter your salary: "))

    try:
        if not 5000 <= salary <= 10000:
            raise SalaryNotInRangeException(
                salary, "Salary must be between 5000 and 10000.")
    except SalaryNotInRangeException as e:
        print(f"Custom Exception: {e.message}")
    else:
        print("Salary validation successful.")


if __name__ == "__main__":
    # unhandled_exception()
    # handle_exception()
    # handle_custom_exception()
    handle_salary_exception()

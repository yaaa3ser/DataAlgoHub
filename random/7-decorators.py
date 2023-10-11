# Simulated user data for authorization check
AUTHORIZED_USERS = ["user1", "user2"]

def validate_input(func):
    def wrapper(name, age):
        if not isinstance(name, str) or not isinstance(age, int) or age < 0:
            raise ValueError("Invalid input. Name should be a string, and age should be a non-negative integer.")
        return func(name, age)
    return wrapper

def authorize_access(func):
    def wrapper(name, age):
        if name not in AUTHORIZED_USERS:
            raise PermissionError("Unauthorized access. You are not allowed to access sensitive information.")
        return func(name, age)
    return wrapper

@validate_input
@authorize_access
def print_sensitive_info(name, age):
    print(f"Name: {name}, Age: {age}, Sensitive Information: Top Secret")

# Try authorized access with valid input
try:
    print_sensitive_info("user1", 30)
except Exception as e:
    print(e)

# Try unauthorized access
try:
    print_sensitive_info("user3", 25)
except Exception as e:
    print(e)

# Try with invalid input
try:
    print_sensitive_info("user1", -5)
except Exception as e:
    print(e)

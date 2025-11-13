# Another file with some intentional problems.

def multiply(a, b):
    return a * b


def redundant_code(a, b):
    if a > b:
        return a - b
    else:
        return a - b  # Sonar: duplicated code branches!

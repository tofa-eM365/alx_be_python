def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Perform division
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result:.1f}"

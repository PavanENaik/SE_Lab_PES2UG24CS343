
import math


def parse_declaration(text):
    try:
        if not isinstance(text, str) or text.count(':') != 1:
            return None

        category, value = text.split(':')
        category = category.strip()
        value = float(value.strip())

        if not category or not math.isfinite(value) or value < 0:
            return None

        return category.lower(), value

    except (ValueError, TypeError, AttributeError):
        return None


def duty_amount(text):
    try:
        if not isinstance(text, str) or text.count('@') != 1:
            return None

        value, rate = text.split('@')
        value = float(value.strip())
        rate = float(rate.strip())

        if not math.isfinite(value) or not math.isfinite(rate):
            return None

        if value < 0 or rate < 0 or rate > 100:
            return None

        return value * rate / 100

    except (ValueError, TypeError, AttributeError):
        return None


def hs_chapter(code):
    try:
        if not isinstance(code, str):
            return None

        parts = code.strip().split('.')

        if len(parts) > 2:
            return None

        if not parts[0].isdigit() or len(parts[0]) < 2:
            return None

        if len(parts) == 2 and not parts[1].isdigit():
            return None

        return int(parts[0][:2])

    except (ValueError, TypeError, AttributeError):
        return None


def main():
    print("==== Running parse_declaration ====")
    user_input = input("Enter category:value (e.g. electronics:25000): ")
    result = parse_declaration(user_input)
    print("Category and Value:", result if result is not None else "Invalid input")

    print("\n==== Running duty_amount ====")
    user_input = input("Enter value@rate (e.g. 25000@20): ")
    result = duty_amount(user_input)
    print("Duty Amount:", result if result is not None else "Invalid input")

    print("\n==== Running hs_chapter ====")
    user_input = input("Enter an HS code (e.g. 8517.12): ")
    result = hs_chapter(user_input)
    print("Chapter:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()

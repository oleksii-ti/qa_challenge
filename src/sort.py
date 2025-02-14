import re
import sys

MAX_INPUT_SIZE = 10**7


# Sorting string by numbers, then lowercase letters, then uppercase letters,
# then others characters
def alphanumeric_sort(s):
    if len(s) > MAX_INPUT_SIZE:
        raise ValueError(
            f"Input is too large ({len(s)} characters). Maximum allowed: {MAX_INPUT_SIZE}"
        )

    # Divide the string into parts of numbers and other characters
    parts = re.findall(r"\d+|.", s)

    def sort_key(item):
        if item.isdigit():
            return (0, item.zfill(20))  # Numbers, sorted numerically
        elif item.islower():
            return (1, item)  # Lowercase letters
        elif item.isupper():
            return (2, item)  # Uppercase letters
        else:
            return (3, item)  # Other characters

    sorted_parts = sorted(parts, key=sort_key)

    return "".join(sorted_parts)


if __name__ == "__main__":
    input_str = sys.argv[1] if len(sys.argv) > 1 else "‘A11a4’"
    output_str = alphanumeric_sort(input_str)
    print(output_str)

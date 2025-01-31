def decimal_to_binary_recursive(n):
    """
    Convert a decimal number to binary using recursion.

    Args:
        n (int): The decimal number to be converted.

    Returns:
        None: Prints the binary representation.
    """
    if n > 1:
        decimal_to_binary_recursive(n // 2)
    print(n % 2, end='')

# Decimal number
dec = 34

decimal_to_binary_recursive(dec)
print()


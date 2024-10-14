def pattern_count(text: str, pattern: str) -> int:
    """Returns the number of occurrences of a given pattern within the text.
    
    Example: pattern_count('TCATCA', 'TCA') returns 2.

    Args:
        text (str): The text in which to search for the pattern.
        pattern (str): The pattern to search for.

    Returns:
        int: The number of occurrences of the pattern in the text.
    """
    # Checking if text or pattern is empty
    if not text or not pattern:
        return 0
    
    # Checking if pattern is longer than text
    if len(pattern) > len(text):
        return 0
    
    # Length difference between text and pattern determines the range limit
    occurrences = sum(1 for i in range(len(text) - len(pattern) + 1) 
               if text[i:i + len(pattern)] == pattern)
    
    return occurrences

def pattern_count_test(pattern_count: "function") -> bool:
    """Tests the pattern_count function.
    
    Example: pattern_count('TCATCA', 'TCA') returns 2.

    Args:
        function: The function to be tested.

    Returns:
        bool: True if all tests pass, False if any fail.

    """
    # text, pattern, expected_output
    test_cases = [
        ('TCATCACTATTA', 'TCA', 2),
        ('GACCATGCUAC', 'AC', 2),
        ('AAAAA', 'AA', 4),
        ('GACCATGCU', 'T', 1),
        ('', 'AA', 0),
        ('AAAAA', '', 0),
        ('AAAAA', 'C', 0)
    ]

    passed = True
    for test_case in test_cases:
        text, pattern, expected_output = test_case
        result = pattern_count(text, pattern)
        if result != expected_output:
            print(f"Test case failed: pattern_count('{text}', '{pattern}') should return {expected_output}, but got {result}.")
            passed = False
        else:
            print(f"Test case passed: pattern_count('{text}', '{pattern}') should return {expected_output} and returns {result}.")

    return (passed)

def main():
    print(pattern_count_test(pattern_count))

if __name__ == '__main__':
    main()
    
    
def frequency_map(text: str, k: int) -> dict:
    """Creates a frequency map of all k-mers in the given text.

    Args:
        text (str): The input string.
        k (int): The length of k-mers to search for.

    Returns:
        frequency (dict): A dictionary where keys are k-mers and values are their counts.
    """
    frequency = {}
    n = len(text)

    # Loop over each k-mer and update its frequency
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        if pattern in frequency:
            frequency[pattern] += 1
        else:
            frequency[pattern] = 1

    return frequency
def longest_palindromic_substring(s):
    # Problem: Find the longest substring of s that is a palindrome.
    """
    Given a string s, return the longest palindromic substring.
    """
    n = len(s)
    # Edge case: if the string length is less than 2, it is already a palindrome.
    if n < 2:
        return s

    # start will track the starting index of the longest palindrome found
    # max_len will track the length of the longest palindrome found
    start = 0
    max_len = 1

    # Helper function to expand around the center indices left and right
    # It returns the length of the palindrome found by expanding outwards.
    def expand_around_center(left, right):
        # Expand while the characters at left and right are equal and within bounds
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1  # move left pointer outward
            right += 1  # move right pointer outward
        # After expansion, length is right - left - 1 because left and right have moved one step too far
        return right - left - 1

    # Iterate through each index i, treating it as the center of a palindrome
    for i in range(n):
        # Check for odd length palindrome (single center)
        len1 = expand_around_center(i, i)
        # Check for even length palindrome (center between two characters)
        len2 = expand_around_center(i, i + 1)
        # Get the maximum length palindrome from the two centers
        max_curr_len = max(len1, len2)
        # If the found palindrome is longer than the current max, update max_len and start index
        if max_curr_len > max_len:
            max_len = max_curr_len
            # Calculate the new start index based on the current center i and max_len
            start = i - (max_len - 1) // 2

    # Return the longest palindromic substring found using the start index and max_len
    return s[start:start + max_len]
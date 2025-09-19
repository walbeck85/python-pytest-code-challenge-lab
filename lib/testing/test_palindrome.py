from lib.palindrome import longest_palindromic_substring

def test_basic_case_babad():
    # longest palindrome could be "bab" or "aba"
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_basic_case_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_characters():
    assert longest_palindromic_substring("ab") in ["a", "b"]
    assert longest_palindromic_substring("aa") == "aa"

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_no_palindromes_beyond_single_chars():
    # In "abc", no palindromes longer than 1 character
    result = longest_palindromic_substring("abc")
    assert result in ["a", "b", "c"]

def test_mixed_alphanumeric_input():
    # "a1b1a" has "1b1" as palindrome or "a1b1a"
    result = longest_palindromic_substring("a1b1a")
    assert result == "a1b1a"

def test_very_long_string_performance():
    long_str = "a" * 1000
    result = longest_palindromic_substring(long_str)
    assert result == long_str
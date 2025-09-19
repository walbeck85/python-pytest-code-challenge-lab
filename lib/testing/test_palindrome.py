from lib.palindrome import longest_palindromic_substring

def test_basic_case_babad():
    # longest palindrome could be "bab" or "aba"
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_basic_case_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"
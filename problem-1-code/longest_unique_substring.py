
def longest_unique_substring_length(s):
    max_length = 0

    for i in range(len(s)):
        new_s = ""
            #abcabcbb
        for ch in s[i:]:
            if ch in new_s:
                break
            new_s += ch

        max_length = max(max_length, len(new_s))

    return max_length

print(longest_unique_substring_length("abcabcbb"))
print(longest_unique_substring_length("bbbbb"))
print(longest_unique_substring_length("a b c"))
print(longest_unique_substring_length("pwkea"))
print(longest_unique_substring_length(""))
print(longest_unique_substring_length("@#$%"))

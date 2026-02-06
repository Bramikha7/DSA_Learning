#  Determine if a smaller list, sub-list, exists as a contiguous sub-sequence within a
#  larger list, main_list. Return a boolean result (True or False).
# ```python
# # Sample Input
# Input:
main_list=[1, 5, 8, 3, 7, 9, 3, 7, 9, 2]
sublist=[8,5,1]
# Output: True
found=False
for i in range(len(main_list)):
    if main_list[i:i + len(sublist)]==sublist:
        found=True
        break
print(found)    

#### Strings
# -2.  Given two strings, S_1 and S_2, determine if S_2 is a rotation of S_1.
#   For example, "waterbottle" is a rotation of "erbottlewat".
#   Assume both strings have the same number of characters. Print True or False.
# ```python
# test case 1
# Input: s1 = "ABCDE", s2 = "CDEAB"
# Output: True
# test case 2
# Input: s1 = "ABCDE", s2 = "ACDEB"
# Output: False
def str_rotate(s_1, s_2):
    if len(s_1) != len(s_2):
        return False
    return s_2 in (s_1 + s_1)

print(str_rotate("ABCDE", "CDEAB"))


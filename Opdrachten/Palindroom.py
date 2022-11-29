
def isPalindrome(s):
    return s == s[::-1]


s = input("Kies een woord: ")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
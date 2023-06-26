def palindrom(s):
    if s == s[::-1]:
        return True
    return False
print(palindrom('asdfghj'))
print(palindrom('abba'))
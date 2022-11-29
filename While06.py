def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        if i=='o' or i=='e' or i=='i' or i=='u' or i=='a' :
            a+=0
        else :
            a+=1

    return a

print(main('aaaaaaaavb'))
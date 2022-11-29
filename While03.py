def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        if i.isalpha() or i.isdigit():
            a+=0
        else :
            a+=1
    return a
print(main("#hashtag@$"))
def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        if i.isupper():
            a+=1
    return a
print(main("CodeschoolUz"))
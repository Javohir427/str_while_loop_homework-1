def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        if i.isdigit():
            a+=1

    return a
print(main("python 2022"))
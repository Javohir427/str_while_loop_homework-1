def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        a+=int(i)
    return a

print(main("987654"))




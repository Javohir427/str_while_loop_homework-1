def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        if int(i)%2==1:
            a+=1
        else:
            a+=0
    return a
print(main("1567534"))
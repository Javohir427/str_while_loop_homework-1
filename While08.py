def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        if int(i)%2==1:
            a+=int(i)
        else:  
            a+=0    
    return a
print(main("1567534"))
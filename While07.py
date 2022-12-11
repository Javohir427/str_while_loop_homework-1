def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    for i in s:
        
        if int(i)%2==0:
            a+=1
        else :  
            a+=0
    return  a

print(main("56786543250"))
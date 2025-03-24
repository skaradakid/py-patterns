def pattern_1(n):
    """Simple triangle
    For n=4:
    *
    **
    ***
    ****
    """
    # TODO: Implement simple right triangle
    string = ""
    for x in range(1,n+1):
        for y in range(x):
            string += "*"
        if x != n:
            string += "\n"
    return string

def pattern_2(n):
    """Number line
    For n=4:
    1 2 3 4
    """
    # TODO: Implement single line of numbers
    string = ""
    for x in range(1,n+1):
        string += str(x)
        string += " "
    return string[:-1]

def pattern_3(n):
    """Square of stars
    For n=4:
    ****
    ****
    ****
    ****
    """
    # TODO: Implement n x n square
    string = ""
    for x in range(1, n+1):
        for y in range(1, n+1):
           string += "*"
        if x != n:
            string += "\n"
    return string

def pattern_4(n):
    """Reverse triangle
    For n=4:
    ****
    ***
    **
    *
    """
    # TODO: Implement reverse right triangle
    string = ""
    for x in range(n, 0, -1):
        for y in range(x):
            string += "*"
        if x != 1:
            string += "\n"
    return string

def pattern_5(n):
    """Number column
    For n=4:
    1
    2
    3
    4
    """
    # TODO: Implement vertical numbers
    string = ""
    for x in range(1, n+1):
        string += str(x)
        if x != n:
            string += "\n"
    return string

def pattern_6(n):
    """Centered triangle
    For n=4:
       *
      ***
     *****
    *******
    """
    # TODO: Implement centered pyramid
    string = ""
    space = n-1
    for x in range(1, n+1):
        string += " "*space
        space -= 1
        for y in range((x*2)-1):
            string += "*"
        if x != n:
            string += "\n"
    return string

def pattern_7(n):
    """Number pyramid
    For n=4:
       1
      1 2
     1 2 3
    1 2 3 4
    """
    # TODO: Implement number pyramid
    pass

def pattern_8(n):
    """Reverse number pyramid
    For n=4:
    1 2 3 4
     1 2 3
      1 2
       1
    """
    # TODO: Implement reverse number pyramid
    pass

def pattern_9(n):
    """Diamond pattern
    For n=4:
       *
      ***
     *****
    *******
     *****
      ***
       *
    """
    # TODO: Implement diamond shape
    pass

def pattern_10(n):
    """Number square
    For n=4:
    1 2 3 4
    1 2 3 4
    1 2 3 4
    1 2 3 4
    """
    # TODO: Implement number square
    pass

def pattern_11(n):
    """Pascal's triangle
    For n=4:
       1
      1 1
     1 2 1
    1 3 3 1
    """
    # TODO: Implement Pascal's triangle
    pass

def pattern_12(n):
    """Hollow triangle
    For n=4:
    *
    **
    * *
    ****
    """
    # TODO: Implement hollow right triangle
    pass

def pattern_13(n):
    """Hollow square
    For n=4:
    ****
    *  *
    *  *
    ****
    """
    # TODO: Implement hollow square
    pass

def pattern_14(n):
    """Number diamond
    For n=4:
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
    """
    # TODO: Implement number diamond
    pass

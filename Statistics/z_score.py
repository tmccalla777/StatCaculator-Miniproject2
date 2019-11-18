def z_score(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    ## a is value
    ## b is mean
    ## c is standard deviation
        d = (a - b) / c
        return d
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")
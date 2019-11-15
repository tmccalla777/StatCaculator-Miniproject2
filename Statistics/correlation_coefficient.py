import math

def correlation_coefficient(a, b, c, d, e, f, g, h, j, k):
    try:
        dataset1 = [a, b, c, d, e]
        dataset2 = [f, g, h, j, k]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        g = int(g)
        h = int(h)
        j = int(j)
        k = int(k)
        sum_a = 0
        sum_b = 0
        sum_ab = 0
        squaresum_a = 0
        squaresum_b = 0
        n = len(dataset2)
        i = 0
        while i < n:
            # sum of elements of array a.
            sum_a = int(sum_a) + int(dataset1[i])
            sum_b = int(sum_b) + int(dataset2[i])
            sum_ab = int(sum_ab) + int(dataset1[i]) * int(dataset2[i])

            # sum of square of array elements.
            squaresum_a = int(squaresum_a) + int(dataset1[i]) * int(dataset1[i])
            squaresum_b = int(squaresum_b) + int(dataset2[i]) * int(dataset2[i])

            i = i + 1

        c = float(n * squaresum_a - sum_a * sum_a)
        d = float(n * squaresum_b - sum_b * sum_b)
        e = float(math.sqrt(c * d))
        f = float(n * sum_ab - sum_a * sum_b)
        corr = round(float(f / e), 4)
        return corr
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")




import math

def pvalue(a, b, c, d):

    p = float(a / b)
    p1 = float(c)
    n = float(b)
    f = float(p - p1)
    y = float(p1 * (1 - p1))
    y2 = float(y)
    y3 = float(y2 / n)
    z = float(f / math.sqrt(y3))
    norm = d
    pval  = 1 - float(norm)

    return pval

# a = 80 #this is
# b = 240 #this is Population
# c = 0.27 # this is Hypothesis Population
# d = 0.981856 #this is from a Z table
#z = f / (math.sqrt(p1*(1-p1)/(n))) but does not run correctly so I broke it down.
#Result ties to what is in the link

#https://www.wallstreetmojo.com/p-value-formula/





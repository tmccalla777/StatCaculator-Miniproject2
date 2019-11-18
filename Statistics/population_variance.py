#Single-Sample Confidence Interval Using the Z Statistic

def population_variance(a,b,c,d,e,f,g,h,j,k):
    try:
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
        population = [a,b,c,d,e,f,g,h,j,k]
        population_mean = (a+b+c+d+e+f+g+h+j+k)/len(population)
        x_minus_mean_sum = 0
        x_minus_mean_squared = 0
        i = 0
        while i < len(population):
                x_minus_mean = int(population[i]) - float(population_mean)
                x_minus_mean_sum = float(x_minus_mean_sum) + float(x_minus_mean)
                x_minus_mean_squared = x_minus_mean**2 + x_minus_mean_squared

                i = i + 1
        pop_variance = float(x_minus_mean_squared/len(population))
        return pop_variance
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print("Error: Only Numeric Values are valid!!")

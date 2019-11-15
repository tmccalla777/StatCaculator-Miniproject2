#Single-Sample Confidence Interval Using the Z Statistic

def confidence_interval(a,b,c,d,e,f,g,h,j,k):
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
        sample = [a,b,c,d,e,f,g,h,j,k]
        # Assume confidence level 95%
        # Z = Z statistic determined by confidence level 95% = 1.96
        confidence_level = 1.96
        x_minus_mean_sum = 0
        x_minus_mean_squared = 0
        sample_mean = float(sum(sample))/float(len(sample))
        i = 0
        while i < len(sample):
            x_minus_mean = float(sample[i]) - float(sample_mean)
            x_minus_mean_sum = float(x_minus_mean_sum) + float(x_minus_mean)
            x_minus_mean_squared = float(x_minus_mean**2) + x_minus_mean_squared
            i = i + 1
        sample_variance = x_minus_mean_squared/len(sample)
        standard_deviation = sample_variance**0.5
        y =  standard_deviation/((len(sample))**0.5)
        conf_inter = round(confidence_level * y, 2)
        return conf_inter
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")


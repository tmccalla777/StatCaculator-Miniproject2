from Statisticss.computation.populationmean import mean
from Statisticss.computation.sample import Sample





def samplemean(list):
    s=50
    r = Sample(list,s)
    c = mean(r)
    return c




#Sample mean = x = ( Σ xi ) / n
# http://www.differencebetween.net/science/difference-between-sample-mean-and-population-mean/

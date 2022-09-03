rahul = [10,0,100,20,50]
ajay = [40,30,40,30,40]

#mean
def mean(arr):
    mean = sum(arr)/len(arr)
    return mean


#median
def median(arr):
    arr.sort()
    if len(arr) % 2 ==0:
        median = arr[(((len(arr)//2)-1)+(len(arr)//2))/2]
    else:
        median = arr[len(arr)//2]
    
    return median

# variance
def variance(arr):
    variance = 0
    for score in arr:
        variance += (score-mean(arr))**2
    return variance

#standard deviation
def std_ev(arr):
    standard_deviation = variance(arr)**0.5
    return standard_deviation



print(f'Mean of scores of Rahul is :{mean(rahul)}')
print(f'Mean of scores of Ajay is :{mean(ajay)}')
print(f'Median of scores of Rahul is :{median(rahul)}')
print(f'Median of scores of Ajay is :{median(ajay)}')
print(f'Variance of scores of Rahul is :{variance(rahul)}')
print(f'Variance of scores of Ajay is :{variance(ajay)}')
print(f'Stansard Deviation of scores of Rahul is :{std_ev(rahul)}')
print(f'Stansard Deviation of scores of Ajay is :{std_ev(ajay)}')

print(' ')


if std_ev(rahul) > std_ev(ajay):
    print('The team will select Ajay')
elif std_ev(rahul) < std_ev(ajay):
    print('The team will select Rahul')
else:
    print('The team can select either of them')

print(' ')

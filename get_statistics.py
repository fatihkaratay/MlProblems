'''
MEAN: sum(input) / len(input)
MEDIAN = sort(input) then get the middle item. if even = avg of middle points
MODE: most frequent element in the list
STANDARD DEVIATION = sqrt((sum(input) - mean)^2/n-1 please note that this is standard deviation. Therefore, it n-1
if it was population, then it should be n only.
VARIANCE= (standatd_deviation)^2
MEAN CONFIDENCE INTERVAL=
    1 compute the standard_error = standard_deviation/sqrt(n)
    2. get the z score from the table. = 1.96
    3. lower and upper values are substract of add from median respectively.
        = [mean-z-score*standard_err. mean+z-score*standard_err]
'''
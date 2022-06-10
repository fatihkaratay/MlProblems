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

input_list = [2, 1, 3, 4, 4, 5, 6, 7]


def get_statistics(input_list):
    sorted_list = sorted(input_list)
    input_len = len(input_list)

    # mean
    mean = sum(sorted_list) / input_len

    # median
    middle_index = (len(sorted_list) - 1) // 2
    median = sorted_list[middle_index]
    if input_len % 2 == 0 :
        middle_number_1 = sorted_list[middle_index]
        middle_number_2 = sorted_list[middle_index + 1]
        median = (middle_number_1 + middle_number_2) / 2


    return {
        "mean": mean,
        "median": median,
        "mode": 0,
        "sample_variance": 0,
        "sample_standard_deviation": 0,
        "mean_confidence_interval": [0, 0]
    }


print(get_statistics(input_list))

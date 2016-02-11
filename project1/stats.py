import math
import csv


def get_frequency_binary(numbers):
    true_count = 0
    false_count = 0
    for x in range(0, len(numbers)):
        if int(numbers[x]) == 0:
            false_count += 1
        else:
            true_count += 1
    return [true_count, false_count]


def get_frequency_nominal(items):
    frequencies = {}
    for x in range(0, len(items)):
        item = items[x]

        try:
            frequencies[item] += 1
        except KeyError:
            frequencies[item] = 1
    return frequencies


def get_mean(numbers):
    total_sum = 0
    for x in range(0, len(numbers)):
        total_sum += float(numbers[x])
    mean = total_sum/len(numbers)
    return mean


def get_min(numbers):
    min_num = 0
    for x in range(0, len(numbers)):
        if x == 0:
            min_num = float(numbers[x])
        if float(numbers[x]) < min_num:
            min_num = float(numbers[x])
    return min_num


def get_max(numbers):
    max_num = 0
    for x in range(0, len(numbers)):
        if x == 0:
            max_num = float(numbers[x])
        if float(numbers[x]) > max_num:
            max_num = float(numbers[x])
    return max_num


def get_median(numbers):

    for x in range(0, len(numbers)):
        numbers[x] = float(numbers[x])
    numbers = sorted(numbers)

    array_length = len(numbers) - 1
    if array_length % 2 != 0:
        median_indices = [int(float(array_length)/2 - 0.5), int(float(array_length)/2 + 0.5)]
        median1 = numbers[median_indices[0]]
        median2 = numbers[median_indices[1]]
        return (float(median1) + float(median2))/2
    else:
        median_index = array_length/2
        return float(numbers[median_index])


def get_standard_deviation(numbers, mean):
    std_dev_sum = 0
    for x in range(0, len(numbers)):
        current_number = float(numbers[x])
        std_dev_sum += (current_number - mean) * (current_number - mean)
    standard_deviation = math.sqrt(std_dev_sum / len(numbers) - 1)
    return standard_deviation


def get_stats():
    with open('downloaded_stats.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        data = [[], [], [], [], []]

        row_count = 0
        for row in reader:
            if row_count != 0:
                for y in range(0, len(row)):
                    item = row[y]
                    if item != 'NA':
                        data[y].append(item)
            else:
                row_count += 1

        actual_elapsed_time_index = 0
        origin_index = 1
        destination_index = 2
        distance_index = 3
        cancelled_index = 4

        actual_elapsed_time_array = data[actual_elapsed_time_index]
        origin_array = data[origin_index]
        destination_array = data[destination_index]
        distance_array = data[distance_index]
        cancelled_array = data[cancelled_index]

        actual_elapsed_time_mean = get_mean(actual_elapsed_time_array)
        actual_elapsed_time_standard_deviation = get_standard_deviation(actual_elapsed_time_array, actual_elapsed_time_mean)
        actual_elapsed_time_min = get_min(actual_elapsed_time_array)
        actual_elapsed_time_max = get_max(actual_elapsed_time_array)
        actual_elapsed_time_median = get_median(actual_elapsed_time_array)
        print "\nThe mean of the actual elapsed time is: ", actual_elapsed_time_mean
        print "The standard deviation of the actual elapsed time is: ", actual_elapsed_time_standard_deviation
        print "The maximum actual elapsed time is: ", actual_elapsed_time_max
        print "The minimum actual elapsed time is: ", actual_elapsed_time_min
        print "The median of actual elapsed time is: ", actual_elapsed_time_median, "\n"

        distance_mean = get_mean(distance_array)
        distance_standard_deviation = get_standard_deviation(distance_array, distance_mean)
        distance_min = get_min(distance_array)
        distance_max = get_max(distance_array)
        distance_median = get_median(distance_array)
        print "The mean of the distance is: ", distance_mean
        print "The standard deviation of the distance is: ", distance_standard_deviation
        print "The maximum distance is: ", distance_max
        print "The minimum distance is: ", distance_min
        print "The median of distance is: ", distance_median, "\n"

        cancelled_frequencies = get_frequency_binary(cancelled_array)
        print "Cancelled Frequency: ", cancelled_frequencies[0], "\t Percentage: ", float(cancelled_frequencies[0])/len(cancelled_array) * 100, "%"
        print "Not Cancelled Frequency: ", cancelled_frequencies[1], "\t Percentage: ", float(cancelled_frequencies[1])/len(cancelled_array) * 100, "% \n"

        origin_frequencies = get_frequency_nominal(origin_array)
        for attr, value in origin_frequencies.iteritems():
            print "Origin: ", attr, " Frequency: ", value, " Percentage: ", float(value)/len(origin_array) * 100, "%"
        print "\n"

        destination_frequencies = get_frequency_nominal(destination_array)
        for attr, value in destination_frequencies.iteritems():
            print "Destination: ", attr, " Frequency: ", value, " Percentage ", float(value)/len(destination_array) * 100, "%"

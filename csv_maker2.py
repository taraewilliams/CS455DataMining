import random
import csv


def get_line_count(file_name):
    with open(file_name) as lines:
        return sum(1 for iterator in lines)


def is_duplicate(array, item_to_add):
    for x in range(0, len(array)):
        if item_to_add == array[x]:
            return True
    return False


def get_included_item_indices(include_list, item_array):
    temporary_list = []
    for x in range(0, len(item_array)):
        current_item = item_array[x]
        for y in range(0, len(include_list)):
            include_list_item = include_list[y]
            if current_item == include_list_item:
                temporary_list.append(x)
    return temporary_list


def filter_data_item(include_list, item_array):
    temporary_list = []
    for x in range(0, len(include_list)):
        temporary_list.append(item_array[include_list[x]])
    return temporary_list


def make_ordinal_from_numerical(filtered_row):
    if filtered_row != "NA":
        if int(filtered_row) <= 500:
            return "Short"
        elif int(filtered_row) <= 1000:
            return "Medium"
        elif int(filtered_row) <= 2000:
            return "Long"
        else:
            return "ExtraLong"
    else:
        return "Short"


def create_csv():
    file_line_length = str(get_line_count("1987.csv"))
    temporary_list = []
    include_list = ['ActualElapsedTime', 'Origin', 'Distance', 'Cancelled']

    with open("1987.csv") as data:
        file_data = data.readlines()

    with open('original_stats.csv', 'wb') as csvfile:
        header = file_data[0].split(",")
        include_list = get_included_item_indices(include_list, header)
        filtered_header = filter_data_item(include_list, header)

        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(filtered_header)

        while len(temporary_list) != 1000:
            generated_random = random.randrange(1, int(file_line_length))
            if not (is_duplicate(temporary_list, generated_random)):
                temporary_list.append(generated_random)

                row = file_data[generated_random].strip("\n").split(",")
                filtered_row = filter_data_item(include_list, row)
                filtered_row[2] = make_ordinal_from_numerical(filtered_row[2])

                writer.writerow(filtered_row)
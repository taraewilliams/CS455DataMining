import csv
import similarity


def get_distance_csv():

    weight = 0.25

    with open('normalized_stats.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        row_count = 0
        item_array = []

        for row in reader:
            if row_count != 0:
                item_array.append(row)
            else:
                row_count += 1

        total_data = []
        for x in range(0, len(item_array)):

            item_one = item_array[x]
            distance_column = []

            for y in range(0, len(item_array)):

                item_two = item_array[y]

                actual_elapsed_time_distance = similarity.get_numerical_distance(item_one[0], item_two[0])
                origin_distance = similarity.get_categorical_distance(item_one[1], item_two[1])
                distance_distance = similarity.get_ordinal_distance(item_one[2], item_two[2])
                cancelled_distance = similarity.get_binary_distance(item_one[3], item_two[3])

                total_distance = (weight * actual_elapsed_time_distance) + (weight * origin_distance) + (weight * distance_distance) + (weight * cancelled_distance)
                distance_column.append(total_distance)

            total_data.append(distance_column)

    with open('distance_stats.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(total_data)):
            writer.writerow(total_data[i])
        print len(total_data[0])
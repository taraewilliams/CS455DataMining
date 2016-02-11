import csv
import similarity


def normalize_actual_elapsed_time(actual_elapsed_time):
    max_value = similarity.get_max(actual_elapsed_time)
    min_value = similarity.get_min(actual_elapsed_time)
    for x in range(0, len(actual_elapsed_time)):
        time = actual_elapsed_time[x]
        actual_elapsed_time[x] = similarity.normalize_numerical(time, min_value, max_value)
    return actual_elapsed_time


def normalize_origin(origin):
    origin = similarity.normalize_categorical(origin)
    return origin


def normalize_distance(distance):
    for y in range(0, len(distance)):
        distance[y] = similarity.normalize_ordinal(distance[y])
    return distance


def normalize_cancelled(cancelled):
    for x in range(0, len(cancelled)):
        if cancelled[x] == "NA":
            cancelled[x] = 0
        else:
            cancelled[x] = int(cancelled[x])
    return cancelled


def normalize_csv():

    header = []
    with open('original_stats.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        data = [[], [], [], []]

        row_count = 0
        for row in reader:

            if row_count != 0:
                for y in range(0, len(row)):
                    item = row[y]
                    data[y].append(item)
            else:
                header = row
                row_count += 1

    actual_elapsed_time = data[0]
    origin = data[1]
    distance = data[2]
    cancelled = data[3]

    actual_elapsed_time = normalize_actual_elapsed_time(actual_elapsed_time)
    origin = normalize_origin(origin)
    distance = normalize_distance(distance)
    cancelled = normalize_cancelled(cancelled)

    with open('normalized_stats.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        i = 0
        while i < 1000:
            row = [actual_elapsed_time[i], origin[i], distance[i], cancelled[i]]
            writer.writerow(row)
            i += 1





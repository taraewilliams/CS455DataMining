def normalize_ordinal(value):
    if value == "Short":
        return 0
    elif value == "Medium":
        return 1
    elif value == "Long":
        return 2
    else:
        return 3


def normalize_numerical(value, min_value, max_value):
    if value == "NA":
        return 0
    else:
        value_range = max_value - min_value
        return float((float(value) - min_value)/value_range)


def normalize_categorical(origin_array):
    categorical_array = []

    for z in range(0, len(origin_array)):
        value = origin_array[z]
        if z == 0:
            categorical_array.append(value)
            origin_array[z] = 0

        is_category = False
        for x in range(0, len(categorical_array)):
            if categorical_array[x] == value:
                origin_array[z] = x
                is_category = True

        if not is_category:
            categorical_array.append(value)
            origin_array[z] = len(categorical_array)

    return origin_array


def get_binary_distance(value_one, value_two):
    if int(value_one) == int(value_two):
        distance = 0
    else:
        distance = 1
    return distance


def get_categorical_distance(value_one, value_two):
    if int(value_one) == int(value_two):
        distance = 0
    else:
        distance = 1
    return distance


def get_numerical_distance(value_one, value_two):
    distance = abs(float(value_one) - float(value_two))
    return distance


def get_ordinal_distance(value_one, value_two):
    distance = abs(int(value_one) - int(value_two))
    if distance == 1:
        return 0.33
    elif distance == 2:
        return 0.67
    elif distance == 0:
        return 0
    else:
        return 1


def get_max(numbers):
    max_num = 0
    for x in range(0, len(numbers)):
        if not numbers[x] == "NA":
            if x == 0:
                max_num = float(numbers[x])
            if float(numbers[x]) > max_num:
                max_num = float(numbers[x])
    return max_num


def get_min(numbers):
    min_num = 0
    for x in range(0, len(numbers)):
        if not numbers[x] == "NA":
            if x == 0:
                min_num = float(numbers[x])
            if float(numbers[x]) < min_num:
                min_num = float(numbers[x])
    return min_num
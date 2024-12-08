
def double(arr):
    duplicatee = set()
    result = []
    for item in lst:
        if item not in duplicatee:
            duplicatee.add(item)
            result.append(item)
    return result


def sort_custom(input_list):
    numbers = [item for item in input_list if isinstance(item, (int, float))]
    strings = [item for item in input_list if isinstance(item, str)]
    numbers.sort()
    strings.sort()
    return numbers + strings

arr = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Анаконда']
first_arr = double(arr)
sorted_arr = sort_custom(first_arr)
print(sorted_arr)
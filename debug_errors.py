def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("Cannot calculate the average of an empty list.")
        return None


def get_list_element(my_list, index):
    try:
        if not isinstance(my_list, list):
            raise TypeError

        return my_list[index]

    except IndexError:
        print("Error: Index is out of range.")
        return None

    except TypeError:
        print("Error: The first argument must be a list.")
        return None

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print("Average of data1:", calculate_average(data1))
print("Average of data2:", calculate_average(data2))
print("Average of data3:", calculate_average(data3))

print()
print(get_list_element(data1, 2))
print(get_list_element(data1, 10))
print(get_list_element("Hello", 1))
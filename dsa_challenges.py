def filter_and_sort_evens(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return sorted(even_numbers)


def count_character_frequency(text):
    frequency = {}

    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


print(filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))

print(count_character_frequency("This my task for Basic Data Structures & Algorithms"))




import time

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

def linear_search(list, item):
    for index, value in enumerate(list):
        if value == item:
            return index

    return None


binary_search([item for item in range(0,1000)], 100)

def bubble_sort(unsorted_list):
    # Iterate over the list for the required number of passes
    for pass_num in range(1, len(unsorted_list)):
        # Iterate over the list from the last element to the first
        for current_index in range(len(unsorted_list) - 1, 0, -1):
            # Compare the current element with its previous element
            if unsorted_list[current_index] < unsorted_list[current_index - 1]:
                # Swap the elements if they are in the wrong order
                current_value, previous_value = unsorted_list[current_index], unsorted_list[current_index - 1]
                unsorted_list[current_index], unsorted_list[current_index - 1] = previous_value, current_value

    return unsorted_list


unsorted_list = [10,2,5,4,3,1,0,8,9]

sorted_list = bubble_sort(unsorted_list)

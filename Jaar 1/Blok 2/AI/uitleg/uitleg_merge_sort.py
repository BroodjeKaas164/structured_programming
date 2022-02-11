def merge_sort(list):
    # 1. Store the length of the list (used len(list))

    # 2. List with length less than is already sorted
    if len(list) == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = len(list) // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


def merge(left, right):
    """
    6. takes in two lists and returns a sorted list made up of the content within the two lists
    :param left: Left Partition of list
    :param right: Right Partition of list
    :return: Sorted merged list
    """
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def built_in_sort(lst):
    """
    Sorts given list, built-in style
    :param lst: Given list
    :return: Return Sorted list
    """
    return sorted(lst)


def run_merge_sort():
    """
    Testfunction for Merge Sorting
    :return: None
    """
    import random
    from time import perf_counter

    unsorted_list = [random.choice(range(1000000)) for _ in range(1000000)]

    start = perf_counter()
    sorted = merge_sort(unsorted_list)
    print(f"\n\t\tMerge Sort | Totale tijd: {(perf_counter() - start) * 1000:.0f}ms")

    start = perf_counter()
    sorted = built_in_sort(unsorted_list)
    print(f"\t\tBuilt-In Sort | Totale tijd: {(perf_counter() - start) * 1000:.0f}ms")


run_merge_sort()

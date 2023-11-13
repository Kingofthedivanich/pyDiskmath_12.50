def quicksort_comparisons(arr):
    if len(arr) <= 1:
        return arr, 0

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    sorted_left, comparisons_left = quicksort_comparisons(left)
    sorted_right, comparisons_right = quicksort_comparisons(right)

    return sorted_left + middle + sorted_right, comparisons_left + comparisons_right + len(arr) - 1


def generate_all_arrays(N):
    arrays = []
    for i in range(1, 2 ** N):
        binary_str = bin(i)[2:].zfill(N)
        arrays.append([int(digit) for digit in binary_str])
    return arrays


def find_max_comparisons(arrays):
    max_comparisons = -1
    max_array = None

    for arr in arrays:
        sorted_arr, comparisons = quicksort_comparisons(arr.copy())
        if comparisons > max_comparisons:
            max_comparisons = comparisons
            max_array = arr

    return max_array, max_comparisons


def main():
    with open('input.txt', 'r') as f:
        N = int(f.readline().strip())

    if N >= 15:
        print("N should be less than 15.")
        return

    arrays = generate_all_arrays(N)
    max_array, max_comparisons = find_max_comparisons(arrays)

    with open('output.txt', 'w') as f:
        f.write("Input N: {}\n".format(N))
        f.write("Max Comparisons: {}\n".format(max_comparisons))
        f.write("Array with Max Comparisons: {}\n".format(max_array))


if __name__ == "__main__":
    main()

# QuickSort function
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Take input from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
arr = list(map(int, user_input.split()))

# Perform QuickSort
sorted_arr = quicksort(arr)

# Output the sorted array
print("Sorted array:", sorted_arr)

# Define a function that takes a sorted list and a target value as parameters
def binary_search(list, target):
  # Initialize start and end variables to the first and last indices of the list
  start = 0
  end = len(list) - 1
  # Repeat until start is greater than end
  while start <= end:
    # Calculate the middle index of the list
    mid = (start + end) // 2
    # If the middle element is greater than the target, move the end to the left of the middle
    if list[mid] > target:
      end = mid - 1
    # If the middle element is less than the target, move the start to the right of the middle
    elif list[mid] < target:
      start = mid + 1
    # If the middle element is equal to the target, return the middle index
    else:
      return mid
  # If the target is not found, return None
  return None
#//////////////////////////////////////
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(lst[mid] > target):
            end = mid - 1
        elif(lst[mid] < target):
            start = mid + 1
        else:
            return mid
    return None

#############################

#######################################################################
                                    # Start
                                    # |
                                    # v
                                    # Input list, key
                                    # |
                                    # v
                                    # low = 0, high = length(list) - 1
                                    # |
                                    # v
                                    # while low <= high
                                    # |       |
                                    # |       v
                                    # |       mid = (low + high) / 2
                                    # |       |
                                    # |       v
                                    # |       if list[mid] == key
                                    # |       |       |
                                    # |       |       v
                                    # |       |       Output "Found at position", mid
                                    # |       |       |
                                    # |       |       v
                                    # |       |       Stop
                                    # |       |
                                    # |       v
                                    # |       else if list[mid] > key
                                    # |       |       |
                                    # |       |       v
                                    # |       |       high = mid - 1
                                    # |       |
                                    # |       v
                                    # |       else
                                    # |               |
                                    # |               v
                                    # |               low = mid + 1
                                    # |
                                    # v
                                    # Output "Not found"
                                    # |
                                    # v
                                    # Stop



#####################################################################

# def binary_search(arr, target):
#     left = 0
#     right = length in arr - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1  # If the target is not found

# # Example usage
# array = [2, 4, 7, 10, 15, 18, 20]
# target_value = 15

# result = binary_search(array, target_value)

# if result != -1:
#     print("Element found at index", result)
# else:
#     print("Element not found in the array")
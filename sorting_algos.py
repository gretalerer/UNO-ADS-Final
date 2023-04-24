
def quicksort_mid(arr): #Algorithm used to alphabetically sort the cards, gotten from class programs
    if len(arr) < 2:
      return arr
    pivot_index = len(arr) // 2
    pivot_value = arr[pivot_index]
    left = [
      element for element in arr[0:pivot_index] + arr[pivot_index + 1:]
      if element < pivot_value
    ]
    right = [
      element for element in arr[0:pivot_index] + arr[pivot_index + 1:]
      if element >= pivot_value
    ]
    return quicksort_mid(left) + [pivot_value] + quicksort_mid(right)

  ## Time Complexity (quicksort algorithm): O(n*log(n)) best case, O(n^2) worse case


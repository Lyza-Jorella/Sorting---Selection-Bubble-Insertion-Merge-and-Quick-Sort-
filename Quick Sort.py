print()
print("**********Programmed by:**********")
print("**********Lyza Jorella R. Del Rosario**********")

def partition(array, low, high):
  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)

print()
nums = [39, 84, 5, 86, 85, 14, 35, 45, 27, 43]
print("Unsorted Numbers")
print(nums)

size = len(nums)

quickSort(nums, 0, size - 1)

print()
print('Sorted Numbers:')
print(nums)
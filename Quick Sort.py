print()
print("**********Programmed by:**********")
print("**********Lyza Jorella R. Del Rosario**********")

def partition(nums, low, high):
  pivot = nums[high]

  i = low - 1

  for j in range(low, high):
    if nums[j] <= pivot:
      i = i + 1
      (nums[i], nums[j]) = (nums[j], nums[i])

  (nums[i + 1],nums[high]) = (nums[high], nums[i + 1])

  return i + 1

def quickSort(nums, low, high):
  if low < high:

    pi = partition(nums, low, high)

    quickSort(nums, low, pi - 1)

    quickSort(nums, pi + 1, high)

print()
nums = [39, 84, 5, 86, 85, 14, 35, 45, 27, 43]
print("Unsorted Numbers")
print(nums)

size = len(nums)

quickSort(nums, 0, size - 1)

print()
print('Sorted Numbers:')
print(nums)
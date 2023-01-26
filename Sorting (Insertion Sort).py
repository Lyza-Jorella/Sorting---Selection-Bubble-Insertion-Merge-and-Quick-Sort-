print()
print("**********Programmed by:**********")
print("**********Lyza Jorella R. Del Rosario**********")
print()

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


nums = [39, 84, 5, 86, 85, 14, 35, 45, 27, 43]
insertionSort(nums)
print(nums)
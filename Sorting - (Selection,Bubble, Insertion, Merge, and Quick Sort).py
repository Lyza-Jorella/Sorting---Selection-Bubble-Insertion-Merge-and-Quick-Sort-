print()
print("**********Programmed by:**********")
print("**********Lyza Jorella R. Del Rosario**********")
print()

def sort(nums):

    for i in range (39):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [39, 84, 5, 86, 85, 14, 35, 45, 27, 43]
sort(nums)

print(nums)



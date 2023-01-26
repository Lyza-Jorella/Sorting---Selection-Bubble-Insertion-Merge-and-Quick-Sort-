print()
print("**********Programmed by:**********")
print("**********Lyza Jorella R. Del Rosario**********")
print()


def sort(nums):
    for i in range (len(nums) -1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [39, 84, 5, 86, 85, 14, 35, 45, 27, 43]
sort(nums)

print(nums)

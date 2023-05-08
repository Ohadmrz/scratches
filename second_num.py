

nums = [54, -1, 45, 987, 5, 2, 65, 7, 12]
max_num = max(nums[0:2])
second_max = min(nums[0:2])
# max_num = nums[0]
# second_max = nums[1]
for num in nums:
    if num < second_max:
        continue
    if second_max < num < max_num:
        second_max = num
    if num > max_num:
        second_max = max_num
        max_num = num
print(second_max)
print(max_num)


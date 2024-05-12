
def threeSum(nums):
	nums1 = nums[:]
	count = 0
	target = 0
	ans = [ ]
	while len(nums1) > 2:
		print(nums1)
		for i in range(len(nums1)):
			j = i + 1
			while j < len(nums1):
				sum1 = nums1[i] + nums1[j]
				for k in range(j, len(nums1)):
					if sum1 + nums[k] == target:
						print(nums1[k])
						remainder = k
						ans += [[nums1[i], nums[j], nums[k]]]
						nums1.remove(nums1[i])
						nums1.remove(nums1[j])
						nums1.remove(nums1[k])
					
						print(nums1)
						break
		j += 1
	print(ans)
	
list1 = [-1,0,1,2,-1,-4]

print(threeSum(list1))


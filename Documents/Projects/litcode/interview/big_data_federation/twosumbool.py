def twoSum(nums, target):
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return True

        return False

if __name__ == '__main__':
	nums1 = [2, 7, 11, 15]
	target1 = 9
	print(twoSum(nums1, target1))

	nums2 = [3, 2, 4]
	target2 = 6
	print(twoSum(nums2, target2))

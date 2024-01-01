def sortedSquaredArray(arr):
	result = [0 for _ in arr]
	left = 0
	right = len(arr) - 1
	current = len(arr) - 1
	while left <= right:
		if abs(arr[left]) > abs(arr[right]):
			result[current] = arr[left] ** 2
			left += 1
		else:
			result[current] = arr[right] ** 2
			right -= 1
		current -= 1
	return result
def find_once_appearing(nums: list) -> int:
  result = 0
  for num in nums:
    result ^= num
  return result

print(find_once_appearing([2, 2, 1]))


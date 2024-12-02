rows = open('./actual_data.txt').read().strip().splitlines()

def stringOfNumsToArray(stringOfNums: str):
  stringifiedNumbers = stringOfNums.split()
  return list(map(int, stringifiedNumbers))

def filterUnsortedArray(nums: list[int]):
  numsCopy = nums.copy()
  if nums[0] < nums[1]:
    numsCopy.sort()
    return numsCopy == nums
  else:
    numsCopy.sort(reverse=True)
    return numsCopy == nums

def filterByValidJumps(nums: list[int]):
  i = 0
  validDistance = True
  while i < len(nums) - 1 and validDistance:
    distance = abs(nums[i] - nums[i + 1])
    if distance > 3 or distance == 0:
      validDistance = False
    i += 1
  return validDistance

numberMatrix = list(map(stringOfNumsToArray, rows))
matrixWithOnlySortedRows = list(filter(filterUnsortedArray, numberMatrix))
matrixWithOnlyValidJumps = list(filter(filterByValidJumps, matrixWithOnlySortedRows))
print(len(matrixWithOnlyValidJumps))

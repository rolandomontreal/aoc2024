rows = open('./testdata.txt').read().strip().splitlines()

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

numberMatrix = list(map(stringOfNumsToArray, rows))
matrixWithOnlySortedRows = list(filter(filterUnsortedArray, numberMatrix))

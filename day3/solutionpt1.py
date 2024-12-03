import re

data = open('./actualdata.txt').read()

regex = "mul\\(\\d{1,3},\\d{1,3}\\)"
validInstructions = re.findall(regex, data)

def parseAndRunCalculation(mulString: str):
  # All strings are on format 'mul(n1,n2)'
  stringifiedNums = mulString[4:-1].split(',')
  n1, n2 = int(stringifiedNums[0]), int(stringifiedNums[1])
  return n1 * n2

results = list(map(parseAndRunCalculation, validInstructions))
print(sum(results))
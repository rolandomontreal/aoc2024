import re

data = open('./actualdata.txt').read()

mulRegex = "mul\\(\\d{1,3},\\d{1,3}\\)"
regex = "(" + mulRegex + "|do\\(\\)|don't\\(\\))"
matches = re.findall(regex, data)

inExecuteMode = True
def parseAndRunCalculation(input: str):
  # Strings are either "do()", "don't()" or "mul(n,m)"
  global inExecuteMode
  if re.match(mulRegex, input):
    stringifiedNums = input[4:-1].split(',')
    n1, n2 = int(stringifiedNums[0]), int(stringifiedNums[1])
    if inExecuteMode:
      return n1 * n2
  elif input == 'do()':
    inExecuteMode = True
  else:
    inExecuteMode = False
  # If it is no mul(n,m), or not in exectute mode, simply return 0
  return 0

results = list(map(parseAndRunCalculation, matches))
print(sum(results))
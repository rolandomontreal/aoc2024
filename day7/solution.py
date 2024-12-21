equationsInStringFormat = open('./actualdata.txt').read().splitlines()

def parseLines(eqsInStrFormat: list[str]):
  output = []
  for eqStr in eqsInStrFormat:
    [resultString, termsString] = eqStr.split(': ')
    result = int(resultString)
    terms = list(map(int, termsString.split()))
    equation = {
      "result": result,
      "terms": terms,
    }
    output.append(equation)
  return output

cachedResult = {}
def getAllCombinations(characters: list[str], l: int):
  if l in cachedResult:
    print(f'😎 CACHE HIT, returning for l: {l} 😎')
    return cachedResult[l]
  if l == 1:
    return characters
  else:
    smallerCombinations = getAllCombinations(characters, l - 1)
    combinations = []
    for c in characters:
      for combination in smallerCombinations:
        newCombination = c + combination
        combinations.append(newCombination)
    if l not in cachedResult:
      cachedResult[l] = combinations
    return combinations

def getPossibleExpressionsAndEvaluate(terms: list[int]):
  operators = ['+', '*']
  nrOfPossibleExpressions = len(terms) - 1
  allExpressionCombinations = getAllCombinations(operators, nrOfPossibleExpressions)
  expressions = []
  for expressionCombination in allExpressionCombinations:
    expression = ''
    value = 0
    for i in range(len(terms)):
      if i == 0:
        expression = str(terms[i])
        value = terms[i]
      else:
        expression += expressionCombination[i - 1] + str(terms[i])
        if expressionCombination[i-1] == '+':
          value += terms[i]
        else:
          value *= terms[i]
    expressions.append({
      "expression": expression,
      "value": value,
    })
  return expressions

def evaluateExpression(expression: str):
  print(expression)

# ['10+19', '10*19']

allEquations = parseLines(equationsInStringFormat)
# print(allEquations)
validEquations = []
sumOfValus = 0
for eq in allEquations:
  print(eq)
  allPossibleCombinationsAndValues = getPossibleExpressionsAndEvaluate(eq["terms"])
  # print(allPossibleCombinationsAndValues)
  values = list(map(lambda obj: obj["value"], allPossibleCombinationsAndValues))
  # print(values)
  if eq["result"] in values:
    print('Valid equation :D')
    validEquations.append(eq)
    sumOfValus += eq["result"]
    print(f'sumOfValus: {sumOfValus}')
  print()

print(f'\n\nFinal score: {sumOfValus}')

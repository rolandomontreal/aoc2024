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
  operators = ['+', '*', '|']
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
        if expressionCombination[i-1] == '+':
          expression += expressionCombination[i - 1] + str(terms[i])
          value += terms[i]
        elif expressionCombination[i-1] == '*':
          expression += expressionCombination[i - 1] + str(terms[i])
          value *= terms[i]
        else:
          strValue = str(value)
          strNextTerm = str(terms[i])
          value = int(strValue + strNextTerm)
          expression += expressionCombination[i - 1] + str(terms[i])
    expressions.append({
      "expression": expression,
      "value": value,
    })
  return expressions

allEquations = parseLines(equationsInStringFormat)
validEquations = []
sumOfValus = 0
for eq in allEquations:
  allPossibleCombinationsAndValues = getPossibleExpressionsAndEvaluate(eq["terms"])
  values = list(map(lambda obj: obj["value"], allPossibleCombinationsAndValues))
  if eq["result"] in values:
    validEquations.append(eq)
    sumOfValus += eq["result"]

print(f'\n\nFinal score: {sumOfValus}')

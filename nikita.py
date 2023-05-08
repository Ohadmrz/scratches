# Q.1
def main():
    numbers = [1, 2, 3, 4, 5.1]
    result = getSumOfNumbersSequence(numbers)
    print(result)
    return 1
def getSumOfNumbersSequence(numbers: list) -> float:
    return float(sum(numbers))
if __name__ == '__main__':
    main()

# Q.2
def main():
    numbers = (2, 4, 6)
    result = getMultiplyOfNumbersSequence(numbers)
    print(result)
    return 1
def getMultiplyOfNumbersSequence(numbers: tuple) -> float:
    if not numbers:  # empty tuple
        return 0.0
    result = 1.0
    for i in numbers:
        result *= i
    return float(result)
if __name__ == '__main__':
    main()

# Q.3
def main():
    result = getMaxValue(2.0, 4.0, 6.0)
    print(result)
    return 1
def getMaxValue(value_first: float, value_second: float, value_third: float) -> float:
    values = [value_first, value_second, value_third]
    return float(max(values))
if __name__ == '__main__':
    main()

# Q.4
def main():
    result = getFactorialOfNumber(9)
    print(result)
    return 1
def getFactorialOfNumber(number: int) -> int:
    if number < 0:
        return 0
    if number in [0, 1]:
        return 1
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial
if __name__ == '__main__':
    main()

# Q.5
def main():
    values = (0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7)
    result = getSequenceUniqueValues(values)
    print(result)
    return 1
def getSequenceUniqueValues(values: tuple) -> tuple:
    return tuple(i for i in values if values.count(i) == 1)
if __name__ == '__main__':
    main()

# Q.6
def main():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    printSequenceEvenNumbers(values)
    return 1
def printSequenceEvenNumbers(values: tuple) -> bool:
    if not values:
        return False
    for i in values:
        if i % 2 == 0:
            print(i)
    return True
if __name__ == '__main__':
    main()

# Q.7
def main():
    value = 26
    result = isPerfectNumber(value)
    print(result)
    return 1
def isPerfectNumber(number: int) -> bool:
    if number <= 0:
        return False
    return number == sum([i for i in range(1, number) if number % i == 0])
if __name__ == '__main__':
    main()

# Q.8
def main():
    value = 17
    result = isPrimeNumber(value)
    print(result)
    return 1
def isPrimeNumber(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i != 0:
            continue
        #if i not in [1, number]:
        return False
    return True
if __name__ == '__main__':
    main()

# Q.9
def main():
    value = "hello"
    result = reverseString(value)
    print(result)
    return 1
def reverseString(string: str) -> str:
    return string[::-1]
if __name__ == '__main__':
    main()

# Q.10
def main():
    value = 101
    result = isNumberInRange(value, 1, 100)
    print(result)
    return 1
def isNumberInRange(number: int, range_from: int, range_to: int) -> bool:
    return number in range(range_from, range_to + 1)
if __name__ == '__main__':
    main()

# Q.11
import string
def main():
    text = "The quick brown fox jumps over the lazy dog"
    result = isPangramText(text)
    print(result)
    return 1
def isPangramText(text: str) -> bool:
    alphabet = tuple(string.ascii_lowercase)
    for char in alphabet:
        if text.count(char) == 0:
            return False
    return True
if __name__ == '__main__':
    main()

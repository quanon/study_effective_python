def normalize(numbers):
  if iter(numbers) is iter(numbers):
    raise TypeError('Must supply a container')
  total = sum(numbers)
  result = []
  for number in numbers:
    percent = 100 * number / total
    result.append(percent)
  return result


if __name__ == '__main__':
  from read_numbers import ReadNumbers

  numbers = ReadNumbers('./numbers.txt')
  print(type(numbers))  # => <class 'read_numbers.ReadNumbers'>
  print(normalize(numbers))

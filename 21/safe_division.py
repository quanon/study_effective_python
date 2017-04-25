

def safe_division(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
  try:
    return number / divisor
  except OverflowError:
    if ignore_overflow:
      return 0
    else:
      raise
  except ZeroDivisionError:
    if ignore_zero_division:
      return float('inf')
    else:
      raise


if __name__ == '__main__':
  # safe_division(1.0, 10**500, True, True)
  # TypeError: safe_division() takes 2 positional arguments but 4 were given
  answer = safe_division(12, 4)
  print(answer)

  answer = safe_division(1.0, 10**500, ignore_overflow=True)
  print(answer)

  answer = safe_division(1.0, 0, ignore_zero_division=True)
  print(answer)

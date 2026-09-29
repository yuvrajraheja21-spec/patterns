def is_armstrong(n):
  digits = str(n)
  return n == sum(int(d) ** len(digits) for d in digits)

num = int(input(enter the number: )
  print(f"{num} is armstrong: {is_armstrong(num)}")

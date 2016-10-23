# [2016-07-25] Challenge #277 [Easy] Simplifying fractions
# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/

inputArray = ['4 8', '1536 78360', '51478 5536', '46410 119340', '7673 4729', '4096 1024']

def main():
  for item in inputArray:
  	numbers = [int(i) for i in item.split()]
  	print(numbers[0] // gcd(numbers[0], numbers[1]), numbers[1] // gcd(numbers[0], numbers[1]))

def gcd(a,b):
  while b: 
  	a, b = b, a%b
  return a

if __name__ == "__main__":
  main()

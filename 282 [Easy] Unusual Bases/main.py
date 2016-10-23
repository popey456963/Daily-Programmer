# [2016-09-05] Challenge #282 [Easy] Unusual Bases
# https://www.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/

inputArray = ["10 16", "10 32", "10 9024720", "F 10", "F 1", "F 111111", "F 100000", "F 10110110100111001"]

def main():
	print(generateFibNum(10))
	for item in inputArray:
		if item.split()[0] == "F":
			print(parseFib(item.split()[1]))
		else:
			print(parseDecimal(int(item.split()[1])))

def generateFibUpto(highest):
	fib = [1, 1]
	while(1):
		if fib[-1] > highest:
			break
		fib.append(fib[-1] + fib[-2])
	return fib

def generateFibNum(num):
	fib = [1, 1]
	for i in range(num - 2):
		fib.append(fib[-1] + fib[-2])
	return fib

def parseFib(num):
	total = 0
	fib = [int(i) for i in reversed(generateFibNum(len(num)))]
	for index, item in enumerate(num):
		if item == '1':
			total += fib[index]
	return total

def parseDecimal(num):
	start = True
	string = ""
	fib = [int(i) for i in reversed(generateFibUpto(num))]
	for index, item in enumerate(fib):
		if item <= num:
			string += "1"
			num -= item
			start = False
		else:
			if not start:
				string += "0"
	return string


if __name__ == "__main__":
	main()

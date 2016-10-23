# [2016-10-10] Challenge #287 [Easy] Kaprekar's Routine
# https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/

kaprekar_constant = 6174

def main():
    print("Largest Digit is: " + str(largest_digit(1849)))
    print("Descending Order is: " + str(desc_digits(1234)))
    print("Kaprekar Constant: " + str(kaprekar(5455)))

def largest_digit(num):
	return max([int(i) for i in str(num)])

def desc_digits(num, toReverse=True):
	return int("".join([str(j) for j in sorted([int(i) for i in str(num)], reverse=toReverse)]))

def kaprekar(num):
	iteration = 0
	while (1):
		if num == kaprekar_constant or num == 0:
			return iteration
		else:
			num = desc_digits(num) - desc_digits(num, False)
			iteration += 1

if __name__ == "__main__":
    main()

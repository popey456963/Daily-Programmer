# [2016-10-03] Challenge #286 [Easy] Reverse Factorial
# https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/

inputArray = ["120", "150", "3628800", "479001600", "6", "18"]

def main():
    for str_number in inputArray:
    	number = float(str_number)
    	factor = 2
    	while 1:
    		if number == 1:
    			print(str_number + ": " + str(factor - 1) + "!")
    			break
    		elif int(number) != number or number < 1:
    			print(str_number + ": NONE")
    			break
    		else:
    			number = number / factor
    			factor += 1



if __name__ == "__main__":
    main()

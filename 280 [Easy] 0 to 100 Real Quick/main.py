# [2016-08-22] Challenge #280 [Easy] 0 to 100, Real Quick
# https://www.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

inputArray = ["0111011100", "1010010000", "0011101110", "0000110000", "1111110001"]

def main():
  for item in inputArray:
    parseHand(item)

def parseHand(item):
  left = item[0:5]
  right = item[5:10]
  rightStart = False
  leftStart = False

  for i in range(4):
    if not leftStart:
      if left[i] == '1':
        leftStart = True
    else:
      if left[i] == '0':
        print("Invalid Combination")
        return

  for i in range(4, 0, -1):
    # If 1 to right of any zero
    if not rightStart:
      if right[i] == '1':
        rightStart = True
    else:
      if right[i] == '0':
        print("Invalid Combination")
        return

  print(left, right, 10 * countHand("".join(reversed(left))) + countHand(right))

def countHand(hand):
  return 5 * int(hand[0]) + len([i for i in hand[1:4] if i == '1'])

if __name__ == "__main__":
  main()

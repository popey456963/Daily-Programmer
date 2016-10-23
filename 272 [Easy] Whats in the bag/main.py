# [2016-06-20] Challenge #272 [Easy] What's in the bag?
# https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

import copy

count = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "_": 2}
inputArray = ["PQAREIOURSTHGWIOAE_", "LQTOONOEFFJZT", "AXHDRUIOR_XHJZUQEE"]

def main():
  print("==========")
  for item in inputArray:
    tempCount = copy.deepcopy(count)
    for letter in item:
      tempCount[letter] -= 1
    for item in tempCount:
      if tempCount[item] < 0:
        print("Too many " + item + "'s were taken.")
    inv_map = {}
    for k, v in tempCount.iteritems():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
    for i in reversed(range(0, 13)):
      if i in inv_map:
        print(str(i) + ": " + " ".join([str(j) for j in inv_map[i]]))

    print("==========")


if __name__ == "__main__":
  main()

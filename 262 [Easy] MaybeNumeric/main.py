# [2016-04-11] Challenge #262 [Easy] MaybeNumeric
# https://www.reddit.com/r/dailyprogrammer/comments/4eaeff/20160411_challenge_262_easy_maybenumeric/

inputArray = ["123", "44.234", "0x123N", "1..23", "123 234 345", "3.23e5", "1293712938712938172938172391287319237192837329", ".25", "2015 4 4`Challenge #`261`Easy", "234.2`234ggf 45`00`number string number (0)"]

def main():  
  for item in inputArray:
    for miniitem in item.split("`"):
      if miniitem.count(" ") > 0:
        print(miniitem, testArray(miniitem))
      else:
        print(miniitem, isnumber(miniitem))

def testArray(array):
  for ind in array.split():
    if not isnumber(ind):
      return False
  return True

def isnumber(number):
  if number.count(".") < 2:
    if 'e' not in number:
      for i in number:
        if i not in "01234567890.":
          return False
      return True
    else:
      temp = number.split("e")
      return isnumber(temp[0]) and isnumber(temp[1])
  else:
    return False

if __name__ == "__main__":
    main()

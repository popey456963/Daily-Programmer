# [2016-10-24] Challenge #289 [Easy] It's super effective!
# https://www.reddit.com/r/dailyprogrammer/comments/5961a5/20161024_challenge_289_easy_its_super_effective/

inputArray = [["fire", ["grass"]], ["water", ["normal", "steel", "ice", "dragon"]], ["fire", ["rock"]]]
types = ["normal", "fire", "water", "electric", "grass", "ice",
         "fighting", "poison", "ground", "flying", "psychic", "bug",
         "rock", "ghost", "dragon", "dark", "steel", "fairy"]
multiplierArray = {
  "a": 0,
  "b": 0.5,
  "c": 1,
  "d": 2
}
lookupTable = ["ccccccccccccbaccbc",
               "cbbcddcccccdbcbcdc",
               "cdbcbcccdcccdcbccc"]

def main():
  for item in inputArray:
    multiplier = 1
    for defence in item[1]:
      multiplier = multiplier * multiplierArray[lookupTable[types.index(item[0])][types.index(defence)]]
    print(item[0], "-->", " ".join(item[1]), str(multiplier) + "x")

if __name__ == "__main__":
  main()

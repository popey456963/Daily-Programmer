# [2016-03-28] Challenge #260 [Easy] Garage Door Opener
# https://www.reddit.com/r/dailyprogrammer/comments/4cb7eh/20160328_challenge_260_easy_garage_door_opener/

inputArray = ["button_clicked", "cycle_complete", "button_clicked", "button_clicked", "button_clicked", "button_clicked", "button_clicked", "cycle_complete"]
states = ["CLOSED", "CLOSING", "OPEN", "OPENING", "STOPPED_WHILE_CLOSING", "STOPPED_WHILE_OPENING"]
def main():
  currentState = states[0]
  for item in inputArray:
    if item == "cycle_complete":
      currentState = states[states.index(currentState) - 1]
    elif item == "button_clicked":
      if currentState == "CLOSED":
        currentState = "OPENING"
      elif currentState == "OPEN":
        currentState = "CLOSING"
      elif currentState == "CLOSING" or currentState == "OPENING":
        currentState = "STOPPED_WHILE_" + currentState
      elif currentState == "STOPPED_WHILE_CLOSING":
        currentState = "OPENING"
      elif currentState == "STOPPED_WHILE_OPENING":
        currentState = "CLOSING"
    print(currentState)


if __name__ == "__main__":
  main()

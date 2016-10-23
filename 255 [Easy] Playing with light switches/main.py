# [2016-02-22] Challenge #255 [Easy] Playing with light switches
# https://www.reddit.com/r/dailyprogrammer/comments/46zm8m/20160222_challenge_255_easy_playing_with_light/

inputArray = ['10', '3 6', '0 4', '7 3', '9 9']

def main():
    light_switches = int(inputArray[0])
    switches = [False for i in range(light_switches)]

    currentItem = 1

    while 1:
        if len(inputArray) > currentItem:
            light_range = sorted([int(i) for i in inputArray[currentItem].split()])
            light_range[1] += 1
            for i in range(light_range[0], light_range[1]):
                switches[i] = not switches[i]
        else:
            break

        currentItem += 1

    print(switches)

if __name__ == "__main__":
    main()
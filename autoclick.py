import pyautogui
import time

def main():
    #初始化
    print("This is a script to automatically click.\n\tCopyright(c) 2026 Zilin Zheng,\n\tunder Apache-2.0 license.")
    width = input("\nPlease enter the width. Default is 800px: ")
    if width == "" :
        width = 800
    else:
        width = int(width)
    height = input("Please enter the height. Default is 900px: ")
    if height == "" :
        height = 900
    else:
        height = int(height)
    sleep_time = input("Please enter the sleep time. Default is 15sec: ")
    if sleep_time == "" :
        sleep_time = 15
    else:
        sleep_time = float(sleep_time)

    #开始
    c = input("Start? [y/N]: ")
    for i in [5,4,3,2,1]:
        print("Start in " + str(i) + " seconds...")
        time.sleep(1)
    for i in range(3):
        print("")
        print("CTRL+C to EXIT!\nYou can also MOVE MOUSE to ANY CORNER of the screen to EXIT!")
    while c == "y" or c == "Y":
        pyautogui.click(width, height)
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
import pyautogui
# import time
import ReadEmail
from BuyCard import BuyCard

pyautogui.FAILSAFE = True
read_email = ReadEmail
global email


def main():
    global email
    email = read_email.values[0]
    BuyCard.buy(email)


if __name__ == "__main__":
    main()


# # Tool for identifying position of something
# #
# time.sleep(5)
# pyautogui.scroll(-10)
# time.sleep(5)
# print(pyautogui.position())

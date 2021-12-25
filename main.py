import pyautogui
# import time
import ReadEmail
from BuyCard import BuyCard

pyautogui.FAILSAFE = True
read_email = ReadEmail
buy_card = BuyCard()
global email


def main():
    global email
    email = read_email.values[0]
    email = 'nguyen.hoang.jimmy42@gmail.com'
    BuyCard.buy(email)


if __name__ == "__main__":
    main()

# # Tool for identifying position of something
# #
# # time.sleep(5)
# # pyautogui.scroll(-10)
# # time.sleep(5)
# # print(pyautogui.position())

import pyautogui
import time


class BuyCard(object):

    @staticmethod
    def buy(email):
        # # opens QuickTime Player
        # pyautogui.moveTo(825, 765, 1.5)
        # pyautogui.click()
        # time.sleep(5)
        #
        # # cancels finder
        # pyautogui.moveTo(900, 510, 1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # right click QuickTime Player
        # pyautogui.moveTo(825, 765, 1.5)
        # pyautogui.rightClick()
        # time.sleep(1)
        #
        # # starts new Screen Recording
        # pyautogui.moveTo(890, 590, .5)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # hits Record
        # pyautogui.moveTo(820, 675, .5)
        # pyautogui.click()
        # time.sleep(1)

        # opens Google from PyCharm
        pyautogui.moveTo(515, 770, 1.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(10)

        # clicks on Jimmy profile
        pyautogui.moveTo(555, 410, 1)
        pyautogui.click()
        time.sleep(5)

        # Go to search bar and type amazon.com
        pyautogui.moveTo(150, 85, 1)
        pyautogui.click()
        pyautogui.typewrite('amazon.com\n', 0.15)
        time.sleep(5)

        # Navigate to gift cards
        pyautogui.moveTo(110, 180, .5)
        pyautogui.click()
        time.sleep(5)

        # scroll to eGift cards and click See Options
        pyautogui.scroll(-15)
        time.sleep(2)
        pyautogui.moveTo(265, 600, 1)
        pyautogui.click()
        time.sleep(7)

        # Choose stocking photo
        pyautogui.moveTo(550, 565, 2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # Scrolls so email is visible
        pyautogui.scroll(-10)
        time.sleep(2)
        # Goes to $25 option
        pyautogui.moveTo(550, 435, .2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)

        # Moves to email section
        pyautogui.moveTo(550, 525, 1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # Types email
        # change email to email[0] after testing
        pyautogui.typewrite(email[0], 0.3)
        time.sleep(1)

        # Scrolls back up and clicks 'Buy Now'
        pyautogui.scroll(10)
        pyautogui.moveTo(1100, 440, 1)
        pyautogui.click()
        time.sleep(5)

        # Sign in
        pyautogui.moveTo(635, 440, .2)
        pyautogui.click()
        time.sleep(7)

        # Cancel Last Pass
        pyautogui.moveTo(1110, 260, .5)
        pyautogui.click()
        time.sleep(1)

        # Buy
        pyautogui.moveTo(1045, 280, .2)
        time.sleep(5)
        #
        # # Stops screen recording
        # pyautogui.moveTo(765, 13, 1)
        # pyautogui.click()
        # time.sleep(2)
        #
        # # Exits out of preview
        # pyautogui.moveTo(63, 39, 1)
        # time.sleep(1)
        #
        # # Reopens Google
        # pyautogui.moveTo(515, 770, 1.5)
        # pyautogui.click()
        # time.sleep(2)
        #
        # # Opens new tab and opens google photos
        # pyautogui.moveTo(355, 50, 1.5)
        # pyautogui.click()
        # time.sleep(.2)
        # pyautogui.typewrite('http://photos.google.com/\n', .1)
        # time.sleep(5)
        #
        # # Opens Finder
        # pyautogui.moveTo(360, 765, 1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # Accesses desktop
        # pyautogui.moveTo(65, 195, 1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # Turns into grid display
        # pyautogui.moveTo(605, 50, .5)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # Hovers over .mov file and drags to google photos
        # pyautogui.moveTo(450, 125, .25)
        # pyautogui.dragTo(650, 390, 5)

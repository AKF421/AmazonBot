import pyautogui
import keyboard
import time


class BuyCard(object):

    @staticmethod
    def buy(email):
        # opens QuickTime Player
        pyautogui.moveTo(800, 765, 1.5)
        pyautogui.click()
        time.sleep(5)

        # cancels finder
        pyautogui.moveTo(900, 510, 1)
        pyautogui.click()
        time.sleep(1)

        # right click QuickTime Player
        pyautogui.moveTo(800, 765, 1.5)
        pyautogui.rightClick()
        time.sleep(1)

        # starts new Screen Recording
        pyautogui.moveTo(890, 590, .5)
        pyautogui.click()
        time.sleep(1)

        # hits Record
        pyautogui.moveTo(820, 675, .5)
        pyautogui.click()
        time.sleep(1)

        # opens Google from PyCharm
        pyautogui.moveTo(550, 770, 1.5)
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
        keyboard.write("amazon.com")
        # type("amazon.com")
        pyautogui.press('enter')
        time.sleep(5)

        # Navigate to gift cards
        pyautogui.moveTo(110, 180, .5)
        pyautogui.click()
        time.sleep(5)

        # scroll to eGift cards and click See Options
        pyautogui.scroll(-10)
        time.sleep(2)
        pyautogui.moveTo(265, 600, 1)
        pyautogui.click()
        time.sleep(7)

        # Choose stocking photo
        pyautogui.moveTo(550, 565, .5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # Scrolls so email is visible
        pyautogui.scroll(-10)
        time.sleep(2)
        # Goes to $25 option
        pyautogui.moveTo(560, 435, .2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)

        # Backspaces and types in 'Not Jimmy'
        pyautogui.moveTo(655, 590, 1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(.2)

        for _ in "Jimmy Nguyen":
            pyautogui.press('backspace')
            time.sleep(.2)

        keyboard.write("Not Jimmy :]")
        # type("Not Jimmy :]")
        time.sleep(1)
        # Moves to email section
        pyautogui.moveTo(560, 525, 1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # Types email
        # change email to email[0] after testing
        time.sleep(1)
        keyboard.write(email[0])
        # type(email[0])
        time.sleep(1)

        # Scrolls back up and clicks 'Buy Now'
        pyautogui.scroll(10)
        pyautogui.moveTo(1100, 440, 1)
        pyautogui.click()
        time.sleep(5)

        # Sign in
        pyautogui.moveTo(635, 440, .2)
        pyautogui.click()
        time.sleep(10)

        # Cancel Last Pass
        pyautogui.moveTo(1110, 260, .5)
        pyautogui.click()
        time.sleep(1)

        # Buy
        pyautogui.moveTo(1045, 280, .2)
        time.sleep(1)
        # pyautogui.click()
        time.sleep(10)

        # Stops screen recording
        pyautogui.moveTo(691, 13, 1)
        pyautogui.click()
        time.sleep(2)

        # Exits out of preview
        pyautogui.moveTo(63, 39, 1)
        pyautogui.click()
        time.sleep(1)

        # Reopens Google
        pyautogui.moveTo(550, 770, 1.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # Opens new tab and opens google photos
        pyautogui.moveTo(355, 50, 1.5)
        pyautogui.click()
        time.sleep(2)

        keyboard.write("photos.google.com")
        pyautogui.press('enter')
        # type("photos.google.com")
        time.sleep(5)

        # Opens Finder
        pyautogui.moveTo(360, 765, 1)
        pyautogui.click()
        time.sleep(1)

        # Accesses desktop
        pyautogui.moveTo(65, 195, 1)
        pyautogui.click()
        time.sleep(1)

        # Turns into grid display
        pyautogui.moveTo(704, 50, .5)
        pyautogui.click()
        time.sleep(1)

        # Hovers over .mov file and drags to google photos
        pyautogui.moveTo(465, 125, .25)
        time.sleep(2)
        pyautogui.dragTo(800, 670, 5, button='left')
        time.sleep(60)

        # Clicks on video and creates shared link
        pyautogui.moveTo(440, 325, 1)
        time.sleep(1)

        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(1050, 133, 2)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(505, 640, 2)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(780, 490, 2)
        time.sleep(1)
        pyautogui.click()

        time.sleep(5)
        pyautogui.click()
        time.sleep(1)

        # Open discord
        pyautogui.moveTo(650, 765, 1)
        pyautogui.click()
        time.sleep(1)

        # Paste link
        pyautogui.moveTo(415, 690, 1)
        pyautogui.click()
        time.sleep(1)

        pyautogui.rightClick()
        time.sleep(1)
        pyautogui.moveTo(540, 670, 1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.moveTo(415, 690, 1)
        pyautogui.click()
        time.sleep(1)
        keyboard.write("A program bought the gift card and recorded this video! If something went wrong, blame my creator.")
        pyautogui.press('enter')
        # type("A program bought the gift card and recorded this video! If something went wrong, blame my creator.")

    # @staticmethod
    # def type(phrase):
    #     for x in phrase:
    #         pyautogui.press(x)
    #         time.sleep(1.5)

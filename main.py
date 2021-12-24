import pyautogui
import sched, time

s = sched.scheduler(time.time, time.sleep)


def print_mouse_position(sc):
    print(pyautogui.position())

    s.enter(2, 1, print_mouse_position, (sc,))


s.enter(2, 1, print_mouse_position, (s,))
s.run()

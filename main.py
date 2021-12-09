import asyncio
import websockets
import math
import pyautogui
import mouse
from mouse import _os_mouse
from time import time

ACC = 4.0

simulated_mouse_codes = _os_mouse.simulated_mouse_codes
WHEEL = _os_mouse.WHEEL
VERTICAL = _os_mouse.VERTICAL
HORIZONTAL = _os_mouse.HORIZONTAL
WHEEL_DELTA = _os_mouse.WHEEL_DELTA
user32 = _os_mouse.user32

print(mouse.get_position())

# for i in range(20):
#   print(mouse.get_position())
#   mouse.move(0, 0, absolute=False)
#   print(mouse.get_position())


async def handle(websocket):
  lastTime = time()
  spd = 1
  async for message in websocket:
    print(message)
    try:
      msg = message.split(':')
      action = ''
      if len(msg) == 1:
        action = msg[0]
      else:
        [action, args] = msg
      if action == 'clk':
        mouse.click()
      elif action == 'rclk':
        mouse.click(button=mouse.RIGHT)
      elif action == 'dbc':
        mouse.double_click()
      elif action == 'prs':
        # print('pressing...')
        mouse.press()
      elif action == 'rls':
        # print('releasing...')
        mouse.release()
      elif action == 'mv':
        x, y = map(float, args.split(','))
        x = math.ceil(x) if x > 0 else math.floor(x)
        y = math.ceil(y) if y > 0 else math.floor(y)

        t0 = lastTime
        t = time()
        lastTime = t

        duration = t - t0

        spd += (0.02 - duration) * ACC
        spd = max(1, spd)
        mouse.move(x * spd, y * spd, absolute=False)
      elif action == 'scr':
        x, y = map(float, args.split(','))
        # x = 1 if x > 0 else -1
        # y = 1 if x > 0 else -1
        x = math.ceil(x) if x > 0 else math.floor(x)
        y = math.ceil(y) if y > 0 else math.floor(y)
        x = -x

        # mouse.wheel(y)
        code = simulated_mouse_codes[(WHEEL, VERTICAL)]
        user32.mouse_event(code, 0, 0, int(y * .2 * WHEEL_DELTA), 0)
        code = simulated_mouse_codes[(WHEEL, HORIZONTAL)]
        user32.mouse_event(code, 0, 0, int(x * .1 * WHEEL_DELTA), 0)
      elif action == 'act':
        x, y = map(float, args.split(','))

        if abs(x) > abs(y): # horizontal
          if x > 0:
            print('right')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('win')
            pyautogui.press('left')
            pyautogui.keyUp('win')
            pyautogui.keyUp('ctrl')
          else:
            print('left')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('win')
            pyautogui.press('right')
            pyautogui.keyUp('win')
            pyautogui.keyUp('ctrl')
          pass
        else: # vertical
          if y < 0: # up
            print('up')
            pyautogui.keyDown('winleft')
            pyautogui.press('tab')
            pyautogui.keyUp('winleft')
            pass
          else: #down
            print('down')
            # pyautogui.keyDown('winleft')
            # pyautogui.press('d')
            # pyautogui.keyUp('winleft')
            pass
      elif action == 'swp':
        dir = args
        if dir == 'left':
          pyautogui.keyDown('alt')
          pyautogui.press('right')
          pyautogui.keyUp('alt')
        elif dir == 'right':
          pyautogui.keyDown('alt')
          pyautogui.press('left')
          pyautogui.keyUp('alt')
    except Exception as e:
      print(e)
      pass
    # print(x, y)

    # pyautogui.moveRel(x, y, 0)

async def main():
  async with websockets.serve(handle, "0.0.0.0", 3000):
    await asyncio.Future()

asyncio.run(main())

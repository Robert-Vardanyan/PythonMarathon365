import time
import sys
from colorama import init, Fore

init(autoreset=True)

frames = [
    Fore.YELLOW + """
   _________
  /         \\
 /   COIN   \\
 |           |
 \\           /
  \\_________/
""",
    Fore.YELLOW + """
    _______
   /       \\
  |  COIN  |
  |        |
   \\______/
""",
    Fore.YELLOW + """
     _____
    |     |
    |COIN |
    |     |
     -----
""",
    Fore.YELLOW + """
     ___
    |   |
    |COIN|
    |   |
     ---
""",
    Fore.YELLOW + """
      _
     | |
     | |
     | |
      -
""",
]

def animate_coin(duration=3, speed=0.2):
    end_time = time.time() + duration
    frames_cycle = frames + frames[-2:0:-1]  
    idx = 0

    while time.time() < end_time:
        sys.stdout.write('\033c') 
        print(frames_cycle[idx % len(frames_cycle)])
        idx += 1
        time.sleep(speed)

def coin_flip():
    print(Fore.CYAN + "🪙 Coin Flip Simulator with Vertical Flip Animation 🪙")
    input(Fore.YELLOW + "Press Enter to flip the coin...")

    animate_coin()

    import random
    result = random.choice(["Heads", "Tails"])
    color = Fore.GREEN if result == "Heads" else Fore.MAGENTA
    print(color + f"The coin landed on: {result}")

if __name__ == "__main__":
    coin_flip()

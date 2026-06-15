import random
import time
import os

chars = "01"

while True:
    line = "".join(random.choice(chars) for _ in range(80))
    print(line)
    time.sleep(0.05)

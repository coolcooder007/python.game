import time
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print("HACKING INSTAGRAM ACCOUNT...\n")

for i in range(20):
    password = "".join(random.choice(chars) for _ in range(12))
    print("Trying password:", password)
    time.sleep(0.2)

print("\nACCESS GRANTED")

import os
import time

def animacja_papugi():
    papuga = ["🦜", "o", "🦜", "k"]
    while True:
        for frame in papuga:
            os.system('cls' if os.name == 'nt' else 'clear')  # Czyści ekran
            print(frame)
            time.sleep(0.2)  # Czas między klatkami

animacja_papugi()
import time
from datetime import datetime

def countdown():
    try:
        target = input("Enter future time (YYYY-MM-DD HH:MM:SS): ")
        target_time = datetime.strptime(target, "%Y-%m-%d %H:%M:%S")
        print("⏳ Countdown started...\n")
        while True:
            now = datetime.now()
            diff = target_time - now
            if diff.total_seconds() <= 0:
                print("⏰ Time's up!")
                break
            print(f"\rTime left: {diff}", end="")
            time.sleep(1)
    except:
        print("❌ Invalid format. Example: 2025-06-23 10:00:00")

if __name__ == "__main__":
    countdown()

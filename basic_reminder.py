
import time

def reminder():
    note = input("Enter reminder note: ")
    try:
        mins = int(input("Remind after how many minutes? "))
        print(f"⏳ Setting reminder for '{note}' in {mins} minutes...\n")
        time.sleep(mins * 60)
        print(f"\n🔔 Reminder: {note}")
    except:
        print("❌ Invalid input.")

if __name__ == "__main__":
    reminder()

def tip_splitter():
    try:
        bill = float(input("Enter bill amount: ₹"))
        tip_percent = float(input("Enter tip percentage (%): "))
        people = int(input("Number of people: "))
        tip_amount = bill * tip_percent / 100
        total = bill + tip_amount
        per_person = total / people
        print(f"\nTotal Bill: ₹{total:.2f}")
        print(f"Each Person Pays: ₹{per_person:.2f}")
    except:
        print("❌ Invalid input. Try again.")

if __name__ == "__main__":
    tip_splitter()

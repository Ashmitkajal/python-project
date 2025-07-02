import random

def quote_generator():
    quotes = [
        "“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb",
        "“Stay hungry, stay foolish.” – Steve Jobs",
        "“You miss 100% of the shots you don’t take.” – Wayne Gretzky",
        "“Whether you think you can or you think you can’t, you’re right.” – Henry Ford",
        "“The harder you work for something, the greater you’ll feel when you achieve it.” – Anonymous"
    ]
    print("\n✨ Your Quote:\n")
    print(random.choice(quotes))

if __name__ == "__main__":
    quote_generator()

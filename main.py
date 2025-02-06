def update_screen(message):
    print("\n" + message)

def main():
    update_screen("Welcome to the Book Recommendation App!\n")

    print("Based on your preferred genre and age, we'll suggest a book to read.")
    genre = input("Pick a genre (fantasy, mystery, self-help, romance): ").lower()
    age = int(input("Enter your age: "))

    if age < 12 and genre == "fantasy":
        recommendation = "You might enjoy 'The Chronicles of Narnia' by C.S. Lewis or 'Harry Potter and the Sorcerer’s Stone' by J.K. Rowling!"
    elif genre == "fantasy":
        recommendation = "Read 'The Hobbit' by J.R.R. Tolkien, 'Mistborn' by Brandon Sanderson, or 'The Name of the Wind' by Patrick Rothfuss."
    elif age < 12 and genre == "mystery":
        recommendation = "Try 'Nancy Drew: The Secret of the Old Clock' by Carolyn Keene or 'The Hardy Boys: The Tower Treasure' by Franklin W. Dixon!"
    elif genre == "mystery":
        recommendation = "Try 'Gone Girl' by Gillian Flynn, 'The Girl with the Dragon Tattoo' by Stieg Larsson, or 'The Silent Patient' by Alex Michaelides."
    elif age < 16 and genre == "self-help":
        recommendation = "Read 'The 7 Habits of Highly Effective Teens' by Sean Covey!"
    elif genre == "self-help":
        recommendation = "Read 'Atomic Habits' by James Clear, 'The Subtle Art of Not Giving a F*ck' by Mark Manson, or 'How to Win Friends and Influence People' by Dale Carnegie."
    elif genre == "romance" and age < 18:
        recommendation = "Try 'To All the Boys I’ve Loved Before' by Jenny Han or 'Eleanor & Park' by Rainbow Rowell!"
    elif genre == "romance":
        recommendation = "Explore 'Pride and Prejudice' by Jane Austen, 'The Notebook' by Nicholas Sparks, or 'Me Before You' by Jojo Moyes."
    elif genre == "science fiction":
        recommendation = "Check out 'Dune' by Frank Herbert, 'The Martian' by Andy Weir, or 'Neuromancer' by William Gibson."
    elif genre == "historical fiction":
        recommendation = "Read 'The Book Thief' by Markus Zusak, 'All the Light We Cannot See' by Anthony Doerr, or 'The Nightingale' by Kristin Hannah."
    else:
        recommendation = "We recommend exploring something new! How about 'The Hobbit' by J.R.R. Tolkien or 'The Martian' by Andy Weir?"

    update_screen("Your Book Recommendation:\n" + recommendation)

main()
def main():
    score = get_valid_score()
    choice = ''
    while choice != 'Q':
        print("\nMenu:")
        print("(G)et a valid score between 0 and 100")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose your option: ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"Result: {get_score(score)}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell. See you next time")
        else:
            print("Please choose a valid option")

def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100")
        score = float(input("Enter a valid score (0-100): "))
    return score

def get_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * int(score))

main()

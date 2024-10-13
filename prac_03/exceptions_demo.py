"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when the user enters a value that cannot be converted into integer
2. When will a ZeroDivisionError occur?
when the user enters 0 as input in denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (can't be zero): "))
    while denominator == 0:
        print("Denominator can't be zero")
        print("Enter the valid denominator")
        denominator = int(input("Enter the denominator (can't be zero): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

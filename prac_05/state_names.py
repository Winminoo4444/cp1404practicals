"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD":"Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

#4. Write a loop that prints all the states and names neatly lined up with string formatting
for state_code in CODE_TO_NAME:
     print(f"{state_code} is {CODE_TO_NAME[state_code]}")

#5. This code uses the "Look Before You Leap" (LBYL) approach to checking if the key is in the dictionary. Change this to use exceptions and the "Easier to Ask Forgiveness than Permission" (EAFP) approach.
state_code = input("Please enter state name: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:(
        print("Invalid state name."))
    state_code = input("Please enter state name: ").upper()

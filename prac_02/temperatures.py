MENU = """
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("temperature in celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("temperature in fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Please choose the valid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32
def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

main()
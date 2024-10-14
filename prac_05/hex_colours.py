COLOURS_CODES = {
    "Absolute Zero": "#0048ba",
    "Aqua": "#00ffff",
    "Azure1": "#f0ffff",
    "BlueViolet":"#8a2be2",
    "Baby Blue":"#89cff0",
    "Baker-Miller Pink":"#ff91af",
    "Black Coffee":"#3b2f2f",
    "Brandeis Blue": "#0070ff",
    "Brass": "#b5a642",
    "Bright Green":"#66ff00"}

def main():
    """Validating colour names"""
    color_names = validate_color_names()
    while color_names != "":
        color_code = COLOURS_CODES[color_names]
        print(f"{color_code}")
        color_names = validate_color_names()

def validate_color_names():
    """Error checking colour names"""
    color_names = input("Enter the color name: ").title()
    while color_names not in COLOURS_CODES:
        print("Invalid Color Name")
        color_names = input("Color Name: ").title()
    return color_names

main()
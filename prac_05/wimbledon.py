FILENAME = "wimbledon.csv"
def main():
    """Read file"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
    champions = get_data(data, 2)
    countries = get_data(data, 1)
    country_counts = count_item(countries)
    champion_counts = count_item(champions)
    print("Wimbledon Champions:")
    for name in sorted(champion_counts.keys()):
        print(f"{name}: {champion_counts[name]}")
    sorted_countries = sorted(country_counts.keys())
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

def get_data(data, number):
    """Get the data"""
    items = []
    for line in data[1:]:
        items.append(line.strip().split(",")[number])
    return items

def count_item(items):
    """Get item counts"""
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts
main()


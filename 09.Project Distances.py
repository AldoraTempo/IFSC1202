def load_distance_table():
    """Load distance table from user input."""
    distance_table = []
    print("Enter the distance table (row by row) with cities separated by commas.")
    print("End input with an empty line.")
    
    while True:
        row = input("Enter row: ").strip()
        if row == "":
            break
        distance_table.append(row.split(","))
    
    return distance_table

def print_distance_table(distance_table):
    """Print the distance table."""
    for row in distance_table:
        print(', '.join(row))

def find_city_index(city_list, city_name):
    """Find the index of the city in the list."""
    try:
        return city_list.index(city_name)
    except ValueError:
        return -1

def main():
    # Load the distance table
    distance_table = load_distance_table()
    
    # Print the distance table
    print("Distance Table:")
    print_distance_table(distance_table)

    # Prompt for From City and To City
    from_city = input("Enter the From City: ").strip()
    to_city = input("Enter the To City: ").strip()

    # Find indices of From City and To City
    from_city_index = find_city_index([row[0] for row in distance_table], from_city)
    to_city_index = find_city_index(distance_table[0], to_city)

    # Validate the inputs and output the distance
    if from_city_index == -1:
        print("Invalid From City")
    elif to_city_index == -1:
        print("Invalid To City")
    else:
        distance = distance_table[from_city_index][to_city_index]
        print(f"Distance from {from_city} to {to_city} is: {distance} miles")

if __name__ == "__main__":
    main()

import csv

def load_distance_table(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        distance_table = [row for row in reader]
    return distance_table

def print_distance_table(table):
    for row in table:
        print(', '.join(row))

def get_city_index(city, column):
    if city in column:
        return column.index(city)
    return -1

def main():
    file_path = 'distances.csv'  # Replace with your CSV file path
    distance_table = load_distance_table(file_path)
    
    print("Distance Table:")
    print_distance_table(distance_table)
    
    from_city = input("Enter From City: ")
    to_city = input("Enter To City: ")
    
    header = distance_table[0]
    first_column = [row[0] for row in distance_table]

    from_index = get_city_index(from_city, first_column)
    if from_index == -1:
        print("Invalid From City")
        return

    to_index = get_city_index(to_city, header)
    if to_index == -1:
        print("Invalid To City")
        return
    
    distance = distance_table[from_index][to_index]
    print(f"Distance from {from_city} to {to_city} is: {distance}")

if __name__ == "__main__":
    main()

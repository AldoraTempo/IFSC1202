def read_constitution(file_path):
    """
    Reads the constitution text file and returns a list of lines.
    Each line in the list is stripped of newline characters.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def find_section(lines, search_term, current_line):
    """
    Finds the section in the constitution containing the search term.
    It returns a tuple (start_line, end_line) representing the section range.
    """
  
    start_line = current_line
    while start_line > 0 and lines[start_line - 1]:
        start_line -= 1
      
    end_line = current_line
    while end_line < len(lines) and lines[end_line]:
        end_line += 1
    
    return start_line, end_line

def search_constitution(file_path):
    """
    Prompts for a search term, searches through the constitution, and prints the relevant sections.
    """
    lines = read_constitution(file_path)
    visited_sections = set()  
    
    while True:
        search_term = input("Enter a search term (blank to exit): ").strip()
        
        if not search_term:
            print("Exiting the program.")
            break
        
        for current_line in range(len(lines)):
            if search_term.lower() in lines[current_line].lower():
              
                start_line, end_line = find_section(lines, search_term, current_line)
                
                if (start_line, end_line) not in visited_sections:
                    visited_sections.add((start_line, end_line))
                    print(f"\nSection from line {start_line + 1} to {end_line}:")
                    for i in range(start_line, end_line):
                        print(f"{i + 1}: {lines[i]}")
                    print("\n" + "-" * 50)


file_path = 'constitution.txt' 
search_constitution(file_path)


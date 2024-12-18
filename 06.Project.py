def merge_files():
    input_file_path = '06.Project Input File.txt'
    merge_file_path = '06.Project Merge File.txt'
    output_file_path = '06.Project Output File.txt'
    
    input_count = 0
    merge_count = 0
    output_count = 0

    # Open output file for writing
    with open(output_file_path, 'w') as output_file:
        # Open and read the input file
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                input_count += 1
                output_file.write(line)  # Copy line to output
                output_count += 1

                # Check for the specific marker in the line
                if 'Insert Merge File Here' in line:
                    # If found, open and read the merge file
                    with open(merge_file_path, 'r') as merge_file:
                        for merge_line in merge_file:
                            merge_count += 1
                            output_file.write(merge_line)  # Copy merge line to output
                            output_count += 1

        # After merge file is processed, continue with input file until the end
        input_file.seek(0)  # Reset to the start of the input file
        for line in input_file:
            input_count += 1
            output_file.write(line)  # Copy remaining lines to output
            output_count += 1

    # Print the counts of records
    print(f"Number of records in Input File: {input_count}")
    print(f"Number of records in Merge File: {merge_count}")
    print(f"Number of records in Output File: {output_count}")

# Run the merge function
merge_files()

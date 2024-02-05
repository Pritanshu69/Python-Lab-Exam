input_file_path = "file1.txt"
output_file_path = "output_file.txt"

# Read each line from file1 and copy to output_file with line numbers
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    line_number = 1

    for line in input_file:
        # Add line number at the beginning of each line
        line_with_number = f"{line_number}: {line}"
        
        # Write the line to the output file
        output_file.write(line_with_number)
        
        # Increment the line number
        line_number += 1

print(f"Lines from {input_file_path} copied to {output_file_path} with line numbers.")

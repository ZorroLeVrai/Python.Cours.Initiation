import os
import sys

def modify_file_path(file_path):
    # Split the file path into the directory, file name, and extension
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    
    # Add '_out' to the file name before the extension
    new_filename = f"{name}_out{ext}"
    
    # Join the directory and new file name to get the modified path
    return os.path.join(directory, new_filename)

if sys.argv < 2:
    print("You must provide the file path")
    exit(1)

input_file = sys.argv[0]
output_file = modify_file_path(input_file)

# Open the Latin-1 file and read it, then write it to a new file in UTF-8 format
with open(input_file, 'r', encoding='latin-1') as file_in:
    with open(output_file, 'w', encoding='utf-8') as file_out:
        for line in file_in:
            file_out.write(line)

print(f"The file has been successfully converted to UTF-8 and saved as {output_file}")

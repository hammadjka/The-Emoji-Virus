import os
import glob
import string
def merge_text_files(directory_path, merged_file_name):
    # Get a list of all text files in the directory
    file_list = glob.glob(os.path.join(directory_path, "*.txt"))
    
    # Open the merged file for writing
    with open(merged_file_name, "w") as merged_file:
        # Loop through the text files and append their contents to the merged file
        for file_name in file_list:
            with open(file_name, "r") as text_file:
                merged_file.write(text_file.read())

def remove_whitespace(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                stripped_line = line.strip()
                stripped_line = stripped_line.translate(str.maketrans('', '', string.punctuation))
                if stripped_line:
                    output_file.write(stripped_line + '\n')




#merge_text_files("C:/Users/hamma/Desktop/Dataset", "Data.txt")
remove_whitespace("C:/Users/hamma/Desktop/Data.txt", "C:/Users/hamma/Desktop/Data2.txt")
#remove_whitespace("C:/Users/hamma/Desktop/Mountain Madness/Data2.txt", "C:/Users/hamma/Desktop/Mountain Madness/Data2.txt")
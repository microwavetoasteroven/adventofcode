import re

total_of_numbers = 0

def find_first_number(text):
    match = re.search(r'\d', text)
    if match:
        return match.group()
    else:
        return 0

def process_line(line):
    global total_of_numbers
    combined = f"{find_first_number(line)}{find_first_number(line[::-1])}"
    total_of_numbers += int(combined)

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            process_line(line)

# Example usage
file_path = 'numbers.txt'
process_file(file_path)
print(total_of_numbers)



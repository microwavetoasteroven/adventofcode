import re

list_of_numbers = []

def find_first_number(text):
    match = re.search(r'\d', text)
    if match:
        return match.group()
    else:
        return None

def find_last_number(text):
    matches = re.findall(r'\d', text)
    if matches:
        return matches[-1]
    else:
        return None

def process_line(line):
    first = find_first_number(line)
    last = find_last_number(line)
    combined = f"{first}{last}"
    list_of_numbers.append(int(combined))

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            process_line(line)

# Example usage
file_path = 'numbers.txt'
process_file(file_path)
total = sum(list_of_numbers)
print(total)


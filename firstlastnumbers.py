import re

total_of_numbers = 0
numbers_words_dict = {'one':1,
                      'two':2,
                      'three':3,
                      'four':4,
                      'five':5,
                      'six':6,
                      'seven':7,
                      'eight':8,
                      'nine':9,
                      'enin':9,
                      'thgie':8,
                      'neves':7,
                      'xis':6,
                      'evif':5,
                      'ruof':4,
                      'eerht':3,
                      'owt':2,
                      'eno':1
                      }

def find_first_number(text,first=True):
    last_pattern = re.compile(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)',re.IGNORECASE)
    pattern = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)',re.IGNORECASE)
    if first:
        match = pattern.search(text)
    else:
        match = last_pattern.search(text)
    if len(match.group()) > 1:
        return numbers_words_dict[match.group()]
    if match:
        return match.group()
    else:
        return 0

def process_line(line):
    global total_of_numbers
    total_of_numbers += int(f"{find_first_number(line)}{find_first_number(line[::-1],False)}")

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            process_line(line)

# Example usage
file_path = 'numbers.txt'
process_file(file_path)
print(total_of_numbers)

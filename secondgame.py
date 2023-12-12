import re
import json

pattern_dict = {}
# 12 red cubes, 13 green cubes, and 14 blue cubes
rules = {'red':12,
         'green':13,
         'blue':14}

def process_line(line):
    global pattern_dict
    pattern = re.compile(r'\d[^:]*')
    match = pattern.search(line)
    if match:
        pattern_to_end = re.compile(r':.*')
        string_of_values = pattern_to_end.search(line).group()[1:].strip()
        internal_list = string_of_values.split(';')
        new_internal_list = []
        for item in internal_list:
            tiny_list = []
            internal_internal_list = item.split(',')
            for smaller_item in internal_internal_list:
                two_values = smaller_item.strip().split(' ')
                tiny_list.append({two_values[1]:int(two_values[0])})
            new_internal_list.append(tiny_list)
        pattern_dict[int(match.group())] = new_internal_list


def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            process_line(line)

# Example usage
file_path = 'secondgamenumbers.txt'
process_file(file_path)
print(json.dumps(pattern_dict,indent=4))


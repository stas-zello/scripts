import sys
import json
from collections import defaultdict

delimeter = "`"

def parse_file(input_file):
    file_dictionary = {}
    try:
        json_data = json.load(input_file)
        file_dictionary = parse_json(json_data)
    except:
        input_file.seek(0)
        file_dictionary = parse_text_file(input_file)
    return file_dictionary

def parse_text_file(input_file):
    file_dictionary = {}
    lines = input_file.readlines()
    for line in lines:
        print(line)
        if line[0]=="#":
            continue
        else:
            tokens = line.split()
            if len(tokens) == 1:
                file_dictionary[tokens[0]] = "blank"
            elif len(tokens) == 2:
                file_dictionary[tokens[0]] = tokens[1]
    print(file_dictionary)
    return file_dictionary

def parse_json(json_data):
    file_dictionary = {}
    for key in json_data.keys():
        file_dictionary[key] = str(json_data[key])
    return file_dictionary

def merge_configurations(file_dictionaries):
    with open("total_config.csv","w") as output_file:
        first_line = ["Parameter name"]
        all_key_dictionary = {}
        for file_name, a_dictionary in file_dictionaries:
            first_line.append(file_name)
            all_key_dictionary = {**all_key_dictionary,**a_dictionary}
        output_file.write(delimeter.join(first_line)+"\n")
        key_list = list(all_key_dictionary.keys())
        all_configs = defaultdict(list)
        for file_name, a_dictionary in file_dictionaries:
            for config_key in key_list:
                if config_key in a_dictionary:
                    all_configs[config_key].append(a_dictionary[config_key])
                else:
                    all_configs[config_key].append("NOT IN CONFIG")
        add_configs_to_file(all_configs, output_file)

def add_configs_to_file(all_configs, output_file):
    for key in all_configs:
        output_file.write(key + delimeter + delimeter.join(all_configs[key])+"\n")
    return

def create_input_file_list(input_filename):
    with open(input_filename, "r") as input_file:
        return input_file.readlines() 
    
def main():
    print("Usage /`python3 conf_parser.py <input file listing .conf files> <output file name> <sperator character (default `)>")
    input_filename = sys.argv[1:2][0]
    output_filename = sys.argv[2:3][0]
    if len(sys.argv) == 4:
        delimeter = sys.argv[3:4][0]
        print("Seperator specified: " + delimeter)

    print("Analyzing files listed in: " + input_filename)
    print("Outputting to: " + output_filename)
    file_list = create_input_file_list(input_filename)
    file_dictionaries = []
    for file_name in file_list:
        file_name = file_name.rstrip()
        with open(file_name) as input_file:
            file_dictionaries.append((file_name,parse_file(input_file)))
    merge_configurations(file_dictionaries)

if __name__ == "__main__":
    main()
                
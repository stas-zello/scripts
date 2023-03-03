import sys
from collections import defaultdict
delimeter = "`"
def parse_file(input_file):
    file_dictionary = {}
    lines = input_file.readlines()
    for line in lines:
        if line[0]=="#":
            continue
        else:
            tokens = line.split()
            if len(tokens) == 1:
                file_dictionary[tokens[0]] = "blank"
            elif len(tokens) == 2:
                file_dictionary[tokens[0]] = tokens[1]

    return file_dictionary

def merge_configurations(file_dictionaries):
    with open("total_config.csv","w") as output_file:
        first_line = ["Parameter name"]
        all_key_dictionary = {}
        for file_name, a_dictionary in file_dictionaries:
            first_line.append(file_name)
            print(first_line)
            all_key_dictionary = {**all_key_dictionary,**a_dictionary}
        output_file.write(delimeter.join(first_line)+"\n")
        key_list = list(all_key_dictionary.keys())
        print(key_list)
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
def main():
    file_dictionaries = []
    for file_name in sys.argv[1:]:
        with open(file_name) as input_file:
            file_dictionaries.append((file_name,parse_file(input_file)))
    merge_configurations(file_dictionaries)

if __name__ == "__main__":
    main()
                
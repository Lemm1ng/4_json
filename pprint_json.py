import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as input_file:
        return json.load(input_file)


def pretty_print_json(input_json_data):
    print(json.dumps(input_json_data, indent=4))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Error. The pathway to the input file is not specified.')
    elif len(sys.argv) == 2:
        filepath = sys.argv[1]
        input_json_data = load_data(filepath)
        pretty_print_json(input_json_data)
    else:
        print('Error. More than one argument is specified.')

import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    filepath = input()
    data = load_data(filepath)
    pretty_print_json(data)

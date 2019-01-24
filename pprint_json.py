import json, sys


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.read()
    return json.loads(data)


def pretty_print_json(data):
    return json.dumps(data, indent=4)


if __name__ == '__main__':
    file_path = sys.argv[1]
    pretty = pretty_print_json(
         load_data(file_path)
    )
    print(pretty)

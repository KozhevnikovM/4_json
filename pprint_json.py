import json, sys


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        file_content = f.read()
    return json.loads(file_content)


def pretty_print_json(python_dict):
    return json.dumps(python_dict, indent=4)


if __name__ == '__main__':
    file_path = sys.argv[1]
    pretty = pretty_print_json(
         load_data(file_path)
    )
    print(pretty)

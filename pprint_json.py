import json, sys, os


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        file_content = f.read()
    try:
        return json.loads(file_content)
    except:
        return 'Invalid Json'


def pretty_print_json(data_to_json):
    return json.dumps(data_to_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if sys.argv[1] and os.path.isfile(sys.argv[1]):
        file_path = sys.argv[1]
    else:
        exit('File path not specified or file not exist. Look at README.md for more details')

    pretty = pretty_print_json(
         load_data(file_path)
    )
    print(pretty)

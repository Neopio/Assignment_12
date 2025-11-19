import json
from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of its lines without trailing newlines."""
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip("\n") for line in f]


def train_file_list_to_json(english_list: List[str], german_list: List[str]) -> List[str]:
    """Pairs English and German lines into valid JSON strings."""

    result = []
    for en, de in zip(english_list, german_list):
        obj = {"English": en, "German": de}
        json_line = json.dumps(obj, ensure_ascii=False)
        result.append(json_line)

    return result


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes JSON lines into the output file."""
    with open(path, 'w', encoding='utf-8') as f:
        for line in file_list:
            f.write(line + "\n")


if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    english_lines = path_to_file_list(english_path)
    german_lines = path_to_file_list(german_path)

    processed = train_file_list_to_json(english_lines, german_lines)
    write_file_list(processed, output_path)

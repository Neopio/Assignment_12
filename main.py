from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # Fix 1: 'w' (write) mode deletes content. Changed to 'r' (read).
    # Fix 2: Use 'with open' for safety and readlines() to actually get content.
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Strip newline characters for cleaner processing
    return [line.strip() for line in lines]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    
    def process_file(file):
        # Fix 3: Correct logic for checking characters
        if '\\' in file:
            file = file.replace('\\', '\\\\')
        if '/' in file or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Fix 4: Correct JSON template structure to match {"English":"...", "German":"..."}
    template_start = '{"English":"'
    template_mid = '","German":"'
    template_end = '"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) # Fix 5: Process the German file, don't overwrite english_file

        # Fix 6: Correct concatenation order
        json_string = template_start + english_file + template_mid + german_file + template_end
        processed_file_list.append(json_string)
        
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    # Fix 7: Changed 'r' to 'w' to write file.
    with open(path, 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(file + '\n') # Fix 8: Write the actual content, not just newlines
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    # Fix 9: Correct logic flow in main block
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path) # Read german file first

    # Process both lists
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    # Write result
    write_file_list(processed_file_list, path+'concated.json')
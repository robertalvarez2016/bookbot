def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return len(file_contents.split())

def get_num_characters(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    ans = {}
    for char in file_contents:
        if char.isalpha():
            ans[char] = ans.get(char, 0) + 1
    return ans

def sort_characters(characters):
    return sorted(characters.items(), key=lambda x: x[1], reverse=True)
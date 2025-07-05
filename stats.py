def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return len(file_contents.split())

def character_counter(path):
    with open(path) as f:
        file_contents = f.read()
    
    final = {}
    for char in file_contents:
        if char.lower() in final:
            final[char.lower()] += 1
        else:
            final[char.lower()] = 1
    
    return final

def sort_on(items):
    return items["num"]

def sorter(values):
    result = []
    for key, value in values.items():
        if key.isalpha():
            temp = {"char":key.lower(), "num":value}
            result.append(temp)
    result.sort(reverse=True, key=sort_on)
    return result
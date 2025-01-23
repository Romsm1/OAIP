def brackets(line):
    storage = []
    brackets_value = {")": "(", "]": "[", "}": "{", ">": "<"}
    open_brackets = set(brackets_value.values())
    close_brackets = set(brackets_value.keys())

    for char in line:
        if char in open_brackets:
            storage.append(char)
        elif char in close_brackets:
            if not storage or brackets_value[char] != storage.pop():
                return False
    return not storage
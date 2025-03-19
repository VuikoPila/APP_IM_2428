import re

def contains_all_letters_iterative(s: str) -> bool:
    required_letters = set("while")
    for char in s:
        required_letters.discard(char)
        if not required_letters:
            return True
    return False

def replace_while_iterative(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        if s[i:i+5] == "while":
            result.append("**")
            i += 5
        else:
            result.append(s[i])
            i += 1
    return "".join(result)

if __name__ == "__main__":
    test_string = "this is a while loop while working"
    print("Contains all letters (iterative):", contains_all_letters_iterative(test_string))
    print("Replace 'while' (iterative):", replace_while_iterative(test_string))

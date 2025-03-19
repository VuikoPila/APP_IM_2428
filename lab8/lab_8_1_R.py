import re

def contains_all_letters_recursive(s: str, required_letters=None) -> bool:
    if required_letters is None:
        required_letters = set("while")
    if not required_letters:
        return True
    if not s:
        return False
    return contains_all_letters_recursive(s[1:], required_letters - {s[0]})

def replace_while_recursive(s: str) -> str:
    if not s:
        return ""
    if s.startswith("while"):
        return "**" + replace_while_recursive(s[5:])
    return s[0] + replace_while_recursive(s[1:])

if __name__ == "__main__":
    test_string = "this is a while loop while working"
    print("Contains all letters (recursive):", contains_all_letters_recursive(test_string))
    print("Replace 'while' (recursive):", replace_while_recursive(test_string))

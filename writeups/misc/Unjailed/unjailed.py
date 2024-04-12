#!/usr/bin/env python3

import re
from sys import modules, version

restriction = "import|chr|os|sys|system|builtin|exec|eval|subprocess|pty|popen|read|get_data|cat|ls|bin"
searching = lambda word: re.compile(r"\b({0})\b".format(word), flags=re.IGNORECASE).search

modules.clear()
del modules

def main():
    print(f"{version}\n")
    print("Can you beat me?")
    while True:
        message = input('>>> ').lower()
        finded = searching(restriction)(''.join(message.split("__")))
        if finded:
            print(f"Ha-ha! I banned {finded.group(0)}!")
            break
        if re.match("^(_?[A-Za-z0-9])*[A-Za-z](_?[A-Za-z0-9])*$", message):
            print("Nah, thats not the way)")
            break
        else:
            exec(message, {'globals': globals(), '__builtins__': {}}, {'print':print})

if __name__ == "__main__":
    main()

#! /usr/bin/python3
#-*- coding:utf-8 -*-
def main():
    print("========================================================================")
    #print(open(__file__).read())
    print("You shall not pass!")
    print("========================================================================")
    while True:
        text = input('>>> ')
        for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write']:
            if keyword in text:
                print("U are hacker! Go Away!")
                break;
        else:
            exec(text)
if __name__ == "__main__":
    main()

#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4.pyc

    file_name = "hidden_4.pyc"

    with open(file_name, 'r') as file:
        for line in file:
            if line[:2] != "__"
                print(line)

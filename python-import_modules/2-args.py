#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys

    total_args = len(sys.argv)
    arg_num = 1

    if total_args == 0:
        print("0 arguments.")
    elif total_args == 1:
        print("1 argument:")
        print(sys.argv[1])
    else:
        print(f"{total_args - 1} arguments:")
        for i in range(total_args):
            if i > 0:
                print("{}: {}".format(arg_num, sys.argv[i]))
                arg_num = arg_num + 1

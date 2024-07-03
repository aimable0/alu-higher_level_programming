#!/usr/bin/python3
if __name__ == "__main__":  # condition for: only runs as main not when imported
    import sys

    tot_num = len(sys.argv)
    sum = 0

    if tot_num == 1:  # for one argument which is the script_name
        sum = 0
    elif tot_num == 2:  # for two argument meaning a number and the script_name
        num = f"{sys.argv[1]}"
        sum = int(num)  # we just return the number
    else:
        for i in range(tot_num):  # for more than 2 arguments
            if i > 0:
                str_num = f"{sys.argv[i]}" # collect the number on each iteration
                int_num = int(str_num)  # cast the number from string to int format
                sum = sum + int_num  # add it to the sum on each iteration
    print(sum)

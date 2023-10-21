import pandas as pd
import numpy as np


def is_crossing(square):
    a11 = square[0][0]
    a22 = square[1][1]

    a12 = square[0][1]
    a21 = square[1][0]

    # check if a11 and a22 difference is only 1
    if abs(a11 - a22) == 1:
        # check if a12 and a21 difference is only 1
        if abs(a12 - a21) == 1:
            return True


def do_challenge_1(lines):
    dim = lines[0]

    # transform them into a df
    # transform them into a numpy array
    # create a empty numpy array of dim x dim


    paths = int(lines[int(dim)+1])
    num_to_add = 1

    for i in range(paths):
        is_invalid = False
        array_1 = np.zeros((int(dim), int(dim)))
        koord = lines[int(dim)+2+i]
        koord_list = koord.split(' ')
        for koord_in_list in koord_list:
            x = int(koord_in_list.split(',')[0])
            y = int(koord_in_list.split(',')[1])

            if array_1[y][x] != 0:
                is_invalid = True
                break
            array_1[y][x] = num_to_add
            num_to_add += 1

        for i2 in range(int(dim)-1):
            for j2 in range(int(dim)-1):
                square = array_1[i2:i2+2, j2:j2+2]
                if is_crossing(square):
                    is_invalid = True

        with open('challenge_1.out', 'a') as f:
            if is_invalid:
                f.write('INVALID' + '\n')
            else:
                f.write('VALID' + '\n')


if __name__ == '__main__':
    # read in texxt file challenge_1.in
    with open('challenge_1_test.in') as f:
        lines = f.readlines()

    # replace \n in lines
    lines = [line.replace('\n', '') for line in lines]

    do_challenge_1(lines)
    print(lines)

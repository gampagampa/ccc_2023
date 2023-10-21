import pandas as pd
import numpy as np
import tqdm


def get_all_paths(arr, start_x, start_y, end_x, end_y):
    current_positon = [start_x, start_y]

    # swap around end_x and end_y

    val = 2
    arr[current_positon[0]][current_positon[1]] = val
    met_endpoint = False
    while not met_endpoint:
        # get kooridnates where value is val
        kooridnates = np.where(arr == val)
        # get all surrounding koordinates and assign them val +1
        for i in range(len(kooridnates[0])):
            x = kooridnates[0][i]
            y = kooridnates[1][i]

            # check if x+1 is valid
            if x+1 < len(arr):
                if arr[x+1][y] == 0:
                    arr[x+1][y] = val + 1
                    if x+1 == end_x and y == end_y:
                        met_endpoint = True

            # check if x-1 is valid
            if x-1 >= 0:
                if arr[x-1][y] == 0:
                    arr[x-1][y] = val + 1
                    if x-1 == end_x and y == end_y:
                        met_endpoint = True

            # check if y+1 is valid
            if y+1 < len(arr):
                if arr[x][y+1] == 0:
                    arr[x][y+1] = val + 1
                    if x == end_x and y+1 == end_y:
                        met_endpoint = True

            # check if y-1 is valid
            if y-1 >= 0:
                if arr[x][y-1] == 0:
                    arr[x][y-1] = val + 1
                    if x == end_x and y-1 == end_y:
                        met_endpoint = True


            # check diagonal cases
            # check if x+1 and y+1 is valid
            if x+1 < len(arr) and y+1 < len(arr):
                if arr[x+1][y+1] == 0:
                    arr[x+1][y+1] = val + 1
                    if x+1 == end_x and y+1 == end_y:
                        met_endpoint = True

            # check if x-1 and y-1 is valid
            if x-1 >= 0 and y-1 >= 0:
                if arr[x-1][y-1] == 0:
                    arr[x-1][y-1] = val + 1
                    if x-1 == end_x and y-1 == end_y:
                        met_endpoint = True

            # check if x+1 and y-1 is valid
            if x+1 < len(arr) and y-1 >= 0:
                if arr[x+1][y-1] == 0:
                    arr[x+1][y-1] = val + 1
                    if x+1 == end_x and y-1 == end_y:
                        met_endpoint = True

            # check if x-1 and y+1 is valid
            if x-1 >= 0 and y+1 < len(arr):
                if arr[x-1][y+1] == 0:
                    arr[x-1][y+1] = val + 1
                    if x-1 == end_x and y+1 == end_y:
                        met_endpoint = True

        val += 1
    return arr


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

    arr = np.zeros((int(dim), int(dim)))

    lines_df = pd.DataFrame(lines[1:int(dim)+1])

    for i in range(int(dim)):
        for j in range(int(dim)):
            arr[j][i] = 0 if lines_df.iloc[i][0][j] == 'W' else 1

    paths = int(lines[int(dim)+1])

    for i in range(paths):
        print(f'Doing path: ',  i)
        starting_coords = lines[int(dim)+2+i].split(' ')[0]
        start_x = int(starting_coords.split(',')[0])
        start_y = int(starting_coords.split(',')[1])

        end_coords = lines[int(dim)+2+i].split(' ')[-1]
        end_x = int(end_coords.split(',')[0])
        end_y = int(end_coords.split(',')[1])

        arr_ = arr.copy()
        path = get_all_paths(arr_, start_x, start_y, end_x, end_y)

        current_value = path[end_x][end_y]
        coordinates_list = [[end_x, end_y]]
        current_x, current_y = end_x, end_y
        while current_value != 2:
            # get all koords with value current_value - 1
                if current_x+1 < len(path):
                    if path[current_x+1][current_y] == current_value - 1:
                        coordinates_list.append([current_x+1, current_y])
                        current_x += 1
                        current_value -= 1
                        continue
                if current_y+1 < len(path) and current_x+1 < len(path):
                    if path[current_x+1][current_y+1] == current_value - 1:
                        coordinates_list.append([current_x+1, current_y+1])
                        current_x += 1
                        current_y += 1
                        current_value -= 1
                        continue
                if current_y-1 >= 0 and current_x+1 < len(path):
                    if path[current_x+1][current_y-1] == current_value - 1:
                        coordinates_list.append([current_x+1, current_y-1])
                        current_x += 1
                        current_y -= 1
                        current_value -= 1
                        continue
                if current_x-1 >= 0:
                    if path[current_x-1][current_y] == current_value - 1:
                        coordinates_list.append([current_x-1, current_y])
                        current_x -= 1
                        current_value -= 1
                        continue
                if current_x-1 >= 0 and current_y-1 >= 0:
                    if path[current_x-1][current_y-1] == current_value - 1:
                        coordinates_list.append([current_x-1, current_y-1])
                        current_x -= 1
                        current_y -= 1
                        current_value -= 1
                        continue
                if current_x-1 >= 0 and current_y+1 < len(path):
                    if path[current_x-1][current_y+1] == current_value - 1:
                        coordinates_list.append([current_x-1, current_y+1])
                        current_x -= 1
                        current_y += 1
                        current_value -= 1
                        continue
                if current_y+1 < len(path):
                    if path[current_x][current_y+1] == current_value - 1:
                        coordinates_list.append([current_x, current_y+1])
                        current_y += 1
                        current_value -= 1
                        continue
                if current_y-1 >= 0:
                    if path[current_x][current_y-1] == current_value - 1:
                        coordinates_list.append([current_x, current_y-1])
                        current_y -= 1
                        current_value -= 1
                        continue

        # write coordinates list into a text file
        with open('challenge_1.out', 'a') as f:
            for coordinate in coordinates_list[::-1]:
                f.write(str(coordinate[0]) + ',' + str(coordinate[1]) + ' ')
            f.write('\n')


if __name__ == '__main__':
    # read in texxt file challenge_1.in
    with open('challenge_1_test.in') as f:
        lines = f.readlines()

    # replace \n in lines
    lines = [line.replace('\n', '') for line in lines]

    do_challenge_1(lines)
    print(lines)

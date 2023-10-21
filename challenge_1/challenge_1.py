import pandas as pd


def get_island_map(lines):
    dim = lines[0]

    # transform them into a df
    df = pd.DataFrame(lines[1:int(dim)+1])
    # number of koods = lines[int(dim)+1]
    num_koords = lines[int(dim)+1]

    i = 0
    while i < int(num_koords):
        koord = lines[int(dim)+2+i]
        x = int(koord.split(',')[0])
        y = int(koord.split(',')[1])

        # get x row of df
        x_row = df.iloc[y][0]
        # get y entry of x_row
        y_entry = x_row[x]
        # write y into a text file
        with open('challenge_1.out', 'a') as f:
            f.write(str(y_entry) + '\n')

        i += 1

def do_challenge_1(lines):
    dim = lines[0]

    # transform them into a df
    df = pd.DataFrame(lines[1:int(dim)+1])
    # number of koods = lines[int(dim)+1]
    num_koords = lines[int(dim)+1]

    i = 0
    while i < int(num_koords):
        koord = lines[int(dim)+2+i]
        x = int(koord.split(',')[0])
        y = int(koord.split(',')[1])

        # get x row of df
        x_row = df.iloc[y][0]
        # get y entry of x_row
        y_entry = x_row[x]
        # write y into a text file
        with open('challenge_1.out', 'a') as f:
            f.write(str(y_entry) + '\n')

        i += 1


if __name__ == '__main__':
    # read in texxt file challenge_1.in
    with open('challenge_1.in') as f:
        lines = f.readlines()

    # replace \n in lines
    lines = [line.replace('\n', '') for line in lines]

    #df = pd.read_csv("challenge_1.in", sep=" ", header=None)
    do_challenge_1(lines)
    print(lines)

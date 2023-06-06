import os
import sys


def remove_last_occurrence(string: str, char: str):
    length = len(string)
    string2 = ''
    for i in range(length):
        if string[i] == char:
            string2 = string[0:i] + string[i + 1:length]
    return string2


def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_EXT"]

    paths = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(f'{extension}'):
                paths = paths + '\"' + root + '/' + str(file) + '\", '

    paths = remove_last_occurrence(paths, ',')
    paths = "[" + paths + "]"
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print(f'paths={paths}\n', file=f)
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()

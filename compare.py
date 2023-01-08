from argparse import ArgumentParser


def check_symbols(a, b):
    if a != b:
        return 1
    return 0


def levenshtein(first_file, second_file):
    if len(first_file) > len(second_file):
        first_file, second_file = second_file, first_file
    first_len = len(first_file)
    second_len = len(second_file)
    cur_row = range(first_len + 1)
    for i in range(1, second_len + 1):
        prev_row, cur_row = cur_row, [i] + [0] * first_len
        for j in range(1, first_len + 1):
            cur_row[j] = min(prev_row[j] + 1, cur_row[j - 1] + 1,
                             prev_row[j - 1] + check_symbols(first_file[j - 1], second_file[i - 1]))
    return cur_row[first_len] / second_len


parser = ArgumentParser(description='LevenshteinDistance')
parser.add_argument('infile_path', type=str, help='Input file with paths')
parser.add_argument('outfile_path', type=str, help='Output file for scores')
args = parser.parse_args()
infile_path = args.infile_path
outfile_path = args.outfile_path

filepaths = []
output_file = open(outfile_path, "w")
with open(infile_path, "r") as infile:
    for line in infile.readlines():
        filepaths.append(line.split())

for el in filepaths:
    with open(el[0], "r") as file:
        first_file_code = file.read()
    with open(el[1], "r") as file:
        second_file_code = file.read()
    output_file.write(str(levenshtein(first_file_code, second_file_code)) + '\n')

output_file.close()

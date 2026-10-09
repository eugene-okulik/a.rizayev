import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('filepath', help='full path to file')
parser.add_argument('texttofind', help='text to find in the file')
parser.add_argument('-a', '--allerrors',
                    help='print all if true, print first otherwise', action='store_true')

args = parser.parse_args()

for i_file in sorted(os.listdir(args.filepath)):
    is_found = False
    print(f'В составе файла: {i_file}')
    with open(os.path.join(args.filepath, i_file) , 'r') as file:
        for line_index, line in enumerate(file, start=1):
            if args.texttofind in line:
                line_arr = line.split()
                word_index = line_arr.index(args.texttofind)
                init_index = word_index - 5 if word_index >= 5 else 0
                end_index = word_index + 6 if word_index <= len(line_arr) - 5 else len(line_arr)
                result_string = ' '.join(line_arr[init_index:end_index])
                print(f'Строка {line_index}, время: [{' '.join(line_arr[:2])}]: ' + result_string)
                if not args.allerrors:
                    is_found = True
                    break

    if is_found:
        break
    print()

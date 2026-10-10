import argparse
import os
from datetime import datetime


def is_block_start(_line):
    try:
        datetime.strptime(_line[:23], '%Y-%m-%d %H:%M:%S.%f')
        return True
    except ValueError:
        return False


def block_search_and_get_result(__text, block):
    if __text in block:
        line_arr = block.split()
        word_index = line_arr.index(__text)
        init_index = word_index - 5 if word_index >= 5 else 0
        end_index = word_index + 6 if word_index <= len(line_arr) - 5 else len(line_arr)
        result_string = ' '.join(line_arr[init_index:end_index])
        return result_string
    else:
        return None


parser = argparse.ArgumentParser()

parser.add_argument('filepath', help='full path to file')
parser.add_argument('--text', help='text to find in the file')
parser.add_argument('-a', '--allerrors',
                    help='print all if true, print first otherwise', action='store_true')

args = parser.parse_args()

def print_lines(file_path, _text):
    blocks = {}
    current_time = None
    is_inner_found = False
    file_printed = False
    found_in_block = False
    with open(file_path, 'r') as _file:
        for line_index, line in enumerate(_file, start=1):
            if is_block_start(line):
                if not found_in_block:
                    blocks.pop(current_time, None)
                current_time = line[:23]
                blocks[current_time] = line[24:]
                found_in_block = False
            elif current_time is not None:
                blocks[current_time] += line
            if _text in line:
                found_in_block = True
                result = block_search_and_get_result(_text, blocks[current_time])
                if not file_printed:
                    print(f'\nВ составе файла: {os.path.basename(file_path)}')
                    file_printed = True
                print(f'Строка {line_index}, время [{current_time}]: {result}')

                if not args.allerrors:
                    is_inner_found = True
                    return is_inner_found

    return is_inner_found


if os.path.isdir(args.filepath):
    is_found = False
    for file in sorted(os.listdir(args.filepath)):
        is_found = print_lines(os.path.join(args.filepath,file), args.text)
        if is_found:
            break
elif os.path.isfile(args.filepath):
    print_lines(args.filepath, args.text)


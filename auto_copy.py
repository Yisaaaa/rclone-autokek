import argparse
import os
import subprocess
import sys


#parser object
parser = argparse.ArgumentParser(description="rclone copy from a text file")

parser.add_argument('Source', help='source path to copy from')
parser.add_argument('Destination', help='path to copy to')
parser.add_argument('Txt', help='path to txt file')

ARGS = parser.parse_args()

source, dest, txt_path = ARGS.Source, ARGS.Destination, ARGS.Txt



if not all([os.path.isdir(path) for path in [source, dest]]):
    not_path = source if not os.path.isdir(source) else dest
    print(not_path + ' is not found')

try:
    with open(txt_path) as fp:
        files = fp.readlines()
except FileNotFoundError:
    print(txt_path + ' does not exists')
    sys.exit()
except IsADirectoryError:
    print(txt_path + ' is a directory')
    sys.exit()

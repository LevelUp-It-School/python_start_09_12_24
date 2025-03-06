import argparse
import os

parser = argparse.ArgumentParser(description='Read file and display its content.')
parser.add_argument('filepath', help="Path to the file.")
args = parser.parse_args()

if not os.path.exists(args.filepath):
    parser.error(f'The file {args.filepath} does not exist.')
with open(args.filepath, 'r') as file:
    contents = file.read()
    print(contents)
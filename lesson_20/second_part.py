import argparse

parser = argparse.ArgumentParser(description='Process multiple files.')
parser.add_argument('filenames', nargs='+', help = "List of files to process.")
args = parser.parse_args()
for filename in args.filenames:
    print(f"Processing file: {filename}")
    #Add your fule processing code

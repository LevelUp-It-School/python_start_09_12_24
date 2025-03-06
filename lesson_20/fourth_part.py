import argparse

parser = argparse.ArgumentParser(description='A script with debug mode.')
parser.add_argument('--debug', action='store_true', help="Enable debug output.")
args = parser.parse_args()
if args.debug:
    print('Debug mode is enabled')
    # Additional debug information here.
else:
    print("Debug mode is disabled.")

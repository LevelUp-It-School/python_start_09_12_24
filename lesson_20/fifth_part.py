import argparse

parser = argparse.ArgumentParser(description='Adjust program settings.')
parser.add_argument('--timeout', type=int, default=30, help='Timeout in seconds.')
args = parser.parse_args()
print(f"Timeout is set to {args.timeout} seconds")

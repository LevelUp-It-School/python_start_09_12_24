import argparse
import sys

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"Error: {message}")
        self.print_help()
        sys.exit(2)

parser = CustomArgumentParser(description="Divide two numbers")
parser.add_argument('numerator', type=float, help='The numerator')
parser.add_argument('denominator', type=float, help='The denominator')
args = parser.parse_args()
if args.denominator == 0:
    parser.error("Denominator cannot be zero")
result = args.numerator / args.denominator
print(f'Result: {result}')
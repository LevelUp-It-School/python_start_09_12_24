import argparse

parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('num1', type=int, help="The first number to add.")
parser.add_argument('num2', type=int, help="The second number to add.")

parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity.')
args = parser.parse_args()

result = args.num1 + args.num2
print('The sum of {} and {} is {}'.format(args.num1, args.num2, result))
if args.verbose:
    print("Verbose mode is enabled.")
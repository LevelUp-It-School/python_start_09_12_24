import argparse

parser = argparse.ArgumentParser(
    description='Convert temperatures between Celsius and Fahrenheit',
    epilog='Enjoy using the tempereture converter!',
    usage = "%(prog)s [options] temperature")
parser.add_argument('temperature', type=float, help='Temperature value to convert')
parser.add_argument('--to-fahrenheit', action='store_true', help='Convert Celsius value to Fahrenheit')
parser.add_argument("--to-celsius", action='store_true', help='Convert Fahrenheit value to Celsius')

args = parser.parse_args()

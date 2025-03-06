import argparse

parser = argparse.ArgumentParser(description='Send a message.')
parser.add_argument('--recipient', required=True, help='Recipient of the message.')
args = parser.parse_args()
print(f"Sending message to {args.recipient}.")
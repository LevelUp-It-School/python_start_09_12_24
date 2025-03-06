import argparse

parser = argparse.ArgumentParser(description='Perform actions in different modes.')
parser.add_argument('--mode', choices=['backup', 'restore', 'delete'], required=True, help='Mode of opration.')
args = parser.parse_args()
if args.mode == 'backup':
    print('Backing up data...')
    #Backup code here
elif args.mode == 'restore':
    print('Restoring data...')
    #Restore code here
elif args.mode == 'delete':
    print("Deleting data...")
    #Delete code here


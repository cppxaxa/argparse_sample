import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--strings', dest='strings', metavar='N', nargs='+', help='string')

args = parser.parse_args()
print(args.strings)

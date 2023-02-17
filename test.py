import argparse as agp
print('argparser:',agp)
print('version:',agp.__version__)
parser = agp.ArgumentParser(description='Description of your program')#desc opt
print(parser)
parser = agp.ArgumentParser(description='A simple program to add two numbers')
parser.add_argument('num1', type=int, help='The first number')
parser.add_argument('num2', type=int, help='The second number')
parser.add_argument('--verbose', help='increase output verbosity', action='store_true')
args = parser.parse_args()

if args.verbose:
    print('Verbose mode enabled')
#args = parser.parse_args()

result = args.num1 + args.num2
print(f"The sum of {args.num1} and {args.num2} is {result}")
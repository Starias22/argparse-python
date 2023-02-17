import argparse as ap
parser=ap.ArgumentParser()
#parser.parse_args()#add help option

#add echo arg to the argument parser
parser.add_argument('message',help='the message to print')
#args=parser.parse_args()#


parser.add_argument('mess3',help='the message to print 3 time',type=str)
parser.add_argument('int',help='the times of 8 to print',type=int)
#optional argument that require an value(string)
parser.add_argument("--verbosity", help="increase output verbosity")

#optional argument that require an value(float)
parser.add_argument("--tail", help="print the tail of the user",type=float)


#optional argument that mustn't take any value
#store True if specified
#action can also be 'store_false'
parser.add_argument("--novalue", help="print the tail of the user",action='store_true')

#short options
#just one dash:the shortcomd
#store false if specified
#work with -p,{1,}--ph,--phe,...,--phello,
parser.add_argument('-p','--phello',help='print hello world',
                    action='store_false')
#an optional argument with short alternative and choices
#it requires an argument in [1,2,3]
parser.add_argument('-c','--choice',help='print the choice of the user',
                    choices=(1,2,3),type=int)#or [1,2,3]

parser.add_argument('-t','--count',help='print how many times count is specified',
                    action='count',default=5)
# the default value is added to the number of -t specified



args=parser.parse_args()
print('You enter "'+args.message+'"','as first arg')# print the arg

#now the programm require 2 args
print(3*args.mess3)
print(args.int*"8")
#if the user apply the verbosity option
if args.verbosity:
    print('verbosity option is used', 'and it\' s value is',args.verbosity)
else:
    print('verbosity option us not used')

if args.tail:
    print('Your tail is',args.tail)


#will print true if --novalue opt arg is used and false otherwise
print('--novalue specified? ',args.novalue)

# if not specified
if  args.phello:
    print("Hello world:short not specified command")
else:
    print('Specified')

#none if not specified
if args.choice==1:
    print('You choose 1')
else:
    print('choice:',args.choice)

if args.count:
    print('count is specified',args.count,'times')


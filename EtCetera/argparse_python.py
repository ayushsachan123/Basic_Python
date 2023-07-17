import argparse
# we are giving the default value 1 if there is no argument pass through cli
parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default= 1, help="number of times to meow", type=int) # Now configure argument parser to know about the specific cli that i want to support in my program
args = parser.parse_args() # it automatically looks sys.argv for me i don't need to import sys myself

for _ in range(args.n):
    print("meow")
import sys
from creating_own_module import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
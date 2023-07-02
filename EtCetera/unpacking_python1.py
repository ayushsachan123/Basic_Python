# *args means take variable number of argument
# **kwars means some number of keyword or named argument
def f(*args, **kwargs):
    # print("Positional:",args)
    print("Named: ",kwargs)

# passing variable argument
# f(100,50,25)
# passing named argument
f(galleons=100,sickles=50,knuts=25)

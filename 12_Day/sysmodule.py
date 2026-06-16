#Sys module
#Manipulate different parts of the Python runtime environment. 
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# To know the largest integer variable it takes
print(sys.maxsize)
# To know environment path
print(sys.path)
# To know the version of python you are using
print(sys.version)
# to exit sys
# stops the program immediately
sys.exit()
import os

# Returns 'posix' if is Unix, else 'nt' for Windows, else 'java'
os.name

"""
Works in Unix only; Returns information identifying the current operating system. The return value is an object with five attributes:

sysname - operating system name

nodename - name of machine on network (implementation-defined)

release - operating system release

version - operating system version
machine - hardware identifier
"""
os.uname()

# A dictionary of all environment variables
os.environ

# if you want to modify environment variables, edit the os.environ dictionary.
os.environ['variable'] = 'value'

# function that gets an environment variable; it not exist, returns None
homedirectory = os.getenv('HOME')

# to make a environment variable but not change the os.environ dictionary:
os.putenv('variable','value')

# returns current running directory
os.getcwd()

# changes current working directory
os.chdir(homedirectory + '/Desktop')

# make a single folder
os.mkdir('folder1')

# make multiple folders
os.makedirs('folder1/folder2')

# returns a normalized absolutized version of the pathname path
# this will return something similar to '/Users/danz/Desktop/folder1'
os.path.abspath('././folder1')

# returns the size, in bytes, of a path
# this will return 96.
os.path.getsize('././folder1')
# make file
open('file.txt', 'w').close()

# open a file with its default application. works fir windows only.
# os.startfile('file.txt')

# rename (or move) a file
os.rename('file.txt','folder1/file.txt')

# rename file recursively
os.renames('folder1/file.txt',('folder1/folder2/file.txt'))

# delete file
os.remove('folder1/folder2/file.txt')

# delete folder. only works for a folder that is empty.
os.rmdir('folder1/folder2')
os.rmdir('folder1')

# os.walk can scan for directories, subdirectories and files inside a directory.
def scandir(dir):
  for root, dirs, files in os.walk(dir):
    # root is the directory found in dir
    # dirs is a list of the directories found inside root
    # files is a list of the files found inside root
    print(root,dirs,files)

scandir('.')

# returns the name of a file or directory
# os.path.basename('./folder1/folder2/main.py') # returns 'main.py'
# os.path.basename('./folder1/folder2') # returns 'folder2'

# returns the directory of a file or directory
# os.path.dirname('./folder1/folder2/main.py') # returns './folder1/folder2'
# os.path.dirname('./folder1/folder2') # returns './folder1'


# checks if file or directory exists
os.path.exists('folder1')

# check if exists and is file
os.path.isfile('folder1')

# check if exists and is folder
os.path.isdir('folder1')

# join paths together and adds additional slashes or backslashes as necessary
# this will return './folder1/folder2/./example.txt'
os.path.join('./folder1','folder2/','./example.txt')


# split a path into directory and name
# this will return ('./folder1/folder2/.', 'example.txt')
os.path.split('./folder1/folder2/./example.txt')



# tuple of terminal size (columns, lines)
os.terminal_size



# execute command
os.system('ls -a')


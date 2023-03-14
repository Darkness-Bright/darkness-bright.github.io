import sys

"""
File objects used by the interpreter for standard input, output and errors:

stdin is used for all interactive input (including calls to input());

stdout is used for the output of print() and expression statements and for the prompts of input();

The interpreter’s own prompts and its error messages go to stderr.

These streams are regular text files like those returned by the open() function.

"""

sys.stdin
sys.stdout
sys.stderr

# Note: sys.stdin.read() could be useful. See https://replit.com/@markzhere/POISON

sys.stdout.write('Hi')
sys.stdout.flush()

# sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the absolute path of the script. The rest of the arguments are stored at the subsequent indices.
try:
  print('First argument passed while executing this script is '+sys.argv[1])
except:
  pass


sys.exit
# exits the porgram

sys.version
# python version

print(sys.builtin_module_names)
# A tuple of strings containing the names of all modules that are compiled into this Python interpreter









# sys.platform can tell you what OS the script is running on
is_mac = sys.platform.startswith('darwin')
is_linux = sys.platform.startswith('linux')
is_windows = sys.platform.startswith('win')



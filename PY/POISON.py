import termios, fcntl, sys, os, time


def c():
  try:
    c = sys.stdin.read(1)
    if c:
      print(c)
  except: pass

def poison():
  global fd,oldterm,oldflags
  fd = sys.stdin.fileno()
  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)
  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

def antidote():
  termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def clearin():
  termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def log(message, wait=0.03, delay=0.4, newline=True):
  # For each character in the message
  for i in message:
    # Write the character
    sys.stdout.write(i)
    # Make the character show in console
    sys.stdout.flush()
    # Pause delays
    time.sleep(delay if i == "\n" else wait)
    time.sleep(wait*4-wait**2 if i == "," else 0)
    time.sleep(wait*5-wait**2 if i == "." else 0)
  # Reset ANSI style, and add \n if newline
  sys.stdout.write("\001\033[0m\002\n" if newline else "\001\033[0m\002")

poison()


t_end = time.monotonic() + 10
while time.monotonic() < t_end:
  c()


clearin()
antidote()
'''syntax:
def function(arg,*args.**kwargs):
  # do somethings with the arguments, and return a value if needed
'''

# 1. simple function
def add(number1, number2):
  return number1+number2

assert add(2,3) == 5

# 2. predifined arguments go at the back
def add(number1, number2=3):
  return number1+number2

assert add(2) == 5

# 3. single star (*args)
def add(*numbers):
  return sum(numbers)

assert add(1,2,3) == 6

# 4. double star (**kwargs)
def add(*numbers,**bonuses):
  bonus = 0
  for i in bonuses:
    bonus += bonuses[i]
  return sum(numbers) + bonus

assert add(1,2,3,stylebonus=2,accuracybonus=3,additionalpoints=1) == 12

# 5. using arg, *args and **kwargs together
def add(number1,number2,*othernumbers,**bonuses):
  bonus = 0
  for i in bonuses:
    bonus += bonuses[i]
  return number1 + number2 + sum(othernumbers) + bonus

assert add(2,3,1,1,1,stylebonus=5,additionalpoints=5) == 18

# 6. unlike arg, *args and **kwargs cannot be predifined
# unlike arg, if *args or **kwargs is specified, they are not required.
def add(number1=2,number2=3,*othernumbers,**bonuses):
  bonus = 0
  for i in bonuses:
    bonus += bonuses[i]
  return number1 + number2 + sum(othernumbers) + bonus

assert add() == 5

# for a function that takes many arguments, recommended to use the following syntax.
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                 - Keyword only
#          -- Positional only

def calculation(original,scale,/,toadd,*,printout=False):
  '''In this function, no *args or **kwargs were used.
    could be set via position: original, scale, toadd
    could be set via keyword: toadd, printout
  '''
  if printout:
    print('Calculating...')
  return original*scale+toadd

assert calculation(10,1,toadd=2) == 12
assert calculation(10,1,2,printout=True) == 12
'''
these following calls to the funstion will result in errors:

calculation(original=10,scale=1,toadd=2)
# positional=only arguments cannot be assigned with keywords

calculation(10,1,2,True)
# the printout argument could only be set via keyword.
'''

# Here is another example function for reference.

def calculate_exam_score(math,grammar,science,/,penalties,*answers,**bonuses):
  bonus = 0
  for i in bonuses:
    bonus += bonuses[i]
  return math*2 + grammar*2 + science*3 + bonus + len(''.join(answers)) - penalties


score = calculate_exam_score(20,16,18,5,'B','C','B','A',additionalpoints=3)
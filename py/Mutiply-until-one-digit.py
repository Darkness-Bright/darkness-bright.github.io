def main_function(input):
  a = 1
  for i in range(len(str(input))):
    a = a * int(str(input)[i-1])
  if len(str(a)) == 1:
    return a
  else:
    return main_function(a)
for i in range(1000):
  print(main_function(i),end="") if not main_function(i) == 0 else print("-",end="")
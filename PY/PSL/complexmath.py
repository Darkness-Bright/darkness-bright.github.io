import cmath

# Constants
pi = cmath.pi
e = cmath.e
tau = cmath.tau

# A complex number with real and imaginary parts
number = complex(33.1,13.3)

# Polar and rectangular coordinates of a complex number
polar = cmath.polar(number)
rect = cmath.rect(polar[0],polar[1])

# Square root of complex number
sqrt = cmath.sqrt(number)

# e to the x
# ex will be equal to e^3
ex = cmath.exp(3)



acos = cmath.acos(number)
asin = cmath.asin(number)
atan = cmath.atan(number)
cos = cmath.cos(number)
sin = cmath.sin(number)
tan = cmath.tan(number)
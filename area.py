PI = 3.14

def square (side):
  ''' area do quadrado'''
  return side * side

def rectangle (length, width):
  '''area do retangulo'''
  return length * width

def circle (radius):
  '''area do circulo'''
  return PI * radius * radius

print("Area  do quadrado é:", square(10))
print("Area do retangulo é:", rectangle(10, 20))
print("Area do circulo é:", circle(3))

bool_to_int = lambda value: value == False if value < 2 else True
print(bool_to_int(value=1))

get_smaller = lambda a,b: min(a,b)
print(get_smaller(1,5))

def cube(base):
  x =  base**3
  print(x)
cube(5)

def absolute_difference(a,b):
  x = abs(a - b)
  print(x)
absolute_difference(2,5)

def squared_difference(a,b):
  x = a * b
  print(x)
squared_difference(3,11)

def hours_to_minutes(hours):
  minutes = 60
  print(hours * minutes)
hours_to_minutes(hours=1)

def get_circumference(radius):
  x = (2*3.14)*radius
  print(x)
get_circumference(radius=4)

def linear_transform(x, slope, intercept):
  y = (x + slope)/intercept
  print(y)
linear_transform(x=3,slope=1.5, intercept=3.2)

def standardize(x,x_center,scale_size):
  x = ((x-x_center)/scale_size)
  print(x)
standardize(4, 2,6)

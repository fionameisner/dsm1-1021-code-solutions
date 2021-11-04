bool_to_int = lambda value: 1 if value == True else 0
print(bool_to_int(value=True))

get_smaller = lambda a,b: min(a,b)
print(get_smaller(1,5))

def cube(base):
  return base**3
print(cube(5))

def absolute_difference(a,b):
  return abs(a - b)
print(absolute_difference(2,5))

def squared_difference(a,b):
  return (a - b)**2
print(squared_difference(3,11))

def hours_to_minutes(hours):
  return 60 * hours
print(hours_to_minutes(hours=1))

def get_circumference(radius):
  return (2*3.14)*radius
print(get_circumference(radius=4))

def linear_transform(x, slope, intercept):
  return (slope*x)+intercept
print(linear_transform(x=3,slope=1.5, intercept=3.2))

def standardize(x,x_center,scale_size):
  return ((x-x_center)/scale_size)
print(standardize(4, 2,6))

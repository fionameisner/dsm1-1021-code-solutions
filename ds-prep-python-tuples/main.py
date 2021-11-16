passenger = ( 12,True,'Bonnell, Miss. Elizabeth','female',58)
print(passenger)
name = passenger[2]
age = passenger[-1]
print(name , age)

survived_and_name = passenger[1:3]
gender_and_age = passenger[-2:]
print( survived_and_name , gender_and_age)

if 'female' in passenger:
  is_female = True
else:
  is_female = False
if 'male' in passenger:
  is_male = False
else:
  is_male = False
print(is_female + is_male)

def get_survival_info(passenger):
  (id,survived,name,gender,age) = passenger
  passenger = (age,gender,survived)
  return passenger
print(get_survival_info(passenger))

def get_survival_info(passenger):
  (age, survived, name, gender, age) = passenger
  passenger = (11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)
  return passenger
print(get_survival_info(passenger))

def get_survival_info(passenger):
  (id,survived,name,gender,age) = passenger
  passenger = (28, False, "Fortune, Mr. Charles Alexander", "male", 19)
  return passenger
print(get_survival_info(passenger))

def get_survival_info(passenger):
  (id,survived,name,gender,age) = passenger
  passenger = (51, False, "Panula, Master. Juha Niilo", "male", 7)
  return passenger
print(get_survival_info(passenger))

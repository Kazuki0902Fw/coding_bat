# double_char
def double_char(str):
  return ''.join([i*2 for i in str])

# count_hi
def count_hi(str):
  return str.count('hi')

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i]+str[i+1]=='hi':
      count+=1
  return count

# cat_dog
def cat_dog(str):
  return str.count('dog') == str.count('cat')

# count_code
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i]+str[i+1]+str[i+3] == 'coe':
      count +=1
  return count

# end_other
def end_other(a, b):
  return a.lower()==b.lower()[-len(a):] or b.lower()==a.lower()[-len(b):]

# xyz_there
def xyz_there(str):
  return str.count('xyz')>str.count('.xyz')

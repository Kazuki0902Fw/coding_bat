"""warmup_1"""
# sleep_in
def sleep_in(weekday, vacation):
  if vacation:
    return True
  elif (weekday==vacation):
    return True
  else:
    return False

# monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return (a_smile==b_smile)

# sum_double
def sum_double(a, b):
  if a==b: return (a+b)*2
  else : return a+b

 # diff21
def diff21(n):
  if 21>=n: return abs(n-21)
  else: return abs((n-21)*2)

# parrot_trouble
# 'parrot' means inko in Japanese
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

# makes10
def makes10(a, b):
  return (a==10 or b==10) or a+b==10

# near_hundred
def near_hundred(n):
  return abs(n-100)<11 or abs(n-200)<11

# pos_neg
def pos_neg(a, b, negative):
  if negative:
    return a<0 and b<0
  else:
    return (a<0 and b>0) or (a>0 and b<0)

# not_string
def not_string(str):
  if str.startswith('not') : return str
  else: return 'not '+str

# missing_char
def missing_char(str, n):
  str = list(str)
  str.pop(n)
  return ''.join(str)

# front_back
def front_back(str):
  if len(str)>=3: return str[-1] + str[1:-1] +str[0]
  else: return str[::-1]

# front3
def front3(str):
  return str[:3]*3

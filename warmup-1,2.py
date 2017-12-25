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


"""warmup_2"""
# string_times
def string_times(str, n):
  return str*n

 # front_times
 def front_times(str, n):
  return str[:3]*n

# string_bits
def string_bits(str):
  return  str[::2]

# string_splosion
def string_splosion(str):
  pre = str[0]
  new_str = [pre]
  for i in str[1:]:
    pre += i
    new_str.append(pre)
  return ''.join(new_str)

def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

# last2
def last2(str):
  count=0
  for i in range(len(str)-2):
  if str[-2:] == str[i:i+2]:
    count+=1
  return count

# array_count9
def array_count9(nums):
  return nums.count(9)

# array_front9
def array_front9(nums):
  return 9 in nums[:3]

# array123
def array123(nums):
  return '123' in ''.join([str(i) for i in nums])

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

# string_match
def string_match(a, b):
  count=0
  for i in range(0, min(len(a), len(b))-1):
    if a[i:i+2] == b[i:i+2]:
      count+=1
  return count

# cigar_party
def cigar_party(cigars, is_weekend):
  return (is_weekend and 40<=cigars) or (40<= cigars <=60)

# date_fashion
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  else:
    return 1

# squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer:
    return 60<= temp <=100
  else:
    return 60<= temp <=90

# caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday: speed-=5
  if speed<=60: return 0
  elif speed<=80: return 1
  else: return 2

# sorta_sum
def sorta_sum(a, b):
  return 20 if 9<a+b<20 else a+b

# alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    if 0<day<6: return '10:00'
    else: return 'off'
  else:
    if 0<day<6: return '7:00'
    else: return '10:00'

# love6
def love6(a, b):
  return (a==6 or b==6) or (abs(a-b)==6) or (a+b==6)

# int1to10
def in1to10(n, outside_mode):
  return not(1<n<10) if outside_mode else 0<n<11

# near_ten
def near_ten(num):
  return num%10<3 or num%10>7

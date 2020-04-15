def is_on_list(day_list,day):
    return day in day_list;
  
def get_x(day_list, index):
  return day_list[index];

def add_x(day_list,day):
  return day_list.append(day);

def remove_x(day_list,day):
  day_list.remove(day);
  return list;


days = [월화수목금토일]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

"""
Is Wed on 'days' list? True
The fourth item in 'days' is: Thu
['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sat']
['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sat']
"""
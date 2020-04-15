def add_to_dict(dic,key="none",value="none"):
  if type(dic) is not dict:
    print(f"you need to send a dictionary. you sent:{type(dic)}")
  elif key== "none" or value== "none":
    print("you need to send a word and a definition.")
  elif key in dic:
    print (f"{key} is already on the dictionary. Won't add")
  else:
    dic[key]= value
    print(f"{key} has been added.")
'''
add_to_dict("hello", "kimchi"):
you need to send a dictionary. you sent:<class 'str'>

add_to_dict(my_english_dict, "kimchi"):
you need to send a word and a definition.

add_to_dict(my_english_dict, "kimchi", "The source of life."):
kimchi has been added.

add_to_dict(my_english_dict, "kimchi", "My fav. food"):
kimchi is already on the dictionary. Won't add
'''

def get_from_dict(dic,key="none"):
  if type(dic) is not dict:
    print(f"you need to send a dictionary. you sent:{type(dic)}")
  elif key=="none":
    print("you need to send a word to search for")
  elif key in dic:
    print(f"{key}: {dic.get(key)}")
  else:
    print(f"{key} was not found in this dict")
  
  '''
get_from_dict("hello", "kimchi"):
you need to send a dictionary. you sent:<class 'str'>

get_from_dict(my_english_dict):
you need to send a word to search for

get_from_dict(my_english_dict, "galbi"):
galbi was not found in this dict

get_from_dict(my_english_dict, "kimchi"):
kimchi: The source of life.
  '''

def update_word(dic,key,value="none"):
  if type(dic) is not dict:
    print(f"you need to send a dictionary. you sent:{type(dic)}")
  elif value=="none":
    print("you need to send a word and a definition to update")
  elif key not in dic:
    print(f"{key} is not on the dict. Can't update non-existing word.")
  else:
    dic[key]=value
    print(f"{key} has been updated to: {value}")

'''
update_word("hello", "kimchi"):
you need to send a dictionary. you sent:<class 'str'>

update_word(my_english_dict, "kimchi"):
you need to send a word and a definition to update

update_word(my_english_dict, "galbi", "Love it."):
galbi is not on the dict. Can't update non-existing word.

update_word(my_english_dict, "kimchi", "Food from the gods."):
kimchi has been updated to: Food from the gods.

get_from_dict(my_english_dict, "kimchi"):
kimchi: Food from the gods.
'''

def delete_from_dict(dic,key="none"):
  if type(dic) is not dict:
    print(f"you need to send a dictionary. you sent:{type(dic)}")
  elif key=="none":
    print("you need to specify a word to delete.")
  elif key not in dic:
    print(f"{key} is not in this dict. Won't delete")
  else:
    del dic[key]
    print(f"{key} has been deleted.")

'''
delete_from_dict("hello", "kimchi"):
you need to send a dictionary. you sent:<class 'str'>

delete_from_dict(my_english_dict):
you need to specify a word to delete.

delete_from_dict(my_english_dict, "galbi"):
galbi is not in this dict. Won't delete

delete_from_dict(my_english_dict, "kimchi"):
kimchi has been deleted.

get_from_dict(my_english_dict, "kimchi"):
kimchi was not found in this dict
'''

import os

os.system('clear')


# my_english_dict = {}


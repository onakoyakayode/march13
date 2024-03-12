def get_position(club, position):
   if position >= 1 and position <= 4:
       print(f"{club} is qualified for the next champions league")
   elif position > 4 and position <= 6:
       print(f"The {club} is qualified for the next Europa league")
   elif position > 7 and position <= 17:
       print(f"The {club} will remain in the league")
   elif position >= 18 and position <= 20:
       print(f"The {club} will relegate to Division 1")
   else: 
       print(f"The {club} is not here")
       
       
       
       
       
def add_num(a,b):
    return a + b


def check_list(li):
    print(f"Confimed that {li} is a {type(li)}!")
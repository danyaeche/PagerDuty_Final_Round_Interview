
class dish_dasher(object):
  def __init__(self):
    self.dish_repository = {}

  
  def add_dish(self, dish):
    if type(dish) != str:
        print("Dish must be valid cusine 😡")
    elif  dish.isalpha() == False:
        print("Dish must be valid cusine 😡")     
    else:
        dish = dish.upper()
        dish = dish.replace(" ","")
        if dish not in self.dish_repository:
            print("New Dish added to Dish Dasher! 😁")
            self.dish_repository[dish] = True
        else:
            print("Dish is already added to Dish Dasher 😅")

  def delete_dish(self, dish):
    if type(dish) != str:
        print("Dish must be valid cusine 😡")
    elif dish.isalpha() == False:
        print("Dish must be valid cusine 😡")
    else:
        dish = dish.upper()
        if dish not in self.dish_repository or self.dish_repository[dish] == False:
            print("Dish currently isn't in Dish Dasher! 😅")
        else:
            print("Dish is deleted from Dish Dasher 😁")
            self.dish_repository[dish] = False

  
  def view_dishes(self):
    print("Viewing Dish Dash catalog 👍")
    if len(self.dish_repository) == 0:
      print("There's nothing in the list 😜")
    else:
      for key, values in self.dish_repository.items():
        if values == True:
          print(key)
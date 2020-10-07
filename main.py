from dish_dasher_class import dish_dasher

def main():
  dish_dasher_instance = dish_dasher()
  try:
    input_file = open('input.txt', 'r')
    for line in input_file:
      line_list = line.split(" ")
      print(line_list)
      if len(line_list) == 2 and line_list[0] == 'ADD':
        dish_dasher_instance.add_dish(line_list[1][:-1])
      elif len(line_list) == 2 and line_list[0] == 'DELETE':
        dish_dasher_instance.delete_dish(line_list[1][:-1])
      elif len(line_list) == 1 and line_list[0] == 'VIEW':
        dish_dasher_instance.view_dishes()
      else:
        continue
  except Exception as e:
    print (e)
  finally:
    input_file.close()
    
if __name__ == "__main__": 
  main()
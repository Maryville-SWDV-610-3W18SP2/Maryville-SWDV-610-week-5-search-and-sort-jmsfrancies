def bubble(list):
  list2 = []
  while len(list) > 0:
    if list[:] != min(list):
        item2 = min(list)
        list.remove(item2)
        list2.append(item2)
    if len(list) == 0:
        print(list2)
        break
    
def selection(list):
  list2 = []
  while len(list) > 0:
    if list[:] != max(list):
        item2 = max(list)
        list.remove(item2)
        list2.append(item2)
        list2.sort()
    if len(list) == 0:
        print(list2)
        break

def insertion(list):
  num = len(list)
  list2 = []
  total = 0
  item1 = min(list)
  list.remove(item1)
  list2.append(item1)
  for item in range(len(list)): 
    total = total + 1
    item2 = min(list)
    item3 = list[total - 1]
    if item3 < max(list) and item3 > max(list2):
        list2.append(item3)
    if item2 == item3:
        list2.append(item3)    
    if item3 == max(list):
        list2.append(item3)
    if len(list2) == len(list) + 1:    
        list2.sort()
        print(list2)

def hash(list):
    list2 = []
    total = 0
    for i in range(len(list)):
          p = list[0 + total]
          total = total + 1 
          i = chr(p)
          list2.append(i)
          if total == len(list):
            print("Each item in the previous list has been sorted and given a character number:")  
            print(list2)
    
        
def main(list):
  list = []
  userInput = int(input("""Enter the amount of numbers
that you plan to add to the list: """))
  for num in range(userInput):
    num = int(input("Enter a Whole Number: "))
    if num >= 0:
      list.append(num)
    if len(list) == userInput:
      print(list)  
      Question = input("""Would you like a Bubble Sort, Selection Sort,
or an Insertion Sort, Hash:""")
      if Question == "Bubble Sort":
        bubble(list)
      if Question == "Selection Sort":
        selection(list)
      if Question == "Insertion Sort":  
        insertion(list)
      if Question == "Hash":
         list.sort()
         hash(list)
    
main(list)            
    
    
    
    




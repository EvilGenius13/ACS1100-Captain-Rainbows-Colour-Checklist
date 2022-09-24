import random

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def markCompleted(index):
     checklist[index] = ('{} {}'.format(checkmark, checklist[index]))

def listAllItems():
    if(len(checklist) > 0):
        for i in range(len(checklist)):
            print(f"{i} : {checklist[i]}")
    else:
        print("There's nothing here!")

def pick_for_me():
    merge_list = list(zip(colours, clothing))
    random.shuffle(merge_list)
    shuffle_colours, shuffle_clothing = zip(*merge_list)
    final_shuffled_list = "\n".join("{} {}".format(x, y) for x, y in zip(shuffle_colours, shuffle_clothing))
    print(final_shuffled_list)


def select(function_code):
    if(function_code == "A"):
        newItem = input(f"{yellow}Input item to add: ")
        create(newItem)
    elif(function_code == "R"):
        index = int(input("Index to read: "))
        print(read(index))
    elif(function_code == "U"):
        index = input(f"{red}Index number: ")
        index = int(index)
        item = input(f"{red}New item: ")
        update(index, item)
    elif(function_code == "M"):
        index = int(input("Enter index to mark as complete: "))
        markCompleted(index)
    elif(function_code == "P"):
        listAllItems()
    elif(function_code == "X"):
        pick_for_me()
    elif(function_code == "D"):
        index = input("Index number of item to delete: ")
        index = int(index)
        destroy(index)
    elif(function_code == "HELP"):
        print("A: Add item\nR: Read Item\nM: Mark as complete\nU: replace an item\nP: Print full list\nX: Pick my outfit for me!\nD: Delete item\nHELP: See all options\nQ: Quit")
    elif(function_code == "Q"):
        return False
    else:
        print("We all make mistakes! Type help for all options")
    return True

def app_state():
    running = True
    while(running):
        running = select(input(f"{green}What do you want to do? Type help for all options.{blue}: ").upper())


yellow = '\033[0;93m'
blue = '\033[1;94m'   
green = '\033[1;92m' 
red = '\033[1;91m'
checklist = []
checkmark = u'\u2713'
clothing = ('Shoes', 'Shirt', 'Pants', 'Hat', 'Socks', 'Underwear', 'Sweater')
colours = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet')
app_state()


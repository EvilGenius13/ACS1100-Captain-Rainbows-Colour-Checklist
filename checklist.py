#Some things to consider:
#There are seven colors in the rainbow, and seven items of clothing to color.
#He can never wear the same color on any of his items. 
#If he is wearing a purple shoe, he cannot wear a second purple shoe.
#He must wear every color of the rainbow each day.
#Can you help make his mornings easier by developing an algorhythm 
# that will make it easier to pick his clothes?

# As a user, I want to be able to create, 
# read, update, and destroy items in a checklist.

# As a user, I want to be able to mark off colors 
# so I can know that it's already represented.

# As a user, I want to be able to see everything in my list at once 
# so I know what is in my list.

#These functions -- create, read, update, and destroy 
# -- are generally necessary for any software to be considered complete.
green = '\033[92m]'
red = '\033[93m'
blue = '\u001b[34m'
checkmark = u'\u2713'
#CRUD CREATE READ UPDATE DESTROY
checklist = []


#Create Function
def create(item):
    checklist.append(item)

#Read
def read(index):
    return checklist[index]

#Update
def update(index, item):
    checklist[index] = item

#Destroy
def destroy(index):
    checklist.pop(index)

#List all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#Mark completed
def mark_completed(index):
    checklist[index] = ('{} {}'.format(checkmark, checklist[index]))
# Extra goals - change read or update function to add checkmark when complete?

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    #Create item
    if function_code == 'C':
        create = user_input('Input Item: ')
    #Read item
    elif function_code == 'R':
        item_index = user_input('Index Number?')
    #Remember that the item_index must actually exist or our program will crash - find way to block?
        read(item_index)
    #Print all items
    elif function_code == 'P':
        list_all_items()
    #Stop loop
    elif function_code == "Q":
        return False
    #Catch All
    else:
        print("Unkown Option")
        return True



#Test Code
def test():
    create('purple sox')
    create('red cloak')
    create('red shoes')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    destroy(1)

    print(read(0))
    #print(read(1))

    list_all_items()

    mark_completed(1)
    print(checklist)

    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    user_value = user_input("Please Enter a value:")
    print(user_value)


test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)


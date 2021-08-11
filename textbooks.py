import random


# Randomly generates five unique numbers, each corresponding to the textbook a student needs
def textbook_id():
    return random.randint(1,15)


# Textbook requirements for each course being offered this semester
def textbook_list(id):
    
    textbooks = {
        1:'College_Algebra',
        2:'Intro_to_Statistics',
        3:'Pre_Calculus',
        4:'Calculus',
        5:'How_to_Write_a_Paper',
        6:'Popular_Short_Stories',
        7:'How_to_Act',
        8:'History_of_the_World',
        9:'Government_and_Politics',
        10:'Human_Psychology',
        11:'Art_History',
        12:'Basic_Biology',
        13:'Basic_Chemistry',
        14:'Basic_Physics',
        15:'Intro_to_Python',   
    }

    return textbooks[id]

# Determines which class(es) uses the specified textbook
def classList(id):
    classes = {
        1:'College_Algebra',
        2:'Statistics_1',
        3:'Pre_Calculus, Trigonometry',
        4:'Calculus1, Calculus2, Calculus3',
        5:'English_Composition',
        6:'English_Literature',
        7:'Theater_101',
        8:'World_History1, World_History2',
        9:'US_Government',
        10:'Intro_Psychology',
        11:'Art_History1, Art_History2',
        12:'Biology1, Biology2',
        13:'Chemistry1, Chemistry2',
        14:'Physics1, Physics2',
        15:'Programming1',   
    }

    return classes[id]
    
# Determines a cost for each book
def newBookCost():
    whole = random.randrange(50,250)
    part = round(random.random(),2)
    return whole + part

# determines the cost of a used book
def usedBookCost(new_cost):
    used_cost = (0.8) * new_cost
    return round(used_cost, 2)

# determines the rental cost of a book
def rentalPrice(buy_cost):
    rental_cost = (0.5) * buy_cost
    return round(rental_cost,2)



    

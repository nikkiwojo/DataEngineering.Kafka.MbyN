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

    
# Determines how many of each textbook is available
def newBooks():
    return random.randint(25,501)
    
def usedBooks():
    return random.randint(25,501)

def totalBooks(new, used):
    return (new + used)

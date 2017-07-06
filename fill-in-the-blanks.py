#Imported os to allow to clear the screen after a correct answer. Definition is described later as def clear(), should work for both Windows and Linux/MacOs.
import os

# These are the strings that are show whether the user has won or lost the game. Included some emoticons that required some .decode use to get it to work.
win = ' Congratulations you won!!! ' + '\U0001F600'.decode('unicode-escape')#smiley face

lose = '\U0001F480'.decode('unicode-escape') + '  Game Over - You lose ' + '\U0001F480'.decode('unicode-escape')#skull face
replacements = ['___1___','___2___','___3___','___4___']

# ----------------------------------------------------
#Easy Level variables

# Decided to keep them as global variables to be able to abstract the code from the function itself, allowing me to reuse the same main function and changing the variable assigment for each difficulty.
#This is the sample string for the text
sample = '''San ___1___ SF is spanish for Saint Francis; officially the City and County of San ___1___, is the cultural, commercial, and financial center of ___2___ California. Located at the north end of the San ___1___ Peninsula, San ___1___ is about 47.9 square miles (124 km2) in area, making it the smallest county and the only consolidated city, county within the state of California. With a density of about 18,581 people per square ___3___ (7,174 people per km2), San ___1___ is the most densely settled large city (population greater than 200,000) in California and the second-most densely populated major city in the United States after New ___4___ City.'''

# This list contains all the questions to be asked to the user
# Kept questions as answers to allow easy time for the reviewer. :P
questions = ['Write Francisco -->','Write Northern -->','Write Mile -->','Write York -->']

# This list contains all answers per difficulty level, these are mapped to the user inputs using .lower() to give more flexibility on the user input side.
answers = ['Francisco','Northern','mile','York']

# ----------------------------------------------------
#Medium Level variables

sample2 = '___1___ is a seaport ___2___ on the west coast of the United States and the seat of King County, in the state of ___3___. With an estimated 704,352 residents as of 2016, ___1___ is the largest ___2___ in both the state of ___3___ and the Pacific Northwest region of ___4___ America. In July 2013, it was the fastest-growing major ___2___ in the United States and remained in the Top 5 in May 2015. In July 2016, ___1___ was again the fastest-growing major U.S. ___2___. The ___2___ is situated on an isthmus between Puget Sound (an inlet of the Pacific Ocean) and Lake Washington, about 100 miles (160 km) south of the Canada, United States border. A major gateway for trade with Asia, ___1___ is the fourth largest port in ___4___ America in terms of container handling as of 2015.'

questions2 = ['Write Seattle -->','Write Washington -->','Write city -->','Write North -->']

answers2 = ['Seattle','Washington','city','North']

# ----------------------------------------------------
#Hard Level variables

sample3 = '''___1___ officially the City of ___1___, is the third-most populous city in the United States. With over 2.7 million residents, it is also the most populous city in both the state of ___2___ and the Midwestern United States. It is the county seat of Cook County. The ___1___ metropolitan area, often referred to as ___1___land, has nearly 10 million people and is the third largest in the U.S. ___1___ has also been called a global ___3___ capital. In terms of wealth and economy, ___1___ is considered one of the most important business centers in the world.

___1___ was incorporated as a city in 1837, near a portage between the Great Lakes and the ___4___ River watershed, and grew rapidly in the mid-nineteenth century.'''

questions3 = ['Write Chicago -->','Write Illinois -->','Write architecture -->','Write Mississippi -->']

answers3 = ['Chicago','Illinois','architecture','Mississippi']

# ----------------------------------------------------
# Main functions
# As mentioned before clear allow to clean the screen, this keeps the test easy to consume and better organized.
def clear():
    os.system('cls')
    os.system('clear')

#This takes sample text as input, makes a replacement to the global variable -- forsee feedback in this behavior and return a modified string, doing it this way kept my code short and consice.
def question(replacements, answers):
        global sample
        sample = sample.replace(replacements, answers) #change global string and replace it with answer.
        os.system('cls')
        os.system('clear')
        return ('Welcome to ' + level + ' mode\n\n' + sample + '\n\n')# use newly composed string

#this function runs a loop, that if correct will replace the answer in the main string, if not then will show you how many tries you have and substract 1. Once it has reached the 4th correct answer  it uses break to print winning string
def testing():
    tries = 5 #keeps tracks of failed attempts
    index = 0 #keeps track of correct answers
    while tries > 0:
        user_input = raw_input(questions[index])
        if user_input.lower() == answers[index].lower():
            #ignores capitalization by using lower on the user_input
            print question(replacements[index], answers[index])
            index +=1
            tries = 5 #this resets the tries when correct
            if index ==4:
                break

        #if user_input is not in the answer list defined...
        else:
            tries -= 1
            print '\nThis is not an option!' + '\nYou have ' + str(tries) + ' tries left\n'
            #this prints a game over message and quits the application for the user. Similar behavior to the example code provided. Added a hint to help solving if the user reaches last try.
            if tries ==1:
                print 'Hint : ' + '...'+answers[index][1:]
            if tries <=0:
                print '- ' * len(lose)
                print lose
                print '- ' * len(lose) + '\n\n'
                exit()

# ----------------------------------------------------
#running code starts here

# This is the code that runs at the beggining of the tests. It clear the screen and asks for level inputself. Depending on the answer it does two things: it changes the assigment of the sample string, questions and answer to their respective value and then runs the testing function.

clear()
level = raw_input('Hi Udacity reviewer... Choose your Level:\n\n'+'Easy - Medium - Hard : ')
if level.lower() == 'easy':
    clear()
    print 'Welcome to easy Mode\n'
    print sample + '\n\n'
    testing()

elif level.lower() == 'medium':
    clear()
    print 'Welcome to medium mode\n'
    sample = sample2
    questions = questions2
    answers = answers2
    print sample + '\n\n'
    testing()

elif level.lower() == 'hard':
    clear()
    print 'Welcome to hard mode\n'
    sample = sample3
    questions = questions3
    answers = answers3
    print sample + '\n\n'
    testing()

#if the user doesn't select any string he will be defaulted to easy mode.
else: #else default to easy
    clear()
    print 'Welcome to easy Mode\n'
    print sample + '\n\n'
    testing()


#once all answers have been correctly answers, it breaks from the loop and runs this message.
print '- ' * len(win)
print win
print '- ' * len(win) + '\n\n'

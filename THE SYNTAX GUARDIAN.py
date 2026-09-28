import random    #HELPS IN GENERATING RANDOM NUMBER 
import time       #THIS IS OPTIONAL AND IS ADDED TO CREATE A SENSE OS SUSPENSE BETWEEN YOUR RESPONSES THUS MAKING THE PROGRAM MORE ENJOYABLE 
tries=0
                                                          #PROGRAM STARTS HERE
#GIVING THE INSTRUCTION TO THE USER
name=input("Enter your name:-")
name=name.upper()                                        #SO THAT THE NAME COMES IN UPPER CASE (DESIGN)
time.sleep(1)
print('''  
                    ONCE UPON A TIME THERE LIVED A MAN~ THE SYNTAX GUARDIAN~ NAMED''',name,'''A FEARLESS PROGRAMMER.....AFRAID OF NOTHING...
                      He was sent on a mission by his master HIGH SORCERER AJEET SINGH to defeat THE UNDEFEATED PROFFESOR HEXADECIMAL.
 ''')
time.sleep(7)
print('''
                  So he packed his PC and went to the GREAT MOUNT ABYSSUS....a mountaion which was directly attached to an endless DARK VOID
                                            On the top of the mountain sat the HEXAGON CITADEL CASTLE of the Proffesor....

''')
time.sleep(7)
print('''
==========================================================WELCOME TO THE HEXAGON CITADEL CASTLE============================================================
                                                
                    HALT, Tarnished one! I am THE PROFFESOR HEXADECIMAL !!!!! Your master sent you to learn Python ? [Laughs mockingly]
                                     but your journey ends here! Guess my secret number, Tarnished One, or fall into the Void!
''')
time.sleep(7)
print('''
                  I will be generous with you by giving you 5 ATTEMPTS.....THE NUMBER I AM THINKING WILL BE IN BETWEEN OF 1 TO 10.........
                             BEWARE!!!!!! TARNISHED ONE.. DO NOT GUESS BLINDLY , THINK BEFORE MAKING YOUR NEXT CHOICE......

                                          OR ELSE YOU WILL BE PUSHED IN AN ENDLESS VOID AND FALL FOR ETERNITY

''')
time.sleep(16)
print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LETS START...... GOOD LUCK TARNISHED ONE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
time.sleep(3)
secret_number = random.randint(1, 10)                          #OUT OF THE LOOP SO THAT IT DOES NOT GENERATE A NEW NUMBER EACH TIME....
while tries<5:                                                   #0 and 100 are also included in this randint.............
    time.sleep(1)
    try:
        while True:
            a = int(input("OKAY TARNISHED WHATS YOUR GUESS??:-"))
            if a>0 and a<11:
                    break
            else:
                print("")
                print("Tarnished are you provoking  me to increase the difficulty....??????  I TOLD YOU NUMBER IS BETWEEN 1 TO 10 ")
    except ValueError:
        print("OH TARNISHED DON'T YOU KNOW WHAT DOES A NUMBER MEAN ????.")
        continue
    tries+=1                #counter to count the number of tries (here 5)
    time.sleep(2)
    if a == secret_number :
        print('''
                                            [THE SECRET NUMBER BURSTS INTO A BLINDING GOLDEN LIGHT!]
        ''')
        time.sleep(3)                                            #example of using time module to create time.sleep({seconds}) this will delay the execution of the next statement
        print('''
                                                    [Professor Hexadecimal shrieks in rage!]
                                        IMPOSSIBLE........THIS...CA-..CAN'T BE TRUE...... I CANNOT LOSE...... ''')
        time.sleep(2)
        print('''
                                  [He strikes the ground with dark magic and vanishes into a plume of angry black smoke!]
                        You think victory is yours, Tarnished One?! You have merely decoded a single digit of your own doom!
                                    Mount Abyssus will become your tomb, whether you solve my riddles or not!
        ''')
        time.sleep(4)
        print('''
                                           [AS THE DARK MAGIC VANISHES THE GATES OF KNOWLEDGE OPENS]
                    Now the Tarnished is no longer a SYNTAX GUARDIAN............now known by GRAND MASTER OF THE PYTHON REALM
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
        time.sleep(6)                                           #this is not necessary but while running in cmd the program stopped instantly (this will prevent it)
        break                                                   #to break the loop is the answer is correct 
    else:
        if tries==1:
            print('''
        TARNISHED ONE the number you entered is not correct ..........
                    ''')
            print('''
        Try AGAIN Tarnished one [PROFFESOR LAUGHING AND MOCKING YOU]........
                    ''')
        if tries==2:
            time.sleep(2)
            print('''
        TARNISHED ONE your guess is incorrect once again...I FEEL PITY FOR YOU..........
                    ''')
            time.sleep(2)
            print('''
        OKAY TARNISHED ONE..... WOULD YOU LIKE TO HAVE A HINT ????
            BUT IT WILL REDUSE YOUR 1 TRY.. CHOOSE WISELY.......
             ''')
            while True:
                hnt=input("Enter yes or no:-")
                if hnt.upper()== "YES" or hnt.upper()=="NO":
                    break
            time.sleep(2)
            if hnt.upper()=="NO":
                print('''
                  WELL WELL WELL............ ITS YOUR WISH....... DON'T COMPLAIN AFTERWORDS
                ''')
            if hnt.upper()=="YES":
                tries+=1
                print('''
                TARNISHED ONE ..... YOU HAVE CHOSEN TO SACRIFICE YOUR 1 TRY TO GET A HINT........
                ''')
                if a>secret_number:
                    print('''
                TARNISHED ONE .....THE NUMBER YOU ENTERED NOW WAS GREATER THAN THE NUMBER I WAS THINKING........
                    ''')
                else:
                    print('''
                TARNISHED ONE .....THE NUMBER YOU ENTERED NOW WAS LESSER THAN THE NUMBER I WAS THINKING........
                    ''')
        if tries==3:
            time.sleep(2)
            print('''
                TARNISHED ONE i expected more from the student of THE HIGH SORCEROR .............
                    ''')
        if tries == 4:
            print('''
                                    Four failures, TARNISHED ONE! Your logic crumbles before my cipher!
                    ''')
            time.sleep(3)
            print('''
                                    One final attempt remains... next destination The void?? who knows
                   
                                     [PROFESSOR HEXADECIMAL LAUGHS  AND POINTS TO THE EDGE OF THE CLIFF]
                    ''')
            time.sleep(3)
            print('''
                 ARE YOU SURE TARNISHED ONE ?? THIS IS YOUR LAST TRY IF YOU GET THIS WRONG.........I WILL PUSH YOU IN THE VOID
                                                 WHERE YOU WILL FALL FOR THE REST OF YOUR LIFE
             ''')
            time.sleep(2)
            print('''
                 TARNISHED ONE WITHOUT HESTITATING SAID ''I WOULD RATHER SACRIFICE MYSELF THAN DISSAPPOINT MY MASTER.......
                                                         "Hesitation is defeat" he says''
            ''')
            time.sleep(2)
        if tries==5:
            time.sleep(5)
            print('''
==============================================[Professor Hexadecimal smiles coldly as dark arcane energy surrounds you...]==================================
''')
            time.sleep(2)
            print("                                                 NOO NOO TARNISHED ONE I WAS THINKING OF  ", secret_number)
            time.sleep(3)
            print('''
                Five wrong guesses, Tarnished One..... your attempts are exausted !!! A flawed variable must be erased—
                                            DOWN INTO THE ENDLESS VOID YOU GO!
            ''')
            time.sleep(2)
            print("                     [As you plunge into the darkness of the Endless Void, Professor Hexadecimal's laughter echoes from atop Mount Abyssus...]")
            print('''
=================================================================GAME OVER=============================================================
                ''')
            time.sleep(16)#this is not necessary but while running in cmd the program stopped instantly (this will prevent it)      

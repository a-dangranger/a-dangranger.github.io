#Objective: Randomly Generate Funny Names

#Components & Strategy:
'''
-Create data frame of various words
-Words will be randomly paired.
-User will need to intall Pandas and openpyxl
-We will read from the 1st sheet which contains the first and last name. We will specifiy
the column from which to pull that data. We will also pull from a different sheet which contains
the middle names.
-"Customer" Request: Ensure the output names font always appears in red.
-Ensure the user can re-run the program until they choose to stop.
-Ensure file notes/pseudocode adequately describe each segment of code.
'''

#Import
import pandas as pd

#Read Names Files
adverbs_df = pd.read_excel("new_names_list.xlsx", sheet_name="Adverbs",usecols="A")
Gerunds_df = pd.read_excel("new_names_list.xlsx", sheet_name="Words",usecols="A")
Agent_Nouns_df = pd.read_excel("new_names_list.xlsx", sheet_name="Words",usecols="B")

#Now we concatenate all the columns into one
horizontal_concat = pd.concat([adverbs_df, Gerunds_df, Agent_Nouns_df], axis=1)
horizontal_concat.dropna()

#Define red font color
RED = '\033[31m'

#Create a reset to go back to standard font color
RESET_TEXT = '\033[0m' # called to return to standard terminal text color

#Print user message
print("\nWelcome to the wacky Charades generator!")
print("I'll give you a prompt and you act it out for your friends to guess.")
print("Here's a prompt just for you:\n")


while True:
    Lname_output = horizontal_concat["Adverbs"].sample().values[0]
    Mname_output = horizontal_concat["Gerunds"].sample().values[0]
    Fname_output = horizontal_concat["Agent Nouns"].sample().values[0]
    print("\n" + RED + f"{Fname_output} {Mname_output} {Lname_output}\n" + RESET_TEXT)

    go_again = input("Would you like another wacky action?\nIf yes, enter y. Entering any other character will end our conversation.\n")
    if go_again.lower() != 'y':
        break

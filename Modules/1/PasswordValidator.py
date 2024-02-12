# define a function that supports a multi line text with border for the end user introduction message and that handles white space

def print_with_border(message): 
    lines = message.split('\n') # split input message into list of lines using '\n' as seperator
    stripped_lines = [line.strip() for line in lines] # create a new list where each line is stripped of leading and trailing white spaces
    stripped_message = '\n'.join(stripped_lines) # join the stripped lines into a single string seperated by new line characters

    max_line_length = max(len(line) for line in stripped_lines)# find the length of the longest line in the stripped message to determine border width

    border = '*' * (max_line_length +4)# create a border made of asterisks
    formatted_message = '\n'.join([f'* {line.ljust(max_line_length)} *' for line in stripped_lines])# create new list where each line is formatted with astericks on each side, and total width matches longest line length
    
    print()
    print(border) # show the border
    print(formatted_message)
    print(border)
    print()
# define a function to test the proposed password against the password policy 

def checkPassword(password): 
    deny_list = ["password", "123456", "qwerty", "abc123"] # define a list of known passwords that will be denied for use. You can add more to the list if you want.  
    if password in deny_list: # check if the password is in the deny list 
        print("""
            ======================================================================================  Test 1 in progress   =============================================================================
                
            +++ Test 1 Failed :-( +++ Password is in the deny list due to it being very common and easily guessed")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
        return False
    else:
        print(""" 
            ======================================================================================  Test 1 in progress   =============================================================================

            +++ Test 1 passed! +++ password is not too common or easily guessed")   

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

        if not (12 <= len(password) <= 50):   # validate that the password is between 12 and 50 characters 

            print(""" 
            ======================================================================================  Test 2 in progress   =============================================================================

             +++ Test 2 Failed :-( +++ The password must be between 12 and 50 characters. Did you try using a phrase? Using a phrase is a great way to create a long password that is easy to remember.

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
            return False
        print(""" 
            ================================================================================  Test 2 in progress   ===================================================================================

            +++ Test 2 passed! +++ password is an adequate length")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

        if not any(char.islower() for char in password):  # validate that the password has atleast one lower case character

            print("""
            ======================================================================================  Test 3 in progress   =============================================================================

            +++ Test 3 Failed :-( +++ The password should have at least one lower case letter")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
            return False
        print(""" 
            ======================================================================================  Test 3 in progress   =============================================================================

            +++ Test 3 passed! +++ atleast 1 lower case character  is present in the password")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
        if not any(char.isupper() for char in password): # validate that the password has atleast one captial letter
            print("""

            ======================================================================================  Test 4 in progress   =============================================================================

            +++ Test 4 Failed :-( +++ The password should have at least one capital letter")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
            return False
        print("""
            ======================================================================================  Test 4 in progress   =============================================================================

            +++ Test 4 passed! +++ atleast 1 upper case character is present in the password")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

        if not any(char.isdigit() for char in password): # validate that the password has atleast one number

            print("""
            ======================================================================================  Test 5 in progress   =============================================================================

            +++ Test 5 Failed :-( +++ The password should have at least one number")

            ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
            return False
        print("""
            -----------------------------------------------------------------------------------------  Test 5 in progress   --------------------------------------------------------------------------

            +++ Test 5 passed! +++ atleast 1 number is present in the password")
        
            ======================================================================================  \033[1mAll tests passed - Congratulations!\033[0m   ==============================================
        
                                                                     ... Great job picking your password. It conforms to best practice ... Enjoy your day and bye! ...")
        
            ==========================================================================================================================================================================================""")
        print()
        return True

# define a function to specify main logic to be run

def main():
    while True:
    # multi line message to introduce end user to the program  
        multi_line_message = """
            Thank you for taking password best practice seriously. 
            This program can be used to help you determine if a password is following best practice.
            
            Step 1: Enter a proposed password 
            Step 2: Learn if it conforms to best practice

            Below are the tests that your password will need to pass in order to conform to best practice:

            +++Test 1+++ The password is not very common or easily guessed
            +++Test 2+++ The password is long(12+ characters) but not tooo long (>50 charachters). Hint: Try using a phrase! 
            +++Test 3+++ The password has atleast one lower case charachter
            +++Test 4+++ The password has atleast one captial letter
            +++Test 5+++ The password has atleast one number
        """      

        # call the function to print the end user program introduction using multi line and border
        print_with_border(multi_line_message) 

        # get proposed password input from end user
        print(""" 

            ===================================================================================  \033[1mLets get started\033[0m ....  ================================================================""")
        print()
        password = input("Please enter a password: ") 
        
        print("""

            ==========================================================================================================================================================================================""")
        print()    
        # display proposed password to end user 
        print("The password you tried is: ", password)

        # call the function to run tests
        if checkPassword(password):
            break # exit loop if password validated
        else:
            print(""" 
            ======================================================================================  ...\033[1mTesting failed\033[0m :-(...   =========================================================""")
            
            try_again = input("                                                                   Would you like to try again? (yes/no): ").lower()
            
            print("""
            ==========================================================================================================================================================================================""")

        if try_again != 'yes':

            print(""" 
            ======================================================================================  ...\033[1mThats all folks\033[0m ...   ===========================================================")
            
                                                                                                   Thanks for your time. Goodbye!")
            
            ==========================================================================================================================================================================================""")
            break # exit loop if end user doesnt want to try another password
        else:
            print(""" 
            ==========================================================================================================================================================================================")
            
                                                                                                        Restarting the program ... 
            
            ==========================================================================================================================================================================================""")
if __name__ == "__main__":
    main()

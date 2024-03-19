taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']  # List of Taken Usernames
username, password = '', ''  # Varibles to hold the Newly Made Username and Password
username_input, password_input = '', ''  # Starting Varibles for Input

# Username Test Varibles
taken_test, lower_test, underscore_test, alpha_num_test = False, False, False, False

#Password Test Varibles
length_test, space_test, special_test = False, False, False
uppercase_test, lowercae_test, digit_test = False, False, False  # Initiating the Varibles for the p Loop below

print('''To sign up, create a Username and Password.
The Username must start with a lowercase letter and only contain letters, numbers, and underscores.
The Password must contain each of the following.
● At least 8 characters long
● At least one uppercase letter
● At least one lowercase letter
● At least one digit
● At least one of these characters: !, ?, @, #, $, ^, &, *, _,  -
● Doesn't contain any spaces''')

# Username Creation
while True:
    username_input = input('Create Username: ')  # Input for creating a new Username
    
# Tests for Username
    taken_test = username_input not in taken_usernames  # Test to check if Username is Taken
    lower_test = username_input[0].islower()  # Test to check if first letter is Lowercase Letter
    underscore_test = ('_' in username_input)  # Test to check if there are any Underscores
    for u in username_input:
        alpha_num_test = username_input.isalnum()  # Test to check for Letters and Numbers

    # Creation Loop
    if taken_test and lower_test and (underscore_test or alpha_num_test) == True:  # Test to see if Username meets all Requirements
        username += username_input  # If True, adds Username Input to Username Varible.
        taken_usernames.append(username_input)  # If True, adds Username Input to Taken Usernames.
        print('Username Made Successfully')  # If True, confirms that Username was Created.
        break
    elif taken_test == False:
        print('Username Taken')  # If Username is Taken, User will be informed that it was taken.
        continue
    else:
        print('Invalid Username')  # If Username is Invalid, User will be informed that it does not meet the requirements.
        continue


# Password Creation
while username != ' ':  # If Username is Made and pushed into its Varible, Password Creation Starts.
    password_input = input('Create Password: ')  # Input for creating a new Password

# Tests for Password
    length_test = (len(password_input) >= 8)  # Test for making sure the Password is 8 characters or greater
    space_test = ' ' not in password_input  # Test for making sure the Password has no spaces

# Test for the Special Characters in the Password
    special_test = '!' in password_input, '?' in password_input, '@' in password_input, '#' in password_input, '$' in password_input, '^' in password_input, '&' in password_input, '*' in password_input, '_' in password_input, '-' in password_input
    for s in special_test:
        if s == True:
            special_test = True

    for p in password_input:
        if p.isupper():
            uppercase_test = True  # Test for at least one uppercase letter
        if p.islower():
            lowercae_test = True  # Test for at least one lowercase letter
        if p.isdigit():
            digit_test = True  # Test for at least one number

    if length_test and space_test and uppercase_test and lowercae_test and digit_test and special_test == True:  # Test to make sure Password meets all requirements
        password += password_input  # If True, adds Password Input to Password Varible.
        print('Password Made Successfully')  # If True, confirms Password was Created.
        break
    else:
        print('Invalid Password')  # If Password is Invalid, informs User that Password does not meet the requirements.


# Login Loop
print('Sign up successful. Now Login.')
while username != ' ' and password != ' ':  # If Username and Password is created and pushed to their varibles, Login Starts.
    username_input = input('Enter your Username: ')  # Login Username Input
    password_input = input('Enter your Password: ')  # Login Password Input

    if username_input == username and password_input == password:  # Testing if the currently made Username and Password matches the Login Input
        print('Login Successful')  # Telling the User that they typed in the right Username and Password
        break
    else:
        print('Incorrect username or password')  # Telling the User that they typed in the wrong Username and/or Password
        continue
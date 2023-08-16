 # PASSWORD X : By Matthew Lewis
 #### Video Demo:  <https://youtu.be/aXJmxhKc_B8>
 #### Description: Simple Python password generator and checker
Password X is a simple command line password generator that can generate two styles of password and test your current password against HIBP.

### 1. Complex password string:
-  This type of password can be any length from 8 to 128 characters in length use a mix of uppercase characters, lowercase characters and numbers and symbols.
Using the function below will return a generated string using the supplied parameters:

` def generate_random_password(length: int = 8, character_set: int = 2) -> str:`
      
Generate a random password s using the supplied parameters.

### Parameters

length : int default = `8` supply a s length from 8 to 128

character_set : int default = `2`

- 1: character_set (Upper_case, lower_case, numbers)
- 2: character_set (Upper_case, lower_case, numbers, symbols)
- 3: character_set (Upper_case, lower_case, symbols)

####  Allowed symbols are !@#$%^&*
### Returns
s : str

a random password in string format


### 2. Multi word passphrase:
Research shows the days of one-word passwords are numbered and taking their place are passphrase's. multiple word phrases using letters, symbols and spaces to create keys that are nearly impossible to crack.

The below function will generate a multi word password using the supplied parameters

`def multi_word_password(num_words: int = 3, capitalization: bool = False, upper_case: bool = False,sep: str = " ",) -> str:`

### Parameters

num_words : int default = `3`

capitalization : bool default = `False`

upper_case : bool default = `False`

sep : str default = ` " "`

### Returns
random_word : str

The program includes a words.csv file with over **58 thousand english words** for use.


### 3. Password Breach checking
By making use of the Have I Been Pwned API the program can check if your password has been seen in any recent breaches. This is useful information. Knowing if your password is breached helps you to stop using bad passwords.
   

The function below will take a string and convert it to a SHA1 hash to be used the test against the have I been Pwned database. The program makes use of the getpass library so you will not see your password on screen when testing.

   `def check_password(password: str) -> int:`

 ### Parameters
 string password : str

This plain text is converted to a SHA1 hash using a support function.

### Returns
     
count : int The number of times the password has been seen.

The above 3 functions make up the main functionality of the program. There is Class for the main menu of the program. keeps track of the user's choice and calls the appropriate functions.
# Password-cracker
Prove the correctness of your solution by providing the plaintext password for the username
The real strength of the Python programming language lies in the wide array of standard and third-party libraries. To write our UNIX password cracker, we will need to use the crypt() algorithm that hashes UNIX passwords. Firing up the Python interpreter, we see that the crypt library already exists in the Python standard library. To calculate an encrypted UNIX password hash, we simply call the function crypt.crypt() and pass it the password and salt as parameters. This function returns the hashed password as a string. 

Read through the details on the Python wrapper for the Unix crypt() algorithm.
Programmer$ python >>> help('crypt') 
Let’s quickly try hashing a password using the crypt() function. After importing the library, we pass the password “egg” and the salt “HX” to the function. 
programmer$ python
>>> import crypt
>>> crypt.crypt("egg","HX") 'HX9LLTdc/jiDE' 

The function returns the hashed password value “HX9LLTdc/jiDE” as a string. Success! Note that the salt appears as the first two characters of the encrypted string. Now we can write a program to iterate through an entire dictionary, trying each word with the custom salt for the hashed password. 
To write your program, you will create two functions: main() and testpass(). It proves a good programming practice to separate your program into separate functions, each with a specific purpose. In the end, this allows you to reuse code and makes the program easier to read. Your main function opens the encrypted password file “passwords.txt” and reads the contents of each line in the password file. For each line, it splits out the username and the hashed password. For each individual hashed password, the main() function should call the testPass() function that tests passwords against a dictionary file. This function, testPass(), should take the encrypted password as a parameter and returns either after finding the password or exhausting the words in the dictionary. 
Hint: testPass() will need to account for the salt that represents the first two characters of the encrypted password hash. 

Q00. Prove the correctness of your solution by providing the plaintext password for the username ‘morty’ in the password file. 
jessica

A basic Spell checker

It reads from a corpus of text and builds up a dictionary of words with their corresponding frequencies. Then when given an input of (possibly)misspelt
words, the program outputs the most likely known word from the dictionary. The program will only look for spelling errors with an edit distance of 2,
which covers about 98% of errors. It will look for the most common spelling errors in the form of-> Deletion, Replacement, Transposition, Insertion. 
This work is inpired from Peter Norvig's work on the same subject, which can be found here -> http://norvig.com/spell-correct.html.

Sample Input

4
musix
seroius  
pureli
nose

Sample Output

music
serious
purely
nose
 

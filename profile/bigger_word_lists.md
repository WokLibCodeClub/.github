# Adding your own word list to the Hangman game

There is a list of 400 common words in the file called *Hangman_words.txt* in the [Hangman project](https://github.com/WokLibCodeClub/Hangman/blob/master/README.md) but some students wanted to use a larger word list. This sometimes caused a problem, because the word from the new list might be in lower case letters, but all the guessing and testing in *Hangman* is set to use CAPITALS. This page will show you how you can use a larger list without causing formatting errors as you run the game.

## A word list where the words are not all in CAPITAL letters

The game is set up for a word list where all the words are in CAPITAL letters. But what if you want to import a list of words from the internet which has words with small letters, or a mixture of capitals and lower case?

The simplest way to use a list like this is to make a slight change to one line of code in the game:

The first bits of code in the game, after making the list of pictures, deal with opening the list of words as a file, reading the contents into Python and converting all the words into a Python *list*. The next line selects one of the list items at random to use as the mystery word. The line that does this is

```python
word_to_guess = choice(wordlist)
```

The change you need to make in order to use a word list in which the words are not all in capitals is this

```python
word_to_guess = choice(wordlist).upper()
```

This will now carry out an additional function after selecting the word at random and before setting the variable ```word_with_guesses``` - namely converting the chosen word to CAPITAL letters. So, it doesn't matter whether the words in the word list are capitals, lower case or a mixture, the variable ```word_to_guess``` will *always* be set to a word which is all CAPITALS. Now you can proceed to guess the mystery word as before.

## Applying some filters to the larger word list

In the original *Hangman_words.txt* word list the words were all selected to make sure they were not too long and not too short (they are all between 6 and 10 letters long), and also that they weren't people's names or brand names, and that they weren't rude words. You can't use Python to check for rude words but you can certainly write some code to filter out words which are too long or too short.

We have already used the Python command to open a file to *read* the contents - now we will use the command to open a file to *write* something to it. This will magically create a new file in your trinket project.

Firstly, start a new trinket project and put in the usual line to make sure trinket will use Python 3 commands:

```python
#!/bin/python3
```

Next, create a file in your project. Do this by clicking on the **plus** sign at the top right corner of the edit pane:

![Click to add a file](add_file.png)

This will open up a box where you can name your file. I used the name Hangman words.txt:

![CName a file](name_file.png)

You can now paste your new wordlist into this new file:

![CAdd words](word_list.png)

Now we can use the same code as in the Hangman game to open our new file, read the words into Python, and convert the words into a Python list:

```python
wordfile = open('Hangman words.txt', 'r')
wordlist = wordfile.read().splitlines()
```

Make sure the name of the new file (in quotes) is exactly the same as the name you gave your file.

The first line here *opens* an existing file, and the bit of code ```'r'``` inside the brackets indicates that we want to ***read** from the file. But as we filter our words and decide to keep some and not others we will also need a file to save the words we want to keep. This file doesn't yet exist, but Python will make it for use if we use this code:

```python
filteredwordfile = open('Hangman words filtered.txt', 'w')
```

The ```'w'``` inside the brackets indicates that we are going to ***write*** data to this file, and if the file doesn't exist then Python knows it has to create it. We have told Python to name this new file *Hangman words filtered.txt*. You won't see the new file immediately - first you will have to write something to it.

### a ```for``` loop to go through all the words

Next we add a ```for``` loop to go through all the words in the list. This will begin something like this:

```python
for word in wordlist:
```

Here ```word``` is just a name for a Python variable - you can use any valid variable name. Whatever the name, this loop will set the variable in turn to every word in the list, which means we can do some tests on the word to see if we want to keep it in our filtered list, or chuck it out. Let's say we only want to keep words which are seven letters long. So each time we go through the loop we need to text the length of the word with an ```if``` statement:

```python
  if len(word) == 7:
```

(Notice that this line has to be indented.)

What do we want to do if the length is equal to 7? Well we want to write the word into the new *Hangman words filtered.txt* file, which is done with this code:

```python
    filteredwordfile.write(word)
```

# Code review for grouping anagrams together

- line 1: Incorrect indentation level, you have to use the same number of spaces in the same block of code, otherwise Python will throw IndentationError.

- line 3: Your code does not have any comments, please provide comments to help the next developer understand your code easily. For example, right before ```result = {}```, you can write a comment like: #initializing an empty dict

- above line 4: Comment your code e.g #iterating over the list to group all anagrams

- line 5: You did not provide any arguments for the ```sorted()``` function. This function have a required argument - iterable, which is the sequence to sort, list, dictionary, tuple etc.

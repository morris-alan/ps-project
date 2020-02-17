# ps-project
Demo project: This project is intended to be a tutorial, with solution.py altered until it passes all the tests. Running the tests is covered below. 

This has been tested on Linux and Mac using python version 3.6, not on Windows for any version of python.

## Introduction

In 2018 the Zimbabwe Electoral Commission released the full voters roll for the historic July harmonised elections, for the first time in 38 years the recently deposed dictator Robert Gabriel Mugabe would not appear on ballot, replaced by his former ally Emmerson Mnangagwa. Elections in Zimbabwe are steeped in a history of fraud, rigging and violence.

The original voters roll was, for a time, downloadable from this [website](https://zimelection.com/votersroll.php), as a disjointed collection of Microsoft excel(xlsx) documents. They contained detailed personal information on registered voters including names, phone numbers, addresses and National Identification numbers.

Today we will be searching a subsection of an altered version of the original voters roll(Harare Metropolitan area) for invalid or incorrectly captured national ID numbers. Within the provided data names have been mixed and the ID numbers are all fake, in addition there are only 3 columns - ID number, first names, surname. 

The goal of this exercise is to search the 900301 rows of fake registered voters and find the 10 planted invalid ID numbers.

## About the national ID number

A Zimbabwe National Identification number consists of 11 or 12 alpha numeric characters and is represented in the data as the following string of characters:

70-991814-P70

The first 2 digits represent the province where the ID was issued, the next 6 are unique identity digits. The first of the trailing 3 characters is always a capitol letter checkdigit, calculated from the previous 8 digits but not from the last 2 digits which loosely encode the ethnicity of the ID holder.

The checkdigit helps detect simple errors in the ID when humans manually input, transcribe or capture the ID. Such as hearing 17 in place of 70, switching 2 digits(9181 instead of 9981) or reading badly written characters incorrectly. For example,

| Description of variation | Example ID string |
| --- | --- |
| Original ID with correct checkdigit(P)                                               | 70-991814-P70 |
| 2 Digits have been swapped(91-19), calculated checkdigit would be D                    | 70-919814-P70 |
| 70 changed to 17, calculated checkdigit would be T                                         | 17-991814-P70 |
| 5th digit altered to 7 from 1(common handwriting error) calculated checkdigit would be L   | 70-997814-P70 |

The checkdigit is calculated by taking the remainder of the first 2 sets of digits (as a single integar) divided by 23. The checkdigit is the corresponding letter from Latin alphabet with the ambiguous character O,U and I removed for the following reasons:

| Letter | Confused for |
| --- | --- |
| O | number 0 |
| U | The letter V |
| I | Lowercase L or the number 1 |

For example, the ID number 70-991814-P70 has the relevant digits 70991814 (P is the checkdigit and 70 is not included in the calculation). 14 is the remainder of the division of 70991814 by 23:
```
>>> 70991814 % 23
14
```
and P is the 14th character of the Latin alphabet after O, U and I have been removed.
 
## How to Proceed

This project can be completed using the standard libraries and only requires a default install of python version 3:
- Unit tests were written for the [unittest framework](https://docs.python.org/3/library/unittest.html)
- The data can be read with the [csv library](https://docs.python.org/3/library/csv.html)

```example_solution.py``` is a completed example solution (try not to peak until you've passed all the tests!).
You will complete this project by editing the file ```solution.py```, you can open that now in your favorite text editor, currently it only contains a header and main method. **solution.py is the only file you will have to edit to complete all the tasks.**

within the data directory are 2 files:
- ```mangled_voters_roll_hre.csv``` : The complete fake dataset with 10 planted invalid ID numbers 
- ```truncated_mangled_voters_roll_hre.csv``` : The first 10 entries of the complete dataset

**Until the final task, use the truncated voters roll**, it will be easier to debug and run faster.
The third entry (59-772671-B59,RUTH,MUCHENGETE) of both files has an ID number with an error. The correct checkdigit would be T.

```test_solution.py``` contains unit tests for each task in this project. The tests can be run on debian based systems by opening a terminal in the root directory of the project and executing the following command:
```
python3 -m unittest -vf
```
**Do this after making any changes to solution.py (Save your changes first!)**
You can go ahead and run it now, it will produce the following output:
```
$ python3 -m unittest -vf 
++++++++++++++++++++++++++++++++++++++++++++++++++
You're program produced the following output:
Hello, world.
++++++++++++++++++++++++++++++++++++++++++++++++++
test_task_1 (test_solution.TestIDValidationMethods) ... FAIL

======================================================================
FAIL: test_task_1 (test_solution.TestIDValidationMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "~/test_solution.py", line 37, in test_task_1
    self.assertNotRegex(self.captured_text,"Hello, world.", "\n\nDon't forget to delete the line: \nprint(\"Hello, world\")")
AssertionError: Regex matched: 'Hello, world.' matches 'Hello, world.' in 'Hello, world.' : 

Don't forget to delete the line: 
print("Hello, world")

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```
The first section shows the output of running solution.py, in this case printing ```Hello, world.```
Below this is a summary of the tasks that you have passed thus far. Right now you haven't passed any, but we'll fix that in a moment. 

Finally, the output shows the most recently failed test and possibly information on how to pass the test given what is currently in your solution.py file.

## Tasks
### Task 1: Reading a csv file.
For the first task we will use the [csv library](https://docs.python.org/3/library/csv.html) to read in the CSV file (truncated_mangled_voters_roll_hre.csv).

We can copy and alter the example code found in the [library documentation](https://docs.python.org/3/library/csv.html#examples).

In the main() function of solution.py, remove ```print("hello, world.")``` and add the code from the example, replacing ```'some.csv'``` with the path to the truncated data file (for Mac or Linux: ```"data/truncated_mangled_voters_roll_hre.csv"``` If you are using Windows change '/' to '\\').

Run the tests whenever you want to verify if a change that you've made brings you closer to passing the task, some of the error messages may be helpful!

If you get a syntax error check your indentation, punctuation, and spelling and don't forget to save solution.py every time before you run the tests!

When you have passed task 1 the feedback should start something like this:
```
test_task_1 (test_solution.TestIDValidationMethods) ... ok
test_task_2 (test_solution.TestIDValidationMethods) ... FAIL
```
It's good style to place all import statements at the top of your code, before any methods and after the header.

If you've passed Task 1 then it's time to move on to the seccond task

### Task 2: Printing only the ID number.
The ```reader``` in the main function is an [iterator](https://wiki.python.org/moin/Iterator), with each 'next' returning a list, which is made up of the next row in the file. So, in the first iteration of the 'for loop', ```row``` is the list:

```['70-991814-P70', 'ALICE', 'ZULU'].``` 

In subsequent iterations, the variable ```row``` will represent the subsequent line in the data file. 

We can alter the current program to print only the ID numbers by selecting the first item of each list in the print statement. The syntax for selecting the n'th item of a list in python is ```variable_name[n]```. What is our variable name? For 'n', remember python lists are indexed from 0.

### Task 3: Extracting the checkdigit from an ID.
We now need to create a function called ```get_id_checkdigit``` which will accept an ID number as a string in the format 

```"70-991814-P70"``` 

and return the checkdigit:

```P``` 

as a single character. Note that in all the ID's in the folder, the checkdigit is third to last. Remember strings can be indexed from the end. Remember to [define your argument and your return value](https://www.learnpython.org/en/Functions).


### Task 4: Extracting the relevant numbers from an ID.

To help us with the next function, we'll write a function called ```get_id_digits``` which will accept an ID number as a string in the format 

```"70-991814-P70"```

and return the first 8 digits as an integer:

```70991814```

Notice that the ID's all have the form 2 digits, dash, 6-7 digits. So we can [break](https://docs.python.org/3/library/stdtypes.html#str.split) the ID string into parts and concatenate the resulting sub strings. Be careful to concatenate strings before casting the digits to an integer.

### Task 5: Calculating the checkdigit from an ID. 

Now we'll write a function called ```calculate_id_checkdigit``` which will accept an ID number string in the format 

```"70-991814-P70"```

and return the calculated checkdigit:

```P```

We can use the function ```get_id_digits``` to extract the digits and then use the [remainder opperator](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) (```%```) to calculate the checkdigit numerical value. 

A checkdigit letter can be determined from the above numerical value by [indexing](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations): 

```"ABCDEFGHJKLMNPQRSTVWXYZ"```

Which is the uppercase Latin alphabet with the characters O, I and U removed. This will substitute the numerical value of the checkdigit for the corresponding letter. 

### Task 6: Check the validity of an ID.

Using the functions that we've written, we can now write a function called ```check_id_valid``` which will accept an ID number string in the format 

```"70-991814-P70"```

and return ```True``` if the calculated checkdigit matches the extracted checkdigit and ```False``` if they don't match.

### Task 7: Print out invalid ID numbers.
Now we can find the ID numbers that are invalid in the truncated dataset! 

To do this we will alter the ```for loop``` in the ```main``` function to only print out the **ID number** if the function ```check_id_valid``` returns ```False```.

### Task 8: Tackling the full dataset.
Now that we can detect invalid ID numbers, we can search the complete dataset to find all 10 invalid ID numbers. To do this, we will change the **filename** in the ```open``` function from ```"truncated_mangled_voters_roll_hre.csv"``` to ```"mangled_voters_roll_hre.csv"```. Be aware that there are 900301 lines in the complete dataset and the program may take a while to finish executing.

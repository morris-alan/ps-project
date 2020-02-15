# ps-project
Demo project 

## Introduction

In 2018 the Zimbabwe Electoral Commission released the full voters roll for the historic July harmonised elections, for the first time in 38 years the recently deposed dictator Robert Gabriel Mugabe would not appear on ballot, replaced by his former ally Emmerson Mnangagwa. Elections in Zimbabwe are steeped in a history of fraud, rigging and violence.

The original voters roll was, for a time, downloadable from this [website](https://zimelection.com/votersroll.php), as a disjointed collection of Microsoft excel(xlsx) documents. They contained detailed personal information on registered voters including names, phone numbers, addresses and National Identification numbers.

Today we will be searching a subsection of an altered version of the original voters roll(Harare Metropolitan area) for invalid or incorrectly captured national ID numbers. Within the provided data names have been mixed and the ID numbers are all fake, in addition there are only 3 columns - ID number, first names, surname. 

The goal of this exercise is to search the 900301 rows of fake registered voters and find the 10 planted invalid ID numbers.

## About the national ID number

A Zimbabwe National Identification number consists of 11 alpha numeric characters and is represented in the data as the following string of characters:

70-991814-P70

The first 2 digits represent the province where the ID was issued, the next 6 are unique identity digits. The first of the trailing 3 characters is always a capitol letter checkdigit, calculated from the previous 8 digits but not from the last 2 digits which loosely encode the ethnicity of the ID holder.

The checkdigit helps detect simple errors in the ID when humans manually input, transcribe or capture the ID. Such as hearing 17 in place of 70, switching 2 digits(9181 instead of 9981) or reading badly written characters incorrectly. for example

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
 


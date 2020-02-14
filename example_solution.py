"""
  Author: Alan Morris
  Creation date: 2020-02-09
  About : example solution for pluralsight interview project: Finding invalid fake ID numbers.
"""
import csv

def main():
    with open('data/truncated_mangled_voters_roll_hre.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if(not check_id_valid(row[0])):
                print(row[0])

def get_id_checkdigit(id_string):
    return(id_string[-3])

# String slicing will not return the full ID for id_strings with 7 middle digits.
def get_id_digits_incorrect(id_string):
    id_substring = id_string[:2] + id_string[3:9]
    return(int(id_substring))

def get_id_digits(id_string):
    id_parts = id_string.split("-")
    return(int(id_parts[0] + id_parts[1]))

def calculate_id_checkdigit(id_string):
    checkdigit_characters = "ABCDEFGHJKLMNPQRSTVWXYZ"
    checkdigit_index = get_id_digits(id_string) % 23 
    return(checkdigit_characters[checkdigit_index - 1])

def check_id_valid(id_string):
    return(calculate_id_checkdigit(id_string) == get_id_checkdigit(id_string))

if __name__ == "__main__":
    main()

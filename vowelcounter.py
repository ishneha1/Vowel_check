def get_vowels_count(input_string):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    vowels_in_input_string=[]
    for c in input_string:
        if c in vowels:
            vowels_count=+1
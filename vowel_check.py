'''def check_vowel(x):
    length=len(x)
    vowel_list=[]
    for i in range (0,length):
        v=x[i:i+1]
        if v == "a"or v=="e" or v=="i" or v=="o" or v=="u":
            vowel_list.append(v)
    return vowel_list

def main():
    sentence=input("enter a sentence:")
    program=check_vowel(sentence)
    print (program)

main()'''
def get_vowels(input_string):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    vowels_in_string=[]
    for c in input_string:
        if c in vowels:
            vowels_in_string.append(c)
    return vowels_in_string

def main():
    sentence=input("enter a sentence:")
    result=get_vowels
    print("the count of vowels alphabets are",result)
main()




    
def digit(str):
    r_str=""
    for ch in str.lower():
        if ch.isspace():#skips whitespaces
            continue
        r_str += ch
    r_str=r_str[::-1]#reverse  str
    if(r_str==str):
        print(str+" is a palindrome")
    else:
        print(str+" is not a palindrome")

str=input("Enter text to check it it is a palindrome: ")
digit(str)
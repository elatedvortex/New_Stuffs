# Challenge 2
## Challenge Description
```
Hmm, I WONDER WHAT A PYC FILE IS?
```
## <span style="color:aqua;">Analysis</span>
From the description given we know that its a compiled python file so I decompiled the python file and found the source code.
```
def modify_string(input_str):
    modified_str = ''
    for i in range(len(input_str)):
        char = input_str[i]
        if i % 2 == 0:
            modified_str += chr(ord(char) - 3)
            continue
        modified_str += chr(ord(char) + 2)
    
    return modified_str


def main():
    user_input = input('Enter a string: ')
    modified_input = modify_string(user_input)
    target_string = 'cn^ixelomkigaam{qjlp<Az'
    if modified_input == target_string:
        print 'Congratulations! You got the correct modified string.'
    else:
        print "Sorry, the modified string doesn't match the target."

if __name__ == '__main__':
    main()
```
We can see the program requests an input from the user and it modifies it in a certain way.<br>
* If the index of the string is odd then it converts the char into its respective ascii value using **ord** and then it adds 2 and then it converts back the value into a character using **char**.
* If the index of the string is even then it converts the char into its respective ascii value then it subtracts the value by 3 and converts it back into a character.

## <span style="color:Green;">Flag- flag{compiled_python??}</span>
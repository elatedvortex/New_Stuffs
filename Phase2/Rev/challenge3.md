# Challenge 3
## Challenge Description
```
wHat is thE paXword?
```
## <span style="color:aqua;">Analysis</span>
Like other rev challenges i used ghidra to find rev the file and see the source code but after looking at it a bit in the main function another function call. It agains calls another function which doesn't provide any information.
<br>
 Then I tried to analyze the **giveFlag()** code and there was an unknown variable that i couldn't find.
 <br>Then after looking around the writeups from other pentesters I found out that I can assign the value of a certain variable while running the programme, so I created a python file and assigned the value of **iVar1** to its required value at which it would give the flag.
 ```
 import subprocess

def variable_change(input_value):
    out= subprocess.run(['./conditional', str(input_value)])
    print(out.stdout)
variable_change(-0x35010ff3)
```
## <span style="color:Green;">Flag- flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}</span>
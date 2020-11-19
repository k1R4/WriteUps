# TODO

desc:
    On our victim's computer, there was some old script. It looks like someone left the message and the unfinished function used to read the content of that message.
    We have to obtain the message, could you do that?

We are given a python file with an encode and shift function along with a hashed string.
On inspection we see that the shift function just groups the first characters from left and right side of string, then second and so on.

The unshift function is quite simple, we group all chars in even places as first part of unshifted string and group all chars in odd places as second part.

```py
def unshift(msg):
    output1 = ''
    output2 = ''
    for i in range(len(msg)):
        if i%2 == 0:
            output1 += msg[i]
        else:
            output2 = msg[i] + output2
    
    output = output1 + output2 
    return output
```
The encode function reverses the string along with multiplying numbers in string to 4660 and converting the alphabetic characters to decimal multiplying by 16 and converting back to ASCII text.

simplified encode fn:
```py
def encode(msg):
    output = ''

    for i in range(len(msg)):
        temp = ord(msg[i])
        #temp = temp/16
        if 48 <= temp < 58: # if char is 0-9
            output = str(int(msg[i]) * 4660) + output
        else:
            output = chr(ord(msg[i]) * 16) + output

    return output
```

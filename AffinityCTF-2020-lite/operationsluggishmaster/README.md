# opperationsluggishmaster

This is an OSINT challenge. Two keywords are provided in the description: ```franciszekwarcislaw``` and ```operationsluggishhamster```

Searching these on google doesn't yield any valid results.
So we will be using a tool called sherlock which checks for usernames on various popular websites.
sherlock: https://github.com/sherlock-project/sherlock

Clone the sherlock repo and run the following commands:

```
➜  ~ cd sherlock/sherlock

➜  sherlock git:(master) python3 sherlock.py operationsluggishhamster
[*] Checking username operationsluggishhamster on:
[+] 500px: https://500px.com/p/operationsluggishhamster
[+] WordPress: https://operationsluggishhamster.wordpress.com/

➜  sherlock git:(master) python3 sherlock.py franciszekwarcislaw     
[*] Checking username franciszekwarcislaw on:
[+] 500px: https://500px.com/p/franciszekwarcislaw
[+] GitHub: https://www.github.com/franciszekwarcislaw
[+] Gravatar: http://en.gravatar.com/franciszekwarcislaw
[+] Strava: https://www.strava.com/athletes/franciszekwarcislaw
```

All links are garbage except: https://operationsluggishhamster.wordpress.com/ & https://www.github.com/franciszekwarcislaw

On the wordpress link, we find a clue asking us to mail Franciszek on his gmail.

On the github link, we find a repo called operationsluggishmaster. We find a GPG key in the repo. 
So we clone the repo and import the GPG key:

```
➜  ~ cd operationsluggishhamster 
➜  operationsluggishhamster git:(main) ✗ gpg --import pubkey.gpg
gpg: key 4E1EA49D6A7C6112: "Franciszek Warcislaw <franciszek.warcislaw@gmail.com>" not changed
gpg: key 4E1EA49D6A7C6112: "Franciszek Warcislaw <franciszek.warcislaw@gmail.com>" not changed
gpg: key 4E1EA49D6A7C6112: secret key imported
gpg: Total number processed: 2
gpg:              unchanged: 2
gpg:       secret keys read: 1
gpg:  secret keys unchanged: 1
```

After import we find out the gmail account mention in the wordpress blog. So we send a test mail to the gmail.
We recieve a bot reply that gives us:

```
This is my time for vacation! I will be back before 01.01.2021.

Ps. I do not work with hamsters anymore !

-----BEGIN PGP MESSAGE-----

hQGMA2aVem7Pudp2AQwAqacnAzr+8DyjtMN2qeDQO0RcpajT89WFLHl7f14csd+2
Ptp9aRfMNjIwbEnsayrrYXXHXxbUsAEeRq72S+L09OoTur5+S3y6ifkEs7AdhSOD
GLBKRaWyBWccH4cmBJILHN0/Cl+XhozVEdqt+rRf00Skvj20S0Az4pz6FFQueQ3Z
eZPRGLwVR17uVFBkSnYNvxKAZQn/ROEUSEFcp5Yo3ML9xZIkq0c9B1YwAcB1HZ8Y
YAyWwETvPipBu9d0aTESF82DlxTYcw+BItlnUfci3e56JlNTqYsXcEEhUKC6YLPe
s0o3mQrtjxLaQL/+ORDzg0yGEtV49PQyVGpyWNNnQSz5rrYtqtfiu7g4DljA55zR
XfPUnOMkpmFA3Bx91OcKLfTB6WK0LJ+NWvLvSh9XstW1FmpmpCQfd6+3QJXmEBwc
oA38DLHu/fFVSiUJtVpizVcMtkvZDaWjcLjEURN7LAakfJdFn5mUExEYTownmJrG
pTm0NoW/qlGi+mWa8oYG0sBzASsOrZA9zKI7lJBLP/OYotGWBS2We3Q4V4VAd501
G4a9ybo4o71JHxsOqkpi8PK5iEB5QIlBxbXGLNyyTJ7SqgIpSWRRZUdPJp/OXQNC
Ref03Jvx8BViV3zrEOkL/zX1AXL/jVzqz9S0SjnhcOzO4Bv2mxVNaClwcuYNhr3+
PQMYMyKfM0pQg6oID6q8OAPfO16tBZxnWEHgpMPqSRRnch0o0R+baMB+99VfkeRl
yC2eAwNsIHReJ17OwMY96o+O7aNeOvSfw61Xd+D1ZI+C4oUB58yLNecWAwYKIyzl
a0r+Tq5XfmVgAuxSqBMfP4KQbXC6aOvzgDr2cQHItScf7OmG4AAzZXtAG0Cvq3y4
rfOO+fptW/kiv9ZqvL7c0uQ8w3Pf7rRfMa9VvDd3oeZ8I1sFvg==
=NgAr
-----END PGP MESSAGE-----
```

We recieve a PGP message. So we can save this to a file called msg and decrypt it with the GPG key we imported earlier.

```
➜  ~ gpg --output doc --decrypt msg 
gpg: encrypted with 3072-bit RSA key, ID 66957A6ECFB9DA76, created 2020-11-11
      "Franciszek Warcislaw <franciszek.warcislaw@gmail.com>"
```

Inspecting the decoded message in the file doc we see that it is a PGP message. So we decrypt it again

```
➜  ~ gpg --output out --decrypt doc
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
```
Running this command prompts us with a passphrase which is: ```operationsluggishmaster```

Inspecting the file out we see that it is a https link: https://docs.google.com/document/d/1yXSpavYyF4ilTnFhvBSytf6UuMcDUPqQeCecIXCkUCU/edit

On visiting this link we see a google doc with three images and some text.
We see something interesting on the top right of the third image:

![emu](https://cdn.discordapp.com/attachments/778227191774707752/778276058087948308/image3.jpg)

Thats the flag!
Flag: ```AFFCTF{GuineaPigsAreTooBigForRunningWheels}```

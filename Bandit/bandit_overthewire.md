===Level 0 -> Level 1===
cmds:
    cat readme
    
output:
    boJ9jbbUNNfktd78OOpsqOltutMc3MY1

===Level 1 -> Level 2===
cmds:
    ls -A
    cat ./-
    
output:
    CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

===Level 2 -> Level 3===
cmds:
    cat spaces\ in\ this\ filename
    
output:
    UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

===Level 3 -> Level 4===
cmds:
    ls -A inhere/
    cat inhere/.hidden

output:
    pIwrPrtPN36QITSp3EQaw936yaFoFgAB

===Level 4 -> Level 5===
cmds:
    ls -A inhere/
    cat inhere/-file0x (-file07 contained flag)
   
output:
    koReBOKuIDDepwhWk7jZC0RTdopnAYKh

===Lvel 5 -> Level 6===
cmds:
    find inhere/ -readable -size 1033c
    cat inhere/maybehere07/.file2
    
output:
    DXjZPULLxYr17uwoI01bNLQbtFemEgo7

===Level 6 -> Level 7===
cmds:
    find / -size 33c -group bandit6 -user bandit7
    cat /var/lib/dpkg/info/bandit7.password
    
output:
    HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

===Level 7 -> Level 8===
cmds:
    grep "millionth*" data.txt 
    
output:
    cvX2JJa4CFALtqS87jk27qwqGhBM9plV

===Level 8 -> Level 9===
cmds:
    cat data.txt | sort | uniq -u

output:
    UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

===Level 9 -> Level 10===
cmds:
    strings data.txt | grep "====*"

output:
    truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

===Level 10 -> Level 11===
cmds:
    base64 -d data.txt

output:
    IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

===Level 11 -> Level 12===
cmds:
    cat data.txt|tr '[a-z]' '[n-za-m]'|tr '[A-Z]' '[N-ZA-M]'

output:
    5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

===Level 12 -> Level 13===
cmds:
   mkdir /tmp/zg1
   cp data.txt /tmp/zg1/
   xxd -r data.txt > uncomp
   file uncomp
   mv uncomp uncomp.gz
   gzip -d uncomp.gz
   file uncomp
   mv uncomp uncomp.bz
   bzip2 -d uncomp.bz
   file uncomp
   mv uncomp uncomp.tar
   tar -xf uncomp.tar
   ls
   file data5.bin
   mv data5.bin data.tar
   tar -xf data.tar
   ls
   file data6.bin
   mv data6.bin data.bz
   bzip2 -d data.bz
   file data
   mv data data2.tar
   tar -xf data2.tar
   ls
   file data8.bin
   mv data8.bin data.gz
   gzip -d data.gz
   file data
   cat data

output:
    8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

===Level 13 -> Level 14===
cmds:
    ssh -i sshkey.private bandit14@localhost
    cat /etc/bandit_pass/bandit14

output:
    4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

===Level 14 -> Level 15===
cmds:
    nc localhost 30000

output:
    BfMYroe26WYalil77FoDi9qh59eK5xNr

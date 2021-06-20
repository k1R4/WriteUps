#!/bin/bash
for i in {1000..1}
    do 
        tar -xvf "$i".tar
        echo "$i.tar extracted."
    done

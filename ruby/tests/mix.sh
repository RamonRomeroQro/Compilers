#!/bin/bash
for filename in ./*.rb; do
   
        cat "$filename" >> 9.rbb
        echo -e "\n\n" >> 9.rbb
    
done
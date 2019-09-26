#!/bin/bash
for filename in ./tests/*.rb; do
    python3 main_lexer.py "$filename"
done
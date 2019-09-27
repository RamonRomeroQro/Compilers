#!/bin/bash
for filename in ./test_set1/*.rb; do
    echo '>>>>>>>'  "$filename"
    python3 main_lexer.py "$filename"
    python3 main_parser.py "$filename"
done
#!/bin/bash
for filename in ./test_set1/*.rb; do
    echo -e "\n\n> TEST_CASE: " "$filename"
    
    echo -e "\n\n>>>" PARSER ERRORS
    python3 main_parser.py "$filename"
done
    echo -e "\n\n"--------------------------------
    echo -e "\n\n"********************************
    echo -e "\n\n"--------------------------------
    echo -e "\n\n"Sintactical Errors Test Cases
for filename in ./test_set2/*.rb; do
    echo -e "\n\n > TEST_CASE::" "$filename"
    
    echo -e "\n\n>>>" PARSER ERRORS
    python3 main_parser.py "$filename"
done
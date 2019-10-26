#!/bin/bash

echo -e --------------------------------
echo -e "\n\n"********************************
echo -e "\n\n"--------------------------------
echo -e "\n\n"Unit Tests

for filename in ./test_set1/*.rb; do
    echo -e "\n\n> TEST_CASE: " "$filename"
    echo -e "\n\n>>>" LEXER
    python3 main_lexer.py "$filename"
    echo -e "\n\n>>>" PARSER EVALUATION
    python3 main_parser.py "$filename"
done

echo -e "\n\n"--------------------------------
echo -e "\n\n"####################################################
echo -e "\n\n"--------------------------------
echo -e "\n\n"Sintactical EVALUATION Test Cases

for filename in ./test_set2/*.rb; do
    echo -e "\n\n > TEST_CASE::" "$filename"
    echo -e "\n\n>>>" LEXER
    python3 main_lexer.py "$filename"
    echo -e "\n\n>>>" PARSER EVALUATION
    python3 main_parser.py "$filename"
done

echo -e "\n\n"--------------------------------
echo -e "\n\n"####################################################
echo -e "\n\n"--------------------------------
echo -e "\n\n" SEGUNDA ENTREGA


for filename in ./test_set3/*.rb; do
    echo -e "\n\n > TEST_CASE::" "$filename"
    echo -e "\n\n>>>" LEXER
    python3 main_lexer.py "$filename"
    echo -e "\n\n>>>" PARSER EVALUATION
    python3 main_parser.py "$filename"
done


for filename in ./test_set4/*.rb; do
    echo -e "\n\n > TEST_CASE::" "$filename"
    echo -e "\n\n>>>" LEXER
    python3 main_lexer.py "$filename"
    echo -e "\n\n>>>" PARSER EVALUATION
    python3 main_parser.py "$filename"
done


for filename in ./test_set5/*.rb; do
    echo -e "\n\n > TEST_CASE::" "$filename"
    echo -e "\n\n>>>" LEXER
    python3 main_lexer.py "$filename"
    echo -e "\n\n>>>" PARSER EVALUATION
    python3 main_parser.py "$filename"
done

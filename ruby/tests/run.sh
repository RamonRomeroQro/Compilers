#!/bin/bash
for filename in ./*.rb; do
    ruby "$filename"
done
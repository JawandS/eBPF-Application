#!/bin/bash
counter=0
sudo when-changed tracking.txt 'echo $counter && counter=$((counter+1)) && echo "second print " && echo $counter';
echo $counter
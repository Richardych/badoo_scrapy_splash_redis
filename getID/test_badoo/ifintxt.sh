#!/bin/bash

num=`cat 'uidbadoo.txt' | grep "$1" | wc -l`
echo $num

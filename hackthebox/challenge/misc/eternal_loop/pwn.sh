#!/bin/bash 

#pass=`unzip -l 37366.zip | awk '{print $4}' | grep -o '[0-9]*\.zip' | grep -o '[0-9]*'`
#echo $pass
file=37366

for i in {1..501}
do
pass=`unzip -l ${file}".zip" | awk '{print $4}' | grep -o '[0-9]*'`
#echo $pass
unzip -o -P "$pass" "${file}.zip"
#:wrm ${file}".zip"
file=$pass
echo $i
done

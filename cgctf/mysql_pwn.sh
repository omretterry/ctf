#!/bin/bash


for i in {1019..1027}
do
	echo $i
	curl "http://chinalover.sinaapp.com/web11/sql.php?id=$i"
	echo "\n"
done

### id 1024.1

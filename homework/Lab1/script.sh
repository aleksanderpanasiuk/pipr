#!/bin/bash
find "$PWD" | grep -E '*\.h|*\.c' > fittingfiles.txt

for i in $( cat fittingfiles.txt);
do
	grep -E 'dragons' $i >> dragons.txt
done

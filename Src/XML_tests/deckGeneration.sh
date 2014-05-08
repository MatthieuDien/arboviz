#!/bin/bash

for ((i=1; 1000000-$i; i=$(($i+100))))
do
	echo "./bin/arbogen -min $i -max $(($i*10)) -type xml -file Deck/tree$i ../Src/Exemples/PSTL_mix.spec"
	./bin/arbogen -min $i -max $(($i*10)) -type xml -file Deck/tree$i ../Src/Exemples/PSTL_mix.spec >> resArbogen.txt
done
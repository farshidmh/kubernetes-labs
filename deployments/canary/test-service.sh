#!/bin/bash

for i in {1..20}; do
	echo -n $i
	curl  -s 172.16.0.78:30100/  | grep 'Welcome to Webapp'
done

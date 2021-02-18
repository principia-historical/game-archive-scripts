#!/bin/bash

for f in *.apk
do
	aapt dump badging $f > $f.yml
done


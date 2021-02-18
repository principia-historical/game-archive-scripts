#!/bin/bash

for f in *.apk
do
	echo "== $f =="
	sha256sum $f ../$1/apks/$f
	echo ""
done
	

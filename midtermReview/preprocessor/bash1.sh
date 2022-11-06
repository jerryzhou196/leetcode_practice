#!/bin/bash

for x in $(ls); do
        echo $(egrep "disco\." $x)
        echo ""
    done

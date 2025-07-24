#!/bin/bash

countToTwenty() {
  i=1
  while [ $i -le 20 ]
  do
    echo "Count: $i"
    ((i++))
  done
}

countToTwenty


# Challenge

#Create a simple while loop in bash that prints the numbers 1-20 to stdout.

#It should look like (stdout):

#Count: 1
#Count: 2
#...
#Count: 20



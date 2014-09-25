#!/usr/bin/env python
win = 0
win += 6/36.0
win += 2/36.0
print "first roll win", win

lose = 0
lose += 1/36.0
lose += 2/36.0
lose += 1/36.0
print "first roll lost", lose

point = 1
point -= win
point -= lose
print "first roll establishes a point", point

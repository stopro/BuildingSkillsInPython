#!/usr/bin/env python
x1,y1 = 2,3
x2,y2 = 6,8
m,b = float(y1-y2)/(x1-x2), y1-float(y1-y2)/(x1-x2)*x1
print "y=",m,"*x+",b

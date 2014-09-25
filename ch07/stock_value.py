#!/usr/bin/env python
shares = int (raw_input("Please input shares "))
dollar = int (raw_input("Please input dollar price "))
eighth = float (raw_input("Please input number of 8th "))
value = shares * (dollar + eighth/8.0)
print "Your own stock values: ", value

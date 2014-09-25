#!/usr/bin/env python
principal = float (raw_input("Input principal:"))
percentage = float (raw_input("Input annual percentage:"))
payments = int (raw_input("Input number of payments:"))
percentage /= 12
payments *= 12

mpay = principal * ( percentage / ( 1 - pow((1 + percentage), (0 - payments))))
print mpay

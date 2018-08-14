#!/bin/env python

def checkPrime(number):
  isPrime = True
  for i in range(2, number):
    if number % i == 0:
      isPrime = False
      break
    else:
      pass
  return isPrime

def primeFactory(min, max):
  for i in range(min, max):
    # print checkPrime(i)
    if checkPrime(i):
      # print '========' + str(i)
      total = 0
      for letter in str(i):
        total = total + int(letter)
      if checkPrime(total): 
        print(i)

# print checkPrime(2)
primeFactory(1000000,10000000)
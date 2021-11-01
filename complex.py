# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 20:33:13 2021

@author: Grant Huang
"""

import math

#class for complex numbers
class Complex:
    #constructor
    #@param realpart - number for real number part
    #@param imagpart - number for imaginary part
    def __init__(self, realPart=0, imagPart=0):
        self.__real = realPart
        self.__imag = imagPart
        self.__angle = Complex.calculateAngle(self.__real, self.__imag)
        self.__magnitude = abs(self)
      
    #creates string from complex number
    #returns string of the form a + bi. removes terms with 0 coefficients.
    def __str__(self):
        a = self.__real
        b = self.__imag
        imagStr = ""
        
        #figuring out imaginary string
        if b == 0:
            imagStr = ""
        elif b == 1:
            imagStr = "i"
        elif b == -1:
            imagStr = "-i"
        else:
            imagStr = str(b) + "i"
            
        #combining parts to make string
        if imagStr == "":
            return str(a)
        elif a == 0:
            return imagStr
        elif b > 0:
            return str(a) + "+" + imagStr
        else:
            return str(a) + imagStr
            
    #adds 2 complex numbers together
    #@param z - complex number being added
    #returns sum of this number and z
    def __add__(self, z):
        #a + bi + c + di = (a + b) + (c + d)i
        return Complex(self.__real + z.__real, self.__imag + z.__imag)
    
    #subtracts 2 complex numbers
    #@param z - complex number being subtracted
    #returns difference between this number and z
    def __sub__(self, z):
        #a + bi - (c + di) = (a - c) + (b - d)i
        return Complex(self.__real - z.__real, self.__imag - z.__imag)
    
    #multiplies this complex number with another
    #@param z - complex number being multiplied
    #returns product of this number and z
    def __mul__(self, z):
        #(a + bi)(c + di) = ac + adi + bci - bd = (ac - bd) + (ad + bc)i
        a = self.__real
        b = self.__imag
        c = z.__real
        d = z.__imag
        
        return Complex(a*c - b*d, a*d + b*c)
    
    #divides this complex number with another
    #@param z - complex divisor
    #returns this number divided by other number
    def __truediv__(self, z):
        #(a + bi)/(c + di) = (a + bi)(c - di)/(c^2 + d^2)
        a = self.__real
        b = self.__imag
        c = z.__real
        d = z.__imag
        
        numerator = Complex(a, b)*Complex(c, -d)
        print("numerator" + str(numerator))
        denominator = c**2 + d**2
        print("denominator" + str(denominator))
        return Complex(numerator.__real/denominator, numerator.__imag/denominator)
        
    #calculates absolute value
    # returns absolute value of complex number as real number
    def __abs__(self):
        a = self.__real
        b = self.__imag
        
        return math.sqrt(a**2 + b**2)
    
    #finds square root of a complex number
    #@param z - complex number
    #returns positive root of complex number
    @staticmethod
    def squareRoot(z):
        #square root of -1 is i
        if z.__imag == 0:
            a = z.__real
            return Complex(0, math.sqrt(-a)) if a < 0 else Complex(math.sqrt(a))
        
        root = Complex()
        root.__magnitude = math.sqrt(z.__magnitude)
        root.__angle = z.__angle/2
        root.__updateRectCoord()
        
        return root
    
    #finds nth power of complex number
    #@param n - complex exponent
    #finds nth power of this number
    def __pow__(self, n):
        exp = Complex(n).__real
        product = Complex()
        
        product.__magnitude = self.__magnitude**exp
        product.__angle = self.__angle*exp
        product.__updateRectCoord()
        return product
    
    #finds square of complex number
    #@param z - complex number
    #returns square of z
    @staticmethod
    def square(z):
        return z*z
    
    #finds cube of comples number
    #@param z - complex number
    #returns cube of z
    @staticmethod
    def cube(z):
        return z*z*z
    
    #figures out the polar coordinate angle of a standard form complex number
    #@param a - real part of complex number
    #@param b - imaginary part of complex number
    #returns radian polar angle on inputed complex number
    @staticmethod
    def calculateAngle(a, b):
        return math.atan2(b, a)

    #updates rectangular coordinates based on polar coordinates
    def __updateRectCoord(self):
        self.__real = self.__magnitude*math.cos(self.__angle)
        self.__imag = self.__magnitude*math.sin(self.__angle)
        
    #updates polar coordinates based on rectangular coordinages
    def __updatePolarCoord(self):
        self.__angle = complex.calculateAngle(self.__real, self.__imag)
        self.__magnitude = abs(self)
    
   

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
        b = float(self.__imag)
        imagStr = ""
        
        #figuring out imaginary string
        if b == 0:
            imagStr = ""
        elif b == 1:
            imagStr = "i"
        elif b == -1:
            imagStr = "-i"
        else:
            imagStr = str(int(b)) + "i" if b.is_integer() else "i" + str(b)
            
        #combining parts to make string
        if imagStr == "":
            return str(a)
        elif a == 0:
            return imagStr
        elif b > 0:
            return str(a) + "+" + imagStr
        else:
            return str(a) + imagStr
        
    #returns number multiplied by -1
    def __neg__(self):
        return Complex(-self.__real, -self.__imag)
            
    #adds 2 complex numbers together
    #@param z - complex number or real number being added
    #returns sum of this number and z
    def __add__(self, z):
        addend = z if isinstance(z, Complex) else Complex(z)
            
        #a + bi + c + di = (a + b) + (c + d)i
        return Complex(self.__real + addend.__real, self.__imag + addend.__imag)
    
    #adds 2 complex numbers together
    #@param z - complex number or real number being added
    #returns sum of this number and z
    def __radd__(self, z):
        return self + z
    
    #subtracts 2 complex numbers
    #@param z - complex number or real number being subtracted
    #returns difference between this number and z
    def __sub__(self, z):
        number2 = z if isinstance(z, Complex) else Complex(z)
        
        #a + bi - (c + di) = (a - c) + (b - d)i
        return Complex(self.__real - number2.__real, self.__imag - number2.__imag)
    
    #subtracts 2 complex numbers
    #@param z - complex number or real number being subtracted
    #returns difference between this number and z
    def __rsub__(self, z):
        return -self + z
    
    #multiplies this complex number with another
    #@param z - complex number being multiplied
    #returns product of this number and z
    def __mul__(self, z):
        number2 = z if isinstance(z, Complex) else Complex(z)
        
        #(a + bi)(c + di) = ac + adi + bci - bd = (ac - bd) + (ad + bc)i
        a = self.__real
        b = self.__imag
        c = number2.__real
        d = number2.__imag
        
        return Complex(a*c - b*d, a*d + b*c)
    
    #multiplies 2 numbers
    #z - some number
    #return product of this complex number and z
    def __rmul__(self, z):
        return self*z
    
    #divides this complex number with another
    #@param z - complex divisor
    #returns this number divided by other number
    def __truediv__(self, z):
        number2 = z if isinstance(z, Complex) else Complex(z)
        
        #(a + bi)/(c + di) = (a + bi)(c - di)/(c^2 + d^2)
        a = self.__real
        b = self.__imag
        c = number2.__real
        d = number2.__imag
        
        numerator = Complex(a, b)*Complex(c, -d)
        denominator = c**2 + d**2
        realQuotient = numerator.__real/denominator
        imagQuotient = numerator.__imag/denominator
        return Complex(realQuotient, imagQuotient)
    
    #divides 2 complex numbers
    #z - some number
    #returns z divided by this complex number
    def __rtruediv__(self, z):
        return Complex(z)/self
        
    #calculates absolute value
    # returns absolute value of complex number as real number
    def __abs__(self):
        a = self.__real
        b = self.__imag
        
        return math.sqrt(a**2 + b**2)
     
    #finds nth root of complex number
    #@param n - positive integer root
    #@param z- complex or real number
    @staticmethod
    def nthRoot(n, z):
        radicand = z if isinstance(z, Complex) else Complex(z)
        exp = 1/n
        
        #even root
        if  n%2 == 0:
            a = radicand.__real  
            
            #determining power
            if n%2 == 0 and a < 0:
                return  Complex(0, (-a)**exp)
            else:
                return Complex(a**exp)
        
        root = Complex()
        root.__magnitude = radicand.__magnitude**exp
        root.__angle = radicand.__angle/n
        root.__updateRectCoord()
        
        return root
    
    #finds square root of a complex number
    #@param z - complex or real number
    #returns positive root of complex number
    @staticmethod
    def squareRoot(z):
        return Complex.nthRoot(2, z)
    
    #finds cube root of complex number
    #@param z - complex or real number
    #returns primary cube root of z
    @staticmethod
    def cubeRoot(z):
        return Complex.nthRoot(3, z)
    
    #finds nth power of complex number
    #@param n - complex exponent
    #finds nth power of this number
    def __pow__(self, n):
        product = Complex()
        
        product.__magnitude = self.__magnitude**n
        product.__angle = self.__angle*n
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
        
    #rounds number to the nearest number of inputed decimal places
    #z - complex number
    #n - number of decimal places to round to
    @staticmethod
    def roundComplex(z, n=0):
        roundedReal = round(z.__real, n)
        roundedImag = round(z.__imag, n)
        return Complex(roundedReal ,roundedImag)
    
   

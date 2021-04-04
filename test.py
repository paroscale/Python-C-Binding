import ctypes
import os 
import numpy
#give whole .so path here 
testlib = ctypes.cdll.LoadLibrary('/home/ashwini/Documents/PythonProject/ArrayCtypes/test.so')

n=5
outa = numpy.zeros(n,numpy.float)
ina = numpy.linspace(1.0,200.0,n)

print("initial array",ina)
testlib.square_array.restype = None
testlib.square_array(ctypes.c_int(n),
                     numpy.ctypeslib.as_ctypes(ina),
                     numpy.ctypeslib.as_ctypes(outa))
print ("final array",outa)
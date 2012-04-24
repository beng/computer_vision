import numpy, sys, time, itertools, scipy.signal, scipy.ndimage

###################################################################
"""
@file    convolve.py
@author  Ben Gelb
@email   beg5670@gmail.com

Convolution in python using yield and chain
to speed up the unpacking of the matrix. 

Messed around with 0 padding on the kernel, 
but didn't get much better results

Naive 2D convolution can be done using 4, nested for loops, which is 
significantly inefficient.

An additional way to do 2D convolution is to use separable
matrices, which is faster than naive 2D convolution because 
the naive approach requires M*N multiplications opposed to
M+N multiplications, BUT since the kernel is so small and 1D there is no
need to.
"""
###################################################################

'''
yields a list of the convolution matrix 

itertools signifcantly increases the unpacking time
of the result

able to see the results being processed in real-time opposed
to just using return and waiting for the results to be calculated 
and then be printed out at once.
'''
def convolve(matrix, kernel):
    # use convolve. works very fast on a small kernel (fft too slow on this size)
    # use chain and yield to significantly speed up unpacking of list
    yield list(itertools.chain(*(scipy.signal.convolve(matrix, kernel, mode='same'))))

'''
yields a list of the convolution matrix using the
ndimage.convolve function in scipy. this was used
to experiment with speed differences compared to signal.convolve
'''
def convolve_using_ndimage(matrix, kernel):
    # VERY SLOW
    # used for comparison!
    yield list(itertools.chain(*(scipy.ndimage.convolve(matrix, kernel, mode='same'))))

'''
returns a matrix with dimensions(w,h) 

fills it with random data
'''
def create_matrix(w,h):
    return numpy.random.random((w,h))

'''
returns an array with the designated values
'''
def create_kernel():
    return numpy.asarray([[-1,0,1]])

'''
returns current system time
'''
def current_time():
    return time.time()

'''
returns total time between 2 points
'''
def total_time(t0, t1):
    return t1 - t0

'''
runs the program
'''
def run(w, h):
    # cant nest function calls otherwise timing is signifcantly off
    # e.g. convolve(create_matrix(w,h), create_kernel()) takes significantly longer
    # for obvious reasons
    m = create_matrix(w,h)
    k = create_kernel()
    t0 = current_time()
    result = convolve(m,k)
    t1 = current_time()
    
    # unpack result
    for i in result:
        print i

    print '\nTotal execution time :: ', total_time(t0,t1), '\n'
  
'''
parse command line arguments and call run
'''  
def main(args):
    try:
        width = int(args[0])
        height = int(args[1])
        run(width, height)
    except ValueError:
        usage()
        
'''
how to run the program
'''                
def usage():
    sys.exit("Usage: python convolve.py <width> <height>")
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    main(sys.argv[1:])

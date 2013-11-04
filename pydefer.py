#!/usr/bin/env python
# coding: utf-8
#
# 2013-11-04 @skyblue
#
# module(pydefer) implements golang-defer in python
#
# How to use
# add @godefer.wrapper to each function
# call pydefer.defer(func, *args, **kwargs)
#

__chain = []
def wrapper(func):
    def funcNew(*args, **kwargs):
        err = None
        try:
            result = func(*args, **kwargs)
        except Exception, e:
            err = e

        # call defer chain
        while len(__chain) > 0:
            f, args, kws = __chain.pop()
            try:
                f(*args, **kws)
            except:
                pass
        
        if err != None:
            raise err
        return result
    return funcNew

def defer(func, *args, **kwargs):
    __chain.append((func, args, kwargs))


def printf(fmt, *args):
    ''' printf(format, args...) '''
    print fmt % args
    
def println(*args):
    print ' '.join(args)

if __name__ == '__main__':
    @wrapper
    def hello(name):
        print 1
        print 2
        defer(printf, 'defer 5')
        def hi(name = 'sx'):
            defer(printf, 'defer 4')
            print 'hi', name
        hi('ss')
        print 3
        print 'hello', name        
    defer(printf, "defer main")
    hello('mei zi')

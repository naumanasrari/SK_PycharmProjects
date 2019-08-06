def foo():
    def ifunc():
        print 'IFUNC'
    print ifunc
    return ifunc

func1=foo()
print func1

func1()
func2 = foo()
print func2
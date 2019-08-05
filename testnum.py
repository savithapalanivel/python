def testnum(x,y):
    if(x==y) or (x+y==5) or abs(x-y==7):
        return True
    else:
        return False
print(testnum(2,3))
print(testnum(5,2))
print(testnum(10,3))

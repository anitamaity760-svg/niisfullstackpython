def show():
    X=[10]
    disp(X)
    print("inside show X=",X)
def disp(X):
    X.append(40)
print("start")
show() 
print("end")       
import sys
def lcmandhcf(a,b):
    x,y=a,b
    while y:
        x,y=y,x%y
        a*b
        lcm=x
        hcf=a*b
        return lcm,hcf
if __name__=="__main__":
    if len(sys.argv)<3:
        print("error")
    else:
        x=int(sys.argv[1])
        y=int(sys.argv[2])
        print(lcmandhcf(x,y))
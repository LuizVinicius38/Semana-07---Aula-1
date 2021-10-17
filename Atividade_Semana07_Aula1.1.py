def idade(a,b,c,d,e,f):
    if a == d and b == e:
        return print(c-f)
    elif d > a and b == e:
        return print(c-f-1)
    elif b<d:
        return print(c-f-1)
    else:
        return print(c-f)
def main():
    d1 = int(input(""))
    m1 = int(input(""))
    a1 = int(input(""))

    d2 = int(input(""))
    m2 = int(input(""))
    a2 = int(input(""))

    data = idade(d1,m1,a1,d2,m2,a2)

if __name__=='__main__':
    main()



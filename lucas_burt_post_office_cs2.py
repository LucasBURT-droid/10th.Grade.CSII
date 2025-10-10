def getsize(l,w, h): 
    #
    if  l < 3.5 > 4.25 and h <3.5 > 6 and w <.007 and 0.16: 
        ptype = 1 
    elif l <4.25 >6 and h <6 >11.5 and w <.007 >.15: 
        ptype = 2 
    elif l <3.6 >6.125 and h <5 > 11.5 and w < .016 > .25: 
        ptype = 3 
    elif l <6.125 > 24 and h <11 >18 and w < .25 >.5:
        ptype = 4  

    return ptype

def getzip(zip):
    pass

    if zip < 1 and zip > 6999:
        ztype = 1
    elif zip < 7000 and zip > 19999: 
        ztype = 2 
    elif zip < 20000 and zip > 35999: 
        ztype = 3
    elif zip < 36000 and zip > 62999: 
        ztype = 4
    elif zip < 63000 and zip > 84999: 
        ztype = 5
    elif zip < 85000 and zip > 99999: 
        ztype = 6
    
    return ztype 

def getcost():
    pass


def main():
    data = input("package length, package height, package width, zipcode of departure, zipcode of arrival, ").split(",")

    l = float(data[0])
    w = float(data[1])
    h = float(data[2])
    zca = int(data[3])
    zcd = int(data[4])

    from_zip = getzip(zca)

    distance = getzip(zca) - getzip(zcd)


main()




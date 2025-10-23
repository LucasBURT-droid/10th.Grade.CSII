'''
Author: Lucas Burt 
Description: calculates the postage cost for different types of mail based on their dimensions and post codes, classifying items into diffrent catagories 
Bugs: Unmailable ptype does not always print "unmailable"
Sources: Google
Dates: 10.22.25
Features: 4 unique functions to classify mail by size, calculates postage by class and zones, flags unmailable items, rounds costs to 2 decimals.
Log: 1.1 

'''

def getsize(l,w,h): 
    
    '''
    description - takes in the user input dimensions, classifys them into diffrent types.
    args - l: length w: width h: hieght 
    returns- specific package type based on user input
    '''
    ptype = ""
    if  l > 3.5 and l < 4.25 and h > 3.5 and h < 6 and w >.007 and w < 0.16:                #Reg post card                                  
        ptype = 1 
    elif l > 4.25 and l < 6 and h >6 and h <11.5 and w >.007 and w  <.15:                   #Large post card
        ptype = 2 
    elif l > 3.6 and l <6.125 and h >5 and h < 11.5 and w > .016 and w < .25:               #Envelope 
        ptype = 3 
    elif l > 6.125 and l < 24 and h > 11 and h < 18 and w > .25 and w <.5:                  #Large Envelope 
        ptype = 4  
    elif l + w + h > 84 and l + w + h < 130:                                                #Package
        ptype = 5 
    elif l + h + h + w + w > 84 <= 130:                                                      #Large Package
        ptype = 6  
    elif l + w + h > 130:                                                             # Too large
        ptype = -1 
    else:                                                                                   #Unmailable 
        ptype = -1 
        
    return ptype 
def getzip(zip):

    '''
    description - gets the  zipcode based on the inputs of user (classifying into diffrent groups/zones)  
    args - zip: zip code (int) of either the origin or destination.
    returns- integer from 1-6 based on the zones 
    
    '''
    ztype = 0

    if zip > 1 and zip < 6999:
        ztype = 1
    elif zip > 7000 and zip < 19999: 
        ztype = 2 
    elif zip > 20000 and zip < 35999: 
        ztype = 3
    elif zip > 36000 and zip < 62999: 
        ztype = 4
    elif zip > 63000 and zip < 84999: 
        ztype = 5
    elif zip > 85000 and zip < 99999: 
        ztype = 6
    
    return ztype 

def getcost(ptype, ztype): 
    
    '''
    description - calculates  the  cost  based on the package type and postal zone.
    args - ptype: package type, ztype: zipcode zone 
    returns- float: cost of package in $  
    '''
    #price = 0 
    
    if ptype == 1: 
        return (.20 + 0.03 * ztype)
    elif ptype  == 2: 
        return (.37 + 0.03 * ztype )
    elif ptype  == 3: 
        return (.37 + 0.04 * ztype )
    elif ptype  == 4: 
        return (.60 + 0.05 * ztype) 
    elif ptype  == 5: 
        return (2.95 + 0.25 * ztype)
    elif ptype  == 6: 
        return( 3.95 + 0.35 * ztype) 
    elif ptype == -1:
        print("UNMAILABLE")

def main():
    counter = 0 
    while counter <5:                               #Loop runs up to 5 times                                                                                                                   
        data = input("package length, package height, package width, zipcode of departure, zipcode of arrival, ").split(",")

        l = float(data[0])
        w = float(data[2])
        h = float(data[1])
        zca = int(data[3])                  #from
        zcd = int(data[4])                  #to
        from_zip = getzip(zca)
        to_zip = getzip(zcd)

        ztype = abs(to_zip-from_zip)
        ptype = getsize(l,w,h)
        price = getcost(ptype,ztype)
        print(price) 
    counter = counter+1                     #adds +1 to counter until it hits 5 

main()



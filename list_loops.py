from argparse import Namespace


temperatures=[9,15,23,28,30,33] # 0=9 array starts from 0
print (len(temperatures)) # how many items inside "temperatures"
print (temperatures[:3]) # :3 slicing the first three array items
print (temperatures[4:]) # 4: slicing from the 4th array item
print (temperatures[-3:]) # - means starting from behind


print ("--------------------------")
for item in temperatures:
    print (item)
    if item %2==0:       
        print ("even") # to make calculation
    else:
        print ("uneven")
        
print ("--------------------------")
names=["tina","tommy"]
for i in range (2):
    print (i) 
    print (names[i])
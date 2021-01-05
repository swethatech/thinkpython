#type  (chapter-2)

'''width = 17
height = 12.0
delimiter = '.'


width=width/2
width2=width/2.0
height=height/3
num=1 + 2 * 5
delimiter=delimiter * 5
print("width",type(width))
print("width2",type(width2))
print("height",type(height))
print("num",type(num))
print("delimiter",type(delimiter))




#formula
r=5
sum=(4/3)*3.14*r*r*r
sum1=int(input("enter the sum value:"))
if (sum1==523.3333333333334):
    print("{} is correct".format(sum1))
else:
    print("{} is wrong!".format(sum1))






#bookcost
bookCost = 24.95
numBooks = 60.0

def cost(numBooks):
   bulkBookCost = ((bookCost * 0.60) * numBooks)
   shippingCost = (3.0 + (0.75 * (numBooks - 1)))
   totalCost = bulkBookCost + shippingCost
   print('The total cost is: $', totalCost)

cost(numBooks)





#datetime
import datetime
from datetime import timedelta

startTime = datetime.datetime(2011,1,1, 6, 52, 0)
timeSec = (((8.0 * 60.0) + 15.0) * 2.0) + (((7.0 * 60.0) + 12.0) * 3.0)
timeMin = timeSec / 60.0
timeSpent = datetime.timedelta(minutes=38, seconds=6)
finalTime = startTime + timeSpent

print('You get home at: ', finalTime)'''




# Here are the test scores of 10 students in physics and history:
# 
# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15
# 
# Compute the slope of the line of regression obtained while treating Physics as the independent variable. Compute the answer correct to three decimal places.

import math
x= [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y= [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
a=sum(x)/len(x)
b=sum(y)/len(y)
l1=[i-a for i in x]
l2=[i-b for i in y]
l3=[i*j for i,j in zip(l1,l2)]
l4=[i*i for i in l1]
print("%0.3f"%(sum(l3)/sum(l4)))

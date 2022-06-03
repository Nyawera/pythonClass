# x = 90
# if x > 90:
#     print("A")
#   elif x ==80 and x <=90:
#         print("B")
#         elif x ==60 and x <=79
#         print("c")

x = 0
price=int(input("Enter the price of bike"))
if price > 100000:
     tax = 15/100*price
elif price >50000 and price <=100000:
     tax = 10/100*price
else:
     tax = 5/100*price
print("Tax to be paid ",tax)





 
 
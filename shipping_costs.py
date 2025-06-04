#Change the weight value to any nnumber
weight = 50

#Ground Shipping Costs
if weight <= 2:
  price = weight * 1.50 + 20.00
  print ("Price: $" + str(price))

elif weight >= 2 and weight <= 6:
  price = weight * 3.00 + 20.00
  print ("Price: $" + str(price))

elif weight >= 6 and weight <= 10:
  price = weight * 3.00 + 20.00
  print ("Price: $" + str(price))

else:
  price = weight * 3.00 + 20.00
  print ("Price: $" + str(price))

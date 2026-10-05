price = float(input("enter unit price: "))
stock = int(input("enter avaible stock: "))
quantity = int(input("enter requested quantity: "))
member = input("Is the cutomer a member? (yes or no ): ").lower()
if quantity <=0:
  print("rejected: invalid quantity")
elif quantity > stock:
  print("rejected: insufficient stock")
else:
  total = price * quantity
  if member == "yes" and total >= 500:
    total = total * 0.9 
    print("approved: discount applied")
  else:
    print("approved: no discount")
  print(f"final price : {total:.2f}")
    

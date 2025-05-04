# Build a simple bill calculator for a grocery store: Ask for item prices and quantities, apply 18% GST, and show the total bill.
noGstPrice = 0
for i in range(1,4):
    prices = float(input(f"Price of the item {i} : "))
    quantities = int(input(f"Enter the quantity of items {i} :"))
    noGstPrice += prices*quantities


gstPrice = noGstPrice * 0.18
final_Amount = noGstPrice + gstPrice
print("Your bill!")

print("\nTotal(without GST) :", noGstPrice)
print("\nGST 18% :", gstPrice)
print("\nTotal (with GST) :", final_Amount)
print("\nThank you for visiting!")
print("Pleaase visit again!")

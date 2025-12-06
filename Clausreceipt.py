fast = 10
slow = 0
premium = 7
normal = 0
price = 15
email = input("email MANDATORY: ") 
speed = input("delivery(fast OR slow): ")
coding = input("premium OR normal: ")
print("NOW ON YOUR COMPUTER YOU CAN FIND A FILE ON YOUR PC CALLED: ")
print("Claus_receipt.txt")

if speed == "fast":
    price = price + fast

if coding == "premium":
    price = price + premium


with open("Claus_receipt.txt", "w") as file:
    file.write("=== Claus(TM) Receipt ===\n")
    file.write("--------------------------\n")
    file.write(f"User EMAIL: {email}\n")
    file.write(f"Delivery speed: {speed}\n")
    file.write(f"Code option: {coding}\n")
    file.write(f"TOTAL PRICE: {price}\n")
    file.write("--------------------------\n")
    file.write("=== Thanks for ordering from CLAUS ===\n")
    file.write("SEND THIS FILE TO help@claus.tr\n")

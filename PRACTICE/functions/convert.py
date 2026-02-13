print("program for converting USD to INR")
num = float(input("Enter the amount in USD : "))
def convert(usd_amount):
    exchange_rate = 90.63
    inr_value = exchange_rate * usd_amount
    return inr_value
result = convert(num)
print("INR value of the USD is : ", result)
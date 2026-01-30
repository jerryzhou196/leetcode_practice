# {"james,10,sf", "bonnie,50,ny", "james,30,ny"}

# count = {
# james: {10: ['sf'], 30: ['ny']} 
# bonnie: {50: ['ny']}
# }

for transaction in transactions: 
    ans = []
    name, amount, city = transaction.split(",")
    for i in range(amount - 60, amount + 61): 
        if i in count[]

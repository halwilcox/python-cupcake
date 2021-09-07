open_file = open("CupcakeInvoices.csv")

sum = 0

total_sales =[]
for line in open_file:
    line = line.rstrip('\n').split(",")
    print (line)
    print(line[2])
    quantity = float(line[3])
    price = float(line[4])
    print(quantity * price)
   # total_sales.append(quantity * price)
    sum += (quantity * price)


#done = sum(total_sales)
print(sum)
#Float-method
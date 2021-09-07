open_file = open("CupcakeInvoices.csv")

for line in open_file:
    line = line.rstrip('\n').split(",")
    print(line)

#for line in open_file:
 #   line= line.rstrip('\n').split(",")
  #  print(line[2])
def extract_bill(line1): # function for extracting bill number
	bill = ""
	#print "bill" + line1
	for i in range(0, len(line1)):
		if(line1[i].lower() == "b"):
			if(line1[i+1] == "i"):
				if(line1[i+2] == "l"):
					if(line1[i+3] == "l"):
						j = i + 6
						for p in range(0, 8):
							bill = bill + line1[j+p]
						break
	return bill

def extract_da_ti(line2): # function for extracting date and time
	date = ""
	time = ""
	#print "dt" + line2
	if len(line2) >= 34:
		for i in range(0, len(line2)):
			if(line2[i].lower() == "d"):
				if(line2[i+1] == "a"):
					if(line2[i+2] == "t"):
						if(line2[i+3] == "e"):
							j = i + 7
							for p in range(0, 10):
								date = date + line2[j+p]
						
			elif(line2[i].lower() == "t"):
				if(line2[i+1] == "i"):
					if(line2[i+2] == "m"):
						if(line2[i+3] == "e"):
							j = i + 6
							for p in range(0, 8):
								time = time + line2[j+p]
							break
	return (date, time) 

def extract_product(text_file, csv_file, line3, bill, date, time): # function for extracting the product details
	description = ""
	quantity = ""
	rate = ""
	amount = ""
	my_file = open(csv_file, "a")
	#print "pro" + line3

	for i in range(0, len(line3)):
		if line3[i] == "-":
			if line3[i+1] == "-":
				my_file.close()
				return
		else:
			if i < 12:
				description = description + line3[i]
			elif i > 11 and i < 19:
				quantity = quantity + line3[i]
			elif i > 18 and i < 29:
				rate = rate + line3[i]
			elif i > 28 and i <= len(line3):
				 amount = amount + line3[i]
	else:
		#print description
		if description != "Description " and bill != "":
			my_file.write(bill + "," + date + "," + time + "," + description + "," + quantity + "," + rate + "," + amount)
		line3 = text_file.readline()
		extract_product(text_file, csv_file, line3, bill, date, time)		



def bill_extract(file_name, csv_file):
	text_file = open(file_name, "r") # opening the file

	while True:
		line1 = text_file.readline() # reads the first line of the file

		while line1[0] != "\x0f":  # reads the next lines till it encounters the line containing bill number
			line1 = text_file.readline()

		line1 = text_file.readline()	
	
		if line1[1].lower() != "p":
			line1 = text_file.readline()

		bill = extract_bill(line1)

		line2 = text_file.readline()

		date, time = extract_da_ti(line2)

		line3 = text_file.readline() # reads ------
		line3 = text_file.readline() # reads description qty rate amount
		line3 = text_file.readline() # reads --------
		line3 = text_file.readline() # reads the products line

		extract_product(text_file, csv_file, line3, bill, date, time)

		line1 = text_file.readline()
		
		if line1[0].lower() == "v":
			if line1[1] == "-":
				if line1[2].lower() == "c":
					if line1[3].lower() == "a":
						if line1[4].lower() == "r":
							if line1[5].lower() == "d":
								break
		if line1[0].lower() == "c":
			if line1[1].lower() == "a":
				if line1[2].lower() == "s":
					if line1[3].lower() == "h":
						break
	return


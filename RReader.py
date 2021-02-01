import csv 
import crypt






with open("testpw.csv") as passwords:
	reader = DictReader(passwords)
	for row in reader:
		salt_sha512 = crypt.crypt(row, crypt.mksalt(crypt.METHOD_SHA512))
		writer = csv.DictWriter(open("rainbow.csv")
		writer.writerow(salt_sha512)

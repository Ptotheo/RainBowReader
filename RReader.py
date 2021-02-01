import csv 
import crypt









with open("testpw.csv") as passwords:
	for line in passwords:
		salt_sha512 = crypt.crypt(line, crypt.mksalt(crypt.METHOD_SHA512))
		writer = csv.writer(open("rainbow.csv" , "w"))
		writer(salt_sha512.append())





		
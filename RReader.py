import csv 
import crypt






with open("testpw.csv") as passwords:
	for row in passwords:
		salt_sha512 = crypt.crypt(row, crypt.mksalt(crypt.METHOD_SHA512))


with open('rainbow.csv', 'w', newline='') as rainbow:
    fieldnames = ['password', 'hash']
    writer = csv.DictWriter(rainbow, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(f'password: {row}, hash: {salt_sha512}')

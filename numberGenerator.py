with open('numbers.txt', 'w') as writefile:
	for x in range(99999):
		if x < 10 and x > 0:
			writefile.write('000000'+str(x)+'\n')	
		if x < 100 and x > 9:
			writefile.write('00000'+str(x)+'\n')	
		if x < 1000  and x > 99:
			writefile.write('0000'+str(x)+'\n')	
		if x < 10000 and x > 999:
			writefile.write('000'+str(x)+'\n')	
		if x < 100000 and x > 9999:
			writefile.write('00'+str(x)+'\n')	
	writefile.write('0099999')
		
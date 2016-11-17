with open("countries.txt", "r") as ins:
    f = open('myfile','w')
    array = []
    i = 0
    for line in ins:
		f.write(line.replace(' ','_').upper().rstrip()+': setProp('+str(i)+',\''+line.rstrip()+'\' , { translate: false}) ,\n')
		i+=1
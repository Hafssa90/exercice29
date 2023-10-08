pmarrakech = 1000000           
pagadir = 500000            
m=0
while pmarrakech>pagadir :	
	pmarrakech=pmarrakech+50000
	pagadir=pagadir+(pagadir*0.08)
	m=m+1                     

print("le nombre d'anne est: ",m)
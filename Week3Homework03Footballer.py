try:
	with open('futbolcular.txt','r') as f:
		lisst =f.readlines()
		#print(lisst)
	with open('Galatasaray.txt','a') as gal:
		#print(lisst[25:47])
		gal.writelines(lisst[24:47])
	with open('Fenerbahce.txt','a') as fen:
		#print(lisst[1:24])
		fen.writelines(lisst[1:24])
	with open('Besiktas.txt','a') as bes:
		#print(lisst[48:])
		bes.writelines(lisst[48:])
except FileNotFoundError:
	print("Please Check The Sourcess File")
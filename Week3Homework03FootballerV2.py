list_gs= open("Galata.txt","a")
list_gs.close()
list_fb= open("Fener.txt","a")
list_fb.close()
list_bjk= open("Kartal.txt","a")
list_bjk.close()
try:
	futbolcular=open("futbolcular.txt","r")

	for satir in futbolcular:
		if "Galatasaray" in satir:
			print(satir,file=list_gs,end=""	)
		elif "Fenerbahce" in satir:
			print(satir,file=list_fb,end="")
		elif "Besiktas" in satir:
			print(satir,file=list_bjk,end="")
		else:
			print(satir)
except FileNotFoundError:
	print("File Can Not Found")

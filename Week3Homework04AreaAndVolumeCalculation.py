"""Karenin, ucgenin ve diktortgenin alanlarini hesaplayan, kup,kure ve koni seklinde olan cisimlerin hacmini hesaplayan bir program yazmanizi istiyoruz. 
Kullanicidan hangi seklin alanini veya hangi sekildeki cismin hacmini hesaplamak istedigini sormalisiniz ve o islem icin gereken verileri isteyip hesaplamayi 
yapmalisiniz. Tum bu islemleri yaparken hata alinabilecek durumlari ongorerek gerekli onlemleri almalisiniz.
"""
key = 1
while key == 1:
	try:
		enter = input("Please Press '1' For Volume Calculation, '2' for Area Calculation and 'q' To Exit: ")
		if enter =='q':
			print("Exiting...")
			key == 0
			break
		enter = int(enter)
		if enter == 1:
			value = int(input("Please Press '1' For Cube Volume Calculation, '2' for Sphere Volume Calculation and, '3' for Cone Volume Calculation: "))
			if value == 1:
				side= float(input("Please Enter The One Side Of Cube The Volume Of: "))
				print("Your Volume of Cube Is :",side**3)
			elif value == 2:
				radius= float(input("Please Enter The Radius of The Sphere You Want To Calculate The Volume Of: "))
				pi = 3.141592
				VolumeSphere = 4/3*(pi*radius**3)
				print("Your Volume of Sphere Is :",VolumeSphere)
			elif value==3:
				height= float(input("Please Enter The Height of The Cone You Want To Calculate The Volume Of: "))
				radiusCone = float(input("Enter The Radius (r) of The Base Circle of The Cone: "))
				pi = 3.141592
				VolumaCone = (1/3)*(pi*radiusCone**2*height)
				print("Your Volume of Cone Is :",VolumaCone)
		elif enter == 2:
			value = float(input("Press '1' to Calculate The Area of ​​the Square, '2' to Calculate The Area of T​the Triangle, and '3' to Calculate The Area of ​Tthe Rectangle: "))
			if value == 1:
				side= float(input("Please Enter an Edge of The Square You Want to Calculate The Area Of: "))
				print("Your Volume of Cube Is :",side**2)
			elif value == 2:
				side1= float(input("Please Enter First Edge of The Perpendicular Triangle You Want to Calculate The Area Of: "))
				side2= float(input("Please Enter Second Edge of The Perpendicular Triangle You Want to Calculate The Area Of: "))
				print("The Area Of The Perpendicular Triangle is: ",(side1*side2)/2)
			elif value == 3:
				side1= float(input("Please Enter Short Edge of The Rectangle You Want to Calculate The Area Of: "))
				side2= float(input("Please Enter Long Edge of The Rectangle You Want to Calculate The Area Of: "))
				print("The Area Of The Rectangle is: ",(side1*side2))
		else:
			print("Something Is Wrong")
	except ValueError:
		print("You Can Only Enter Integer")

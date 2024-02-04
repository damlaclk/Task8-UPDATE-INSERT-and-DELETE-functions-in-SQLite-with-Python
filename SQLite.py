import sqlite3

Connection = sqlite3.connect("/home/kali/Desktop/DB4S/TESTDB.db")
Cursor = Connection.cursor()

class Database:
	def getColumnNames():
        	Cursor.execute("PRAGMA table_info(STUDENTS)")
        	Columns = Cursor.fetchall()
        	return Columns
        	
        	
	def getAllStudents():
		Cursor.execute("SELECT * FROM STUDENTS ORDER BY studentName ASC;")	
		Students = Cursor.fetchall()
		return Students
		print(Database.getAllStudents())
		
		
	def searchStudent(value):
        	value = '%' + value + '%'
        	Cursor.execute("SELECT * FROM STUDENTS WHERE studentName LIKE ? OR studentSurname LIKE ?;", (value, value,))
        	Students = Cursor.fetchall()
        	return Students
        	
        	
	def searchStudentID(value):
        	Cursor.execute("SELECT * FROM STUDENTS WHERE studentId= ?;", (value,))
        	Students = Cursor.fetchall()
        	return Students
        	
        	
	def updateStudent(columnName, newValue, where):
        	Cursor.execute("UPDATE STUDENTS SET "+columnName+" = ? WHERE studentId = ?;", (newValue, where,))
        	print("Veri güncellendi.")
        	print(Database.getAllStudents())
        	Students = Cursor.fetchall()
        	Connection.commit()
        	return Students
        	
        	
	def addStudents(newName, newSurname):
		Cursor.execute("INSERT INTO STUDENTS (studentName, studentSurname) VALUES (?, ?);", (newName, newSurname,))
		print("Veri eklendi.")
		print(Database.getAllStudents())
		Students = Cursor.fetchall()
		Connection.commit()
		return Students
		
		
	def deleteStudent(delValue):
		Cursor.execute("DELETE FROM STUDENTS WHERE studentId = ?;", (delValue,))
		print("Veri silindi.")
		print(Database.getAllStudents())
		Students = Cursor.fetchall()
		Connection.commit()
		return Students
		
		
def baslangic():

	print ("Merhaba, öğrenci veri tabanında ne işlem yapmak istersiniz."+"\n"+"[1] Öğrenci Ara"+"\n"+"[2] Öğrenci güncelleştir"+"\n"+"[3] Öğrenci ekle"+"\n"+"[4] Öğrenci sil")

	islem = input ("Yapmak istediğiniz seçeneği giriniz: ")
	if islem == "1":
		ara = input ("Aramak istediğiniz öğrenci ismini yazınız: ")
		veri = Database.searchStudent(ara)
		if veri == (Database.searchStudent(ara)):
			print (veri)
		else:	
			print ("Aradığınız öğrenci sistemde yoktur.")
			
			
	elif islem == "2":
		print (Database.getAllStudents())
		guncelleme = input ("Güncellemek istediğiniz öğrencinin ID bilgisini giriniz: ")
		ad = Database.searchStudentID(guncelleme)
		
		print (ad[0][0],"adlı öğrencinin, hangi bilgisini güncelleştirmek istiyorsunuz?"+"\n"+"[1] Öğrenci Adı"+"\n"+"[2] Öğrenci Soyadı")
		guncelleme2 = input ("Güncellemek istediğiniz bilgiyi giriniz: ")
		
		if guncelleme2 == "1":
			guncelAd= input ("Güncel öğrenci adını giriniz: ")
			Database.updateStudent("studentName", guncelAd, guncelleme)
			
		elif guncelleme2 == "2":
			guncelSoyad= input ("Güncel öğrenci soyadını giriniz: ")
			Database.updateStudent("studentSurname", guncelSoyad, guncelleme)
			
		else:
			print ("Geçersiz işlem yaptınız.")
			
			
	elif islem == "3":
		print ("Eklemek istediğiniz öğrencinin bilgilerini yazınız")
		
		yeniAd = input("Öğrenci adını giriniz: ")
		yeniSoyad = input("Öğrenci soyadını giriniz: ")
		yeniEkleme= Database.addStudents(yeniAd, yeniSoyad)
		
		print (yeniEkleme)
		
		
	elif islem == "4":
		print (Database.getAllStudents())
		
		silID = input ("Silmek istediğiniz öğrencinin ID bilgisini giriniz: ")
		veriSil= Database.deleteStudent(silID)	
		
	else:
		print("Geçersiz işlem!")
		
	return baslangic()
	
print (baslangic())
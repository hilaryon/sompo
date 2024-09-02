import pymssql  
conn = pymssql.connect(server='db1.sompojapan.com.tr', user='sompoadmin@sompojapan.com.tr', password='A123A', database='KUNEFE')
cursor = conn.cursor()  
cursor.execute('SELECT c.SompoID, c.SOMPOCLIENTName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')  
row = cursor.fetchone()  
    while row:  
        print str(row[0]) + " " + str(row[1]) + " " + str(row[2])     
        row = cursor.fetchone()  

import sqlite3 # Python’un içindeki yerleşik veritabanı modülü.
import os # Dosya işlemleri için gerekli. Özellikle veritabanını silmek için kullanılıyor.

def create_database():
    if os.path.exists("students.db"): # Veritabanı dosyası var mı diye bakar.
        os.remove("students.db") # Varsa siler. Böylece her seferinde sıfırdan başlarız
    conn = sqlite3.connect("students.db") # Database ile bağlantı kuruyoruz.
    cursor = conn.cursor() # Bu bir imleç , Data base içinde gezinmemizi sağlıyor.
    return conn,cursor



def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE Students (
                   id INTEGER PRIMARY KEY,
                   name VARCHAR NOT NULL , 
                   age INTEGER, 
                   email VARCHAR UNIQUE,
                   city VARCHAR)
                ''')
    
    cursor.execute('''
    CREATE TABLE Courses (
                   id INTEGER PRIMARY KEY,
                   course_name VARCHAR NOT NULL , 
                   instructor TEXT, 
                   credits INTEGER)
                ''')
    

def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),     # 5 tane kayıt var ve tuple içinde!
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (? , ? , ? , ? , ?)", students) # executemany --> çoklu veri ekle  -   '?' --> Yer tutucu (SQL Injection'a karşı güvenli).
    # Veri eklemek için Python'dan liste gönderiyorum. SQL bu listeyle tabloya satır ekliyor.


    courses  = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ] 

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)" , courses)

    print("Sample data inserted succesfully!")


def basic_sql_operations(cursor):
    # 1-) SELECT ALL
    print("------------Select All------------")
    cursor.execute("SELECT * FROM Students")
    record = cursor.fetchall()   # SELECT * --> Bütün veriyi getirir. 'TÜMÜ' !
    for row in record:
        print(row)
        
    cursor.execute("SELECT * FROM Courses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 2-) SELECT COLUMNS
    print("------------Select Columns------------")
    cursor.execute("SELECT name,age FROM Students") # Sadece name ve age değerlerini getirir
    record = cursor.fetchall()
    print(record)

    # 3-) WHERE clause
    print("------------Where Clause------------")
    cursor.execute("SELECT * FROM Students WHERE age = 20") # Yaşı 20 olanları getirir
    record = cursor.fetchall()
    print(record)

    # 4-) WHERE with string
    print("------------Where city = New York------------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'") # city değeri New York olanları getirir.
    record = cursor.fetchall()
    print(record)

    # 5-) ORDER BY
    print("------------ORDER BY age------------")
    cursor.execute("SELECT * FROM Students ORDER BY age") # Yaşlara göre artan şekilde sıralıyor
    record = cursor.fetchall()
    for row in record:
        print(row)

    # 6-) Limit
    print("------------Limit by 3------------")
    cursor.execute("SELECT * FROM Students LIMIT 3") # Yaşlara göre artan şekilde sıralıyor
    record = cursor.fetchall()
    for row in record:
        print(row)


def sql_update_delete_insert_operations(conn,cursor):
    # 1-) INSERT
    cursor.execute("INSERT INTO Students VALUES (6,'Frank Miller', 23, 'frank@gmail.com', 'Miami')")
    conn.commit() # Delete edeceğimiz zaman bunu yazmamış olsak kayıt yok diyebilir. Database e işlenmezdi!

    # 2-) UPDATE
    cursor.execute("UPDATE Students SET age = 30 WHERE id = 6")
    conn.commit()

    # 3-) DELETE 
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()


def aggregate_functions(cursor):
    # 1-) Counts
    print("------------Aggregate Functions Count------------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchall() # --> [(5,)] # fetchone ---> (5,)
    print(result)

    # 2-) Average
    print("------------Aggregate Functions Average------------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone() 
    print(result[0])

    # 3-) MAX-MIN   
    print("------------Aggregate Functions MAX-MIN------------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone() # tuple olarak (22,19) gelecek resutl[0] yaparsak sadece 22 gelir!
    print(result)

    # 4-) GROUP BY
    print("------------Aggregate Functions Group By------------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall() 
    print(result)

def answers(cursor):
    # QUİZ 2. SORU
    print("----2. SORU----")
    cursor.execute("SELECT instructor , course_name FROM Courses")
    result = cursor.fetchall()
    for res in result:
        print(res)

    # QUİZ 3. SORU
    print("----3. SORU----")
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    result = cursor.fetchall()
    for res in result:
        print(res)

    # QUİZ 4. SORU
    print("----4. SORU----")
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    result = cursor.fetchall()
    for res in result:
        print(res)

    # QUİZ 5. SORU
    print("----5. SORU----")
    cursor.execute("SELECT course_name FROM Courses WHERE instructor = 'Dr. Anderson' ")
    result = cursor.fetchall()
    for res in result:
        print(res[0])

    # QUİZ 6. SORU
    print("----6. SORU----")
    cursor.execute("SELECT name FROM Students WHERE name LIKE 'A%' ")
    result = cursor.fetchall()
    for res in result:
        print(res[0])

    # QUİZ 7. SORU
    print("----7. SORU----")
    cursor.execute("SELECT course_name FROM Courses WHERE credits >= 3 ")
    result = cursor.fetchall()
    for res in result:
        print(res[0])

    # QUİZ 1**. SORU  ??????
    print("----1**. SORU----")
    cursor.execute("SELECT name FROM Students ORDER BY name ")
    result = cursor.fetchall()
    for res in result:
        print(res)

    # QUİZ 2**. SORU ????
    print("----2**. SORU----")
    cursor.execute("SELECT name FROM Students WHERE  age >20 ORDER BY age ")
    result = cursor.fetchall()
    for res in result:
        print(res[0])

    # QUİZ 3**. SORU
    print("----3**. SORU----")
    cursor.execute("SELECT name FROM Students WHERE city = 'New York' OR city = 'Chicago' ")
    result = cursor.fetchall()                            # IN ('New York' , 'Chicago')  ---> İki şekilde de oluyor ama bu daha mantıklı!
    for res in result:
        print(res[0])

    # QUİZ 4**. SORU
    print("----4**. SORU----")
    cursor.execute("SELECT name FROM Students WHERE city NOT IN ('New York')") 
    result = cursor.fetchall()                      # city != 'New York'  ---> klasik bu yöntem de olur! Ama NOT IN kullan1
    for res in result:
        print(res[0])

    






def main():
    conn , cursor = create_database()
    
    # try/except/finally yapısı sayesinde hata da olsa bağlantı temizce kapanıyor.
    try: 
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn,cursor)
        aggregate_functions(cursor)
        answers(cursor)
        conn.commit() # Yapılan işlemleri kaydeder (SQL'de bu çok önemli!)


    
    except sqlite3.Error as e:
        print(e)
    
    finally: #Ne olursa olsun bağlantı kapatılıyor.
        conn.close()


if __name__ == "__main__": # Eğer başka bir dosyada bu kodu import edersen, bu blok çalışmaz. 
    main()                 # Yani sadece ana dosya olarak çalıştırıldığında devreye girer.

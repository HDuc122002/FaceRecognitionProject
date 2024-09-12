import mysql.connector

def getProfile(user_id):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    query = "SELECT * FROM people WHERE id=%s"
    cursor.execute(query, (user_id,))
    profile = cursor.fetchone()
    conn.close()
    return profile

def checkIn(user_id):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    query = "INSERT INTO attendance (user_id, action) VALUES (%s, 'check-in')"
    cursor.execute(query, (user_id,))
    conn.commit()
    conn.close()


def checkOut(user_id):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    
    # Cập nhật thời gian check-out cho người dùng
    query = """
    UPDATE attendance
    SET action = 'check-out'
    WHERE user_id = %s
    AND action = 'check-in'
    AND timestamp = (
        SELECT MAX(timestamp)
        FROM (SELECT * FROM attendance WHERE user_id = %s AND action = 'check-in') AS temp
    )
    """
    cursor.execute(query, (user_id, user_id))
    conn.commit()
    conn.close()


def check_admin_credentials(username, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    query = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    admin = cursor.fetchone()
    conn.close()
    return admin is not None

def insert(name):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    
    # Kiểm tra xem người dùng đã tồn tại chưa
    cursor.execute("SELECT * FROM people WHERE name = %s", (name,))
    profile = cursor.fetchone()

    if profile:
        return profile[0]  # Trả về ID nếu đã tồn tại
    else:
        # Thêm mới nếu không có
        cursor.execute("INSERT INTO people (name) VALUES (%s)", (name,))
        conn.commit()
        return cursor.lastrowid

def deleteUser(user_id):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    
    # Xóa người dùng và lịch sử check-in/check-out
    cursor.execute("DELETE FROM attendance WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM people WHERE id = %s", (user_id,))
    
    conn.commit()
    conn.close()

def getProfileByName(name):
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    query = "SELECT * FROM people WHERE name=%s"
    cursor.execute(query, (name,))
    profile = cursor.fetchone()
    conn.close()
    return profile

def get_history():
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    
    # Truy vấn lấy dữ liệu lịch sử check-in, check-out
    query = """
    SELECT attendance.user_id, people.name, attendance.timestamp, attendance.action 
    FROM attendance 
    JOIN people ON attendance.user_id = people.id
    ORDER BY attendance.timestamp DESC
    """
    cursor.execute(query)
    history = cursor.fetchall()
    conn.close()
    
    return history

def get_people():
    conn = mysql.connector.connect(host="localhost", user="root", password="Huynhduc1220", database="faceid")
    cursor = conn.cursor()
    query = "SELECT id, name FROM people"
    cursor.execute(query)
    people = cursor.fetchall()
    conn.close()
    return people

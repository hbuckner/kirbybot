import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password = "megaman1", host ="127.0.0.1", port="5432")
print("database opened succesfully")

cur = con.cursor()
cur.execute('''CREATE TABLE tbl_user
    (PHONE CHAR(50) Primary KEY NOT NULL,
    IMAGEID     TEXT,
    SENTTODAY   BOOLEAN);''')
con.commit()
con.close()
print("table created successfully")

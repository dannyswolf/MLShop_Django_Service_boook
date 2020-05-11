import sqlite3
import os

db = "/home/dannys/Desktop/Service_book24-04-2020.db"
db_path = os.path.dirname(db)
print("db_path", db_path)
con = sqlite3.connect(db)
c = con.cursor()
c.execute("SELECT * FROM Service_images;")
all_files = c.fetchall()
c.close()

for file in all_files:
    service_id = file[0]
    filename = file[1] + file[2]
    blob_file = file[4]

    file_path = os.path.join(db_path, f"Service_images/{service_id}/")
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(os.path.join(file_path, filename), 'wb') as new_file:
        new_file.write(blob_file)
    print("Done", service_id)


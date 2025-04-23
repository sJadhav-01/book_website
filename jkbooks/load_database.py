import mysql.connector as sql
import csv

mydb = sql.connect(host= 'localhost', user='root', password='admin123', database='book_website')

mycursor=mydb.cursor()

csv_file_path = './LibraryDataset_CSV.csv'
table_name = 'books'

with open(csv_file_path, 'r', encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        query = f"insert into {table_name} ( ISBN, Book_title, Category, Rental_Price, Status,Author, Publisher) values (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, row)

mydb.commit()
print(f"{mycursor.rowcount} records are inserted.")

import mysql.connector as sql
import os 

image_loc = f'./static/book covers/'

def image_to_blob(image_path):
    try:
        with open (image_path, 'rb') as image_file:
            blob_data = image_file.read(image_file)
            return blob_data
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the image: {e}")
        return None

db_config = {
    'host': 'localhost',
    'user':'root',
    'password':'admin123',
    'database':'book_website'
}

mydb = sql.connect(**db_config)
my_cursor = mydb.cursor()

query= 'select register_no, book_title from books'
my_cursor.execute(query)
records = my_cursor.fetchall()

for record in records:
    book_id = record[0]
    book_title = record[1].strip()
    # image_path = f"{image_loc} {book_title}.jpg"
    image_path = os.path.join(image_loc, f"{book_title}.jpg")
    if os.path.exists(image_path):
        image_blob = image_to_blob(image_path)
        if image_blob:
            query2 = f"update books set cover_image = %s where book_title = %s"
            my_cursor.execute(query2, (image_blob, book_id))
            mydb.commit()
            print(f"Successfully updated cover image for '{book_title}'")
        else:
            print(f"Could not read image or image not found for '{book_title}'")
    else:
        print(f"Warning: Image file not found at '{image_path}' for '{book_title}'")

my_cursor.close()
mydb.close()
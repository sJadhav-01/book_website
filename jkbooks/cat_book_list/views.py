from django.shortcuts import render
import mysql.connector as sql
# Create your views here.

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin123',
    'database': 'book_website'
}

key = ''

def cat_book_list(request):
    global key
    empty_dict = {}
    if request.method == "POST":
        mydb = sql.connect(**db_config)
        mycursor = mydb.cursor()
        key = request.POST.get('category_key', '')
        print(f'Key : {key}')
        # query = f"select * from books where category = '{key}'"
        # # query = f"select * from books where category = 'Fantasy'"
        # mycursor.execute(query)  # there can be a chance of sql injection
        query = "select * from books where category like %s"
        mycursor.execute(query, (f"%{key}%",))
        category_book_list = mycursor.fetchall()
        print (category_book_list)
        cat_book_list_dict = {'category_book_list' : category_book_list,
                              'key' : key}
        print(cat_book_list_dict)
        return render(request, "cat_book_list.html", cat_book_list_dict)
    return render(request, "cat_book_list.html", empty_dict)
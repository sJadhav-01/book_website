from django.shortcuts import render
import mysql.connector as sql
# Create your views here.

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin123',
    'database': 'book_website'
}

key= ''

def search_key(request):
    global key
    empty_dict = {}

    if request.method == "POST":
        mydb = sql.connect(**db_config)
        mycursor = mydb.cursor()
        key = request.POST.get('search_key','')
        # query = f"select * from books where book_title like '%{key}%' or author like '%{key}%' or category like '%{key}%'"
        query = "select * from books where book_title like %s or author like %s or category like %s"
        mycursor.execute(query, (f'%{key}%',f'%{key}%',f'%{key}%',))
        search_result = mycursor.fetchall()
        search_result_dict = {'search_result' : search_result}
        return render(request, 'search_result.html', search_result_dict)
    return render(request, 'search_result.html', empty_dict )   


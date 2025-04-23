from django.shortcuts import render, redirect
import mysql.connector as sql


# Create your views here.
em=''
pw=''

# def login_initial(request):
#     return render(request, 'login_page.html')

def login_action(request):
    global em,pw

    if request.method == "POST":
        data_obj=sql.connect(host="localhost", user='root', password='admin123', database='book_website')
        cursor=data_obj.cursor()
        data=request.POST
        for key, value in data.items():
            if key == 'email':
                em = value
            if key == 'password':
                pw = value
        
        query = "select * from users where email = '{}' and password = '{}'".format(em,pw)
        cursor.execute(query)
        t=tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            # return redirect(request, 'home.html')
            return redirect('home/')
        
    return render(request, 'login_page.html')
from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
fn=''
ln=''
gen=''
em=''
pw=''


def sign_up_action(request):
    global fn,ln,gen,em,pw

    if request.method == "POST":
        data_obj=sql.connect(host="localhost", user='root', password='admin123', database='book_website')
        cursor=data_obj.cursor()
        data=request.POST
        for key, value in data.items():
            if key=='first_name':
                fn = value
            if key=='last_name':
                ln = value
            if key == 'gender':
                gen = value
            if key == 'email':
                em = value
            if key == 'password':
                pw = value
        
        query = "insert into users values ('{}','{}','{}','{}','{}')".format(fn,ln,gen,em,pw)
        cursor.execute(query)
        data_obj.commit()
    
    return render(request, 'signup_page.html')
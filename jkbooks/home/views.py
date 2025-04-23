from django.shortcuts import render
import mysql.connector as sql

# Create your views here.

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin123',
    'database': 'book_website'
}

# # @api.route('home/')
# def display_home_page(request):
#     mydb = sql.connect(**db_config)
#     mycursor = mydb.cursor()

#     query = "select * from books"
#     mycursor.execute(query)
#     book_data = mycursor.fetchall()
#     print(book_data)
#     # book_data_dict = {}

#     # for record in book_data:
#     #     book_data_dict['Register_no'] = record[0]
#     #     book_data_dict['ISBN'] = record[1]
#     #     book_data_dict['Book_title'] = record[2]
#     #     book_data_dict['Category'] = record[3]
#     #     book_data_dict[' Rental_Price'] = record[4]
#     #     book_data_dict['Status'] = record[5]
#     #     book_data_dict['Author'] = record[6]
#     #     book_data_dict['Publisher'] = record[7]

#     # print(book_data_dict)
#     data = {'book_data' : book_data}
#     print(data)
#     return render(request, 'home.html', data)




def display_home_page(request):
    mydb = sql.connect(**db_config)
    mycursor = mydb.cursor()

    query_1 = "select * from books"
    query_2 = "select distinct category from books" 
    # query_3 = "select * from books where date = sysdate - 10"

    mycursor.execute(query_1)
    all_data = mycursor.fetchall()

    # book_data = {}
    # for record in all_data:
    #     if record[2] not in book_data:
    #         book_data[record[2]]= {}
    #         for _ in book_data:
    #             book_data[record[2]]['Register_no'] = record[0]
    #             book_data[record[2]]['ISBN'] = record[1]
    #             book_data[record[2]]['Category'] = record[3]
    #             book_data[record[2]][' Rental_Price'] = record[4]
    #             book_data[record[2]]['Status'] = record[5]
    #             book_data[record[2]]['Author'] = record[6]
    #             book_data[record[2]]['Publisher'] = record[7]

    # print(book_data)
    mycursor.execute(query_2)
    category_data = mycursor.fetchall()
    print(all_data)
    print(category_data)
    data = {'book_data' : all_data,
            'category_data' : category_data}

    return render(request, 'home.html', data)
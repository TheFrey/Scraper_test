import requests
from bs4 import BeautifulSoup
from getters import *
from mysql.connector import connect, Error
from constant import *


def main():
    try:
        with connect(host='localhost',
                     user=input('Login: '),
                     password=input('Password: '),
                     database='test_task') as connection:
            for i in range(1, 2):
                r = requests.get(link.format(num=i))
                if r.status_code == 404:
                    break
                else:
                    soup = BeautifulSoup(r.text, "lxml")
                    div_list = soup.find_all('div', {'class': 'search-item regular-ad'})

                for room in div_list:
                    info = room_info(room)
                    with connection.cursor() as cursor:
                        cursor.execute(db_query.format(title=info['title'],
                                                       img=info['img'],
                                                       pub_date=info['date-post'],
                                                       city=info['city'],
                                                       bedrooms=info['bedrooms'],
                                                       description=info['description'],
                                                       currency=info['price']['currency'],
                                                       price=info['price']['price']))
                        connection.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    main()

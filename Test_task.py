import requests
import asyncio
from bs4 import BeautifulSoup
from getters import *
from mysql.connector import connect, Error
from constant import *


async def req(url):
    global block_list
    r = requests.get(url)
    await asyncio.sleep(2)
    if r.status_code != 404:
        soup = BeautifulSoup(r.text, "lxml")
        block_list.append(soup.find_all('div', {'class': 'search-item regular-ad'}))


def main(div_list):
    try:
        with connect(host='localhost',
                     user=input('Login: '),
                     password=input('Password: '),
                     database='test_task') as connection:
            # Переглядаємо скільки сторінок доступно (1 - 40 of 3766) тобто 95 обмежив
            link_list = []
            for i in range(1, 96):
                link_list.append(link.format(num=i))
            loop = asyncio.new_event_loop()
            tasks_list = [req(url) for url in link_list]
            loop.run_until_complete(asyncio.wait(tasks_list))
            loop.close()
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
    block_list = []
    main(block_list)

from bs4 import BeautifulSoup
import datetime


def room_info(room):
    room_set = {'img': get_img_href(room),
                'title': get_title(room),
                'date-post': get_pub_date(room),
                'city': get_city(room),
                'bedrooms': get_bedrooms(room),
                'description': get_description(room),
                'price': get_price(room)}
    return room_set


def get_price(text):
    soup = BeautifulSoup(str(text), 'lxml')
    price_val = soup.find('div', {'class': 'price'}).text.replace('\n', '').replace(' ', '').replace(',', '')
    if 'Please' not in price_val:
        price = {'currency': price_val[0],
                 'price': price_val[1:]
        }
    else:
        price = {'currency': '-',
                 'price': 0.00
                 }
    return price


def get_img_href(text):
    soup = BeautifulSoup(str(text), 'lxml')
    img = soup.find('img')
    return img.get('data-src')


def get_city(text):
    soup = BeautifulSoup(str(text), 'lxml')
    city = soup.find('span', {'class': ''}).text.replace('\n', '').replace('  ', '')
    return city


def get_title(text):
    soup = BeautifulSoup(str(text), 'lxml')
    title = soup.find('a', {'class': 'title'}).text.replace('\n', '').replace('  ', '')
    return title[:100]


def get_pub_date(text):
    soup = BeautifulSoup(str(text), 'lxml')
    pub_date = soup.find('span', {'class': 'date-posted'}).text
    if pub_date[0] == '<':
        pub_date = str(datetime.date.today().strftime('%d-%m-%Y'))
    elif pub_date[0] == 'Y':
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        pub_date = str(yesterday.strftime('%d-%m-%Y'))
    else:
        pub_date = str(pub_date.strftime('%d-%m-%Y'))
    return pub_date


def get_bedrooms(text):
    soup = BeautifulSoup(str(text), 'lxml')
    bedrooms = soup.find('span', {'class': 'bedrooms'}).text.replace('\n', '').replace('  ', '').split(':')[-1]
    return bedrooms


def get_description(text):
    soup = BeautifulSoup(str(text), 'lxml')
    description = soup.find('div', {'class': 'description'}).text.replace('\n', '').replace('  ', '')
    return description

db_query = '''INSERT room_info(title, img, pub_date, city, bedrooms, description, currency, price)
              VALUES ("{title}", "{img}", "{pub_date}", "{city}", "{bedrooms}", "{description}", 
              "{currency}", "{price}")'''
link = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{num}/c37l1700273'

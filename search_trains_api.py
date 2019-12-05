import requests
import datetime


def find_city(city_part_word):
    """Gets the name of the city, returns the number (Експрес-3) in https://booking.uz.gov.ua/"""
    url = f'https://booking.uz.gov.ua/ru/train_search/station/?term={city_part_word}'
    p = requests.get(url)
    for i in p.json():
        print(i)
        if i['title'].lower() == city_part_word.lower():
            print(i['title'], '=>', i['value'])
            return i['value']


def get_captcha():
    """writes captcha into capcha.gif and returns _gv_sessid from  https://booking.uz.gov.ua/ru/captcha/"""
    url = 'https://booking.uz.gov.ua/ru/captcha/'
    p = requests.get(url)
    out = open("capcha.gif", "wb")
    out.write(p.content)
    out.close()
    # cookies1 = p.cookies
    return p.cookies['_gv_sessid']


def train_search(fr_st, to_st, date):
    count_tries = 0
    while True:
        sessid = get_captcha()
        captcha = input('Введи цифрі с картинки capcha.gif:\n')
        if captcha.isdecimal():
            captcha = int(captcha)
        else:
            print('вы ввели не чесло')
        count_tries = count_tries + 1
        url = 'https://booking.uz.gov.ua/train_search/'
        r = requests.post(url,
                          data={'from': fr_st,
                                'to': to_st,
                                'date': date,
                                'time': '00:00',
                                'captcha': captcha},
                          cookies={'_gv_sessid': sessid})

        if r.json() == {'error': 1, 'data': 'Перевірочний код введено невірно, спробуйте знову', 'captcha': 'booking'}:
            print(count_tries, '=>', datetime.datetime.now().strftime('%d-%m-%Y %H:%M'), '=>', r.json())
        else:
            print(count_tries, '=>', datetime.datetime.now().strftime('%d-%m-%Y %H:%M'), '=>', r.json())
            break


if __name__ == '__main__':
    fr = find_city(input('введите название города отправления\n'))
    to = find_city(input('введите название города прибытия\n'))
    leaving_date = input('Введите дату отправления в формате "YYYY-MM-DD"\n')
    train_search(fr, to, leaving_date)
 #   train_search(2200001, 2218000, '2019-12-12')

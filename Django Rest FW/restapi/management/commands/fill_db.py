import requests


def load_from_xml(file_name):
    url_currency = 'http://www.cbr.ru/scripts/XML_valFull.asp'
    print(f'Загружаем cправочник с кодами валют в таблицу "Currency"...')
    response = requests.get(url_currency)
    for_write = bytes.decode(response.content, 'windows-1251')
    with open(file_name + '.xml', 'w', encoding='utf-8') as file:
        file.write(for_write)
    print(f'Справочник валют сохранен в файл {file_name }.xml')


load_from_xml('currency')

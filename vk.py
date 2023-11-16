import requests

token = 'afe1fa60afe1fa60afe1fa6083acf7d8e3aafe1afe1fa60caa15fbacb31cdb69a225a39'
account_ID = 'roman_lbj23'
domain = 'rhymeru'

def get_accaount_info(account_ID):
    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v': 5.154,
                                'user_ids': account_ID,
                                'fields': 'about, bdate, city, counters'
                            }
                           )
    data = response.json()
    print(data['response'][0]['first_name'], data['response'][0]['last_name'], '\n', 'Дата рождения:', data['response'][0]['bdate'], '\n', 'Город:', data['response'][0]['city']['title'], '\n', 'Кол-во подписчиков', data['response'][0]['counters']['followers'],'\n', 'Кол-во фото', data['response'][0]['counters']['photos'] )




def get_wall_posts(owner_ID):
    all_posts = []

    response = requests.get(
        'https://api.vk.com/method/wall.get',
        params={
            'access_token': token,
            'v': 5.137,
            'domain': owner_ID,
            'count': 4
        }
    )
    data=response.json()
    all_posts.extend(data)

    for i in data['response']['items']:
        print('Текст поста:\n' + i['text'] + '\nКол-во лайков:\n' + str(i['likes']['count']) + '\n')





(get_accaount_info(account_ID))
print('\n\n')

(get_wall_posts(domain))

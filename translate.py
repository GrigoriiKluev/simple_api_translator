import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'OWE5MDJhMWItMjRkMi00NzNmLTk5MWUtZjFiZDMxMzk0YTE1OjY5MzU4ODg2NzVkMDQ1YTY4MWNkNzBkYmJmMGZiMjBl'

headers_auth = {'Authorization': 'Basic ' + KEY}

auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text
    while True:
        word = input("Введите слово для перевода или 'с' для выхода:")
        if word and word != 'c':
            headers_translate = {'Authorization': 'Bearer '+token}
            params = {
                'text':word,
                'srcLang': 1033,
                'dstLang': 1049,
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except Exception:
                print('error')
        else:
            break
else:
    print('Error')
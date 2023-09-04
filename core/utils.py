import requests

def get_quran_surahs():
    api_url = 'https://api.alquran.cloud/v1/surah'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        # Tangani kesalahan jika diperlukan
        return None

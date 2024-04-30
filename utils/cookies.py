import json
import os

import json
import os


import json
import os


def saveCookies(driver, filename='cookies.json', save_path='testdata'):
    # Pobierz pliki cookie z przeglądarki
    cookies = driver.get_cookies()

    # Pobierz aktualny URL
    url = driver.current_url

    # Utwórz pełną ścieżkę do katalogu projektu
    project_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

    # Utwórz pełną ścieżkę do katalogu testdata w katalogu projektu
    testdata_path = os.path.join(project_dir, save_path)

    # Utwórz katalog testdata, jeśli nie istnieje
    if not os.path.exists(testdata_path):
        os.makedirs(testdata_path)

    # Utwórz pełną ścieżkę do pliku w katalogu testdata
    file_path = os.path.join(testdata_path, filename)

    # Zapisz pliki cookie i URL do pliku
    data_to_save = {'url': url, 'cookies': cookies}
    with open(file_path, 'w') as file:
        json.dump(data_to_save, file)
    print(f'New Cookies saved successfully at {file_path}')


def loadCookies(driver, filename='cookies.json', load_path='testdata'):
    # Utwórz pełną ścieżkę do katalogu projektu
    project_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

    # Utwórz pełną ścieżkę do katalogu testdata w katalogu projektu
    testdata_path = os.path.join(project_dir, load_path)

    # Utwórz pełną ścieżkę do pliku w katalogu testdata
    file_path = os.path.join(testdata_path, filename)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Sprawdź, czy zapisane ciasteczka mają przypisany URL
        if 'url' in data:
            url = data['url']
            cookies = data['cookies']

            for cookie in cookies:
                driver.add_cookie(cookie)

            # Dodaj kod do ustawienia języka na stronie
            driver.get(url)  # Przejdź ponownie na stronę
            driver.execute_script("document.cookie='lang=pl'")  # Ustaw język na "pl"

            driver.refresh()
            print(f'Cookies loaded successfully for URL: {url}')
        else:
            print(f'No URL information found in the cookies file: {file_path}')
    else:
        print(f'No cookies file found at: {file_path}')





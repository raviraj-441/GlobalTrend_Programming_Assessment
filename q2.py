import requests
from time import sleep

def download_content(urls):
    results = {}
    for url in urls:
        attempts = 0
        while attempts < 3:
            try:
                response = requests.get(url)
                response.raise_for_status()
                results[url] = response.content
                break
            except requests.exceptions.RequestException as e:
                attempts += 1
                sleep(1)
                if attempts == 3:
                    results[url] = str(e)
    return results

urls = ["https://www.amazon.in/", "https://www.flipkart.com/"]
print(download_content(urls))

import requests
from bs4 import BeautifulSoup

def kubernetes_pod(pages):
    page = 1
    while page <= 1:
        url = 'https://dashboard.i.prod.jiff.kube/#!/pod?namespace=default'
        code = requests.get(url)
        plaintext = code.text
        soup = BeautifulSoup(plaintext)
        for pods in soup.findAll('a', {'class': 'kd-middleellipsis ng-binding'}):
            print(pods)


kubernetes_pod(1)




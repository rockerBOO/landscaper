import requests

def scrape(url):
  headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"}

  resp = requests.get(url, headers=headers)

  return resp.text

# downloading from web
import requests
link_of_file = 'https://...'
res = requests.get(link_of_file)
res.raise_for_status()


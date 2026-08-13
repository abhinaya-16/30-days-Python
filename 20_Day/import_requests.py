import requests # importing the request module

url = 'https://arbre-org-chart.vercel.app/' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print("----Complete page text---------")
print(response.text) # gives all the text from the page
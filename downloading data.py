#As it is needed to download each file for a day in specific year for specific instrument measurement,
#this routine is beneficial to automize the process of downloading big amount of datafiles
 
#!pip install wget <-- first, it is needed to install wget in cmd

#importing libraries
from bs4 import BeautifulSoup
import requests
import wget

#defining url address from which data would be retrieved:
url = 'http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2016/'
url1 = 'http://themis.ssl.berkeley.edu/data/themis/tha/l2/mom/2015/'
url2 = 'http://themis.ssl.berkeley.edu/data/themis/tha/l2/gmom/2016/'

#defining extension of the file ('.cdf')
ext = 'cdf'
#fucntion to find the files with requested extension in url
def listFD(url, ext=''):
    page = requests.get(url).text
    print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

#Calling the function listFD to download the data:
for file in listFD(url, ext):
    wget.download(file)
for file in listFD(url1, ext):
        wget.download(file)
for file in listFD(url2, ext):
    wget.download(file)
        
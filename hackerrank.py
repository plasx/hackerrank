# Simply my 'sratchpad' for hackerrank questions, I tend to like the solutions I provide and sometimes I hate them so I put them here and analyze a better way I could've done the test.
import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


def getMovieTitles(substr):
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title={}'.format(substr)
    html = None
    titles = []
    with urlopen(url) as response:
        html = json.loads(response.read().decode('utf8'))
    for i in range(1, html['total_pages'] + 1):
        print(url)
        with urlopen(url) as response:
            data = json.loads(response.read().decode('utf8'))
            for x in range(len(data['data'])):
                titles.append(data['data'][x]['Title'])
    titles.sort()
    return titles




def getPageCount(url):
    with urlopen(url) as response:
        return json.loads(response.read().decode('utf8'))['total_pages']


def getMovieTitles(substr):
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title={}'.format(substr)
    titles = []
    pages = getPageCount(url)
    #print('PAGES NUM', str(pages))
    for i in range(1, pages + 1):
        #print(str(i))
        with urlopen(url) as response:
            data = json.loads(response.read().decode('utf8'))
            for x in range(len(data['data'])):
                titles.append(data['data'][x]['Title'])
    return titles.sort()
    





select email, count(*) as c from DEPARTMENT
group by email having c > 1
order by c desc


select email from DEPARTMENT group by email having count(*) >1





for i in range(5,0,-1):
    print(i)





[[11, 2, 4], [4, 5, 6], [10, 8, -12]]

# >>> x[0][2]
# 4
# >>> x[1][1]
# 5
# >>> x[2][0]
# 10
def diagonalDifference(arr):
    x = [arr[i-1][i-1] for i in range(1, len(arr) + 1)]
    #y = [arr[i][len(arr) - i] for i in range(len(arr) -1, -1, -1)]
    y = []
    for i in range(len(arr) -1, -1, -1):
        number = i - len(arr) + 1
        y.append(arr[abs(number)][i])
    print(abs(sum(x) - sum(y)))


xbox = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])





def staircase(n):
    [print((n - i) * ' ' +  i * '#') for i in range(1, n + 1)]


staircase(6)








x =  [1,1,2,2,2,2,2,1,1,2,2,1,1,1,2,3,5,6,7,8,9,7,9,9,9,9,9,9]

def count_elements(lst):
    elements = {}
    for elem in lst:
        if elem in elements.keys():
            elements[elem] += 1
        else:
            elements[elem] = 1
    return elements

count_elements(x)


def birthdayCakeCandles(ar):
    candlecount = {}
    largest = 0
    for candle in ar:
        if candle > largest:
            largest = candle
        if candle in candlecount.keys():
            candlecount[candle] += 1
        else:
            candlecount[candle] = 1
    return candlecount[largest]
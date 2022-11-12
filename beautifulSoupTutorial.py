from bs4 import BeautifulSoup

html_doc  = """ #<!DOCTYPE html>
#<html lang="en">
#<head>
 #   <meta charset="UTF-8">
  #  <meta http-equiv="X-UA-Compatible" content="IE=edge">
   # <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#</body>
#</html> """

soup = BeautifulSoup(html_doc, 'html.parser')

for i in soup.find_all('a'):
    print(i.get('href'))


#for yo in soup.find_all('a'):
  #  print(yo.get('href'))
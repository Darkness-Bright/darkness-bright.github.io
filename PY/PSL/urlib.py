import urllib, urllib.parse, urllib.request
with urllib.request.urlopen('https://www.gumtree.com.au/s-mount-waverley-melbourne/ps5+edition/k0l3001607r50?price=300.00__544.00') as response:
   html = response.read().decode('utf-8')
   crop = html.split('class="search-results-page__user-ad-collection">')[1].split('</section>')[0]
   list = crop.split('</a><a')
   for i in list:
      url = 'https://gumtree.com.au'+i.split('href="')[1].split('"')[0]
      price = i.split('Price: ')[1].split(' .')[0]
      print(price+': '+url)
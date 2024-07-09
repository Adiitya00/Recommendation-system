import requests

# url = "https://amazon-data-scraper124.p.rapidapi.com/search/Nintendo%20Switch"
#
# querystring = {"api_key":"3ba0325127417000e0b265200ab7ed34"}
#
# headers = {
# 	"X-RapidAPI-Key": "4e020578dfmshfd79f3addccedd7p19bec8jsn56cb0ca528f9",
# 	"X-RapidAPI-Host": "amazon-data-scraper124.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

product = "iphone 14"

# flipkart_api = requests.get(f'https://flipkart.dvishal485.workers.dev/search/{product}')
# flipkartResponse = flipkart_api.json()

# Amazon Api
# url = f"https://amazon-data-scraper124.p.rapidapi.com/search/{product}"
# querystring = {"api_key": "3ba0325127417000e0b265200ab7ed34"}
#
# headers = {
# 	"X-RapidAPI-Key": "b6859e150fmsh54dc642c5225265p15910ejsn642549934c0e",
# 	"X-RapidAPI-Host": "amazon-data-scraper124.p.rapidapi.com"
# }
#
# Amazon_response = requests.get(url, headers=headers, params=querystring)


# Ebay API
# ebayurl = f"https://ebay-search-result.p.rapidapi.com/search/{product}"
#
# ebayheaders = {
# 	"X-RapidAPI-Key": "b6859e150fmsh54dc642c5225265p15910ejsn642549934c0e",
# 	"X-RapidAPI-Host": "ebay-search-result.p.rapidapi.com"
# }


# Ebay_APIresponse = requests.get(ebayurl, headers=ebayheaders).json()['results']
# amazon = Amazon_response.json()['results'][0]


# print(Ebay_APIresponse)
# print(Amazon_response.json())
# print(amazon)



# ebayProductPrice = float(Ebay_APIresponse[3]['price'].split('$')[1])
# print(ebayProductPrice)
# print(Ebay_APIresponse[3]['url'])
# print(Ebay_APIresponse[1]['rating'])


# flipkart
# flipkart = flipkartResponse['result'][0]
# print(flipkart)
# flipkartPrice = float(flipkart['current_price'])/ 82
# print(flipkartPrice)
# print(flipkart['link'])

# Amazon
# print(Amazon_response.json())
# print(Amazon_response.json()['results'][0])
# print(Amazon_response.json()['results'][0])
# pricesOfAllwebsite = [float(Ebay_APIresponse.split('$')[2]), float(flipkart['current_price']) / 82,
# 					  float(Amazon_response['price'])]
# lowest_price_index = pricesOfAllwebsite.index(min(pricesOfAllwebsite))
# lowest_price = pricesOfAllwebsite[lowest_price_index]
# if lowest_price_index == 0:
# 	Website = "Ebay"
# 	url = Ebay_APIresponse['url']
# elif lowest_price_index == 1:
# 	website = "FlipKart"
# 	url = flipkart['link']
# else:
# 	website = "Amazon"
# 	url = amazon['url']
#
# print(amazon)
# print(Ebay_APIresponse)
# print(flipkart)
# time.sleep(10)
#
# print("lowest Pirce", lowest_price)
# print(website)
# print(url)

# ebayurl = f"https://ebay-search-result.p.rapidapi.com/search/iphone 14"
#
# ebayheaders = {
#             "X-RapidAPI-Key": "b6859e150fmsh54dc642c5225265p15910ejsn642549934c0e",
#             "X-RapidAPI-Host": "ebay-search-result.p.rapidapi.com"
#         	}
# Ebay_APIresponse = requests.get(ebayurl, headers=ebayheaders).json()['results']
# print(Ebay_APIresponse)
# print(Ebay_APIresponse[1]['rating'])
# print(Ebay_APIresponse[2]['title'])
# print(Ebay_APIresponse[2]['image'])
# print(Ebay_APIresponse[3]['price'])
# print(Ebay_APIresponse[3]['url'])
import get_data 

headers = {
	'User-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
	}
url = 'https://stopcov.ge/en/'

p = get_data.CoronaParser(url, headers)
p.parse()




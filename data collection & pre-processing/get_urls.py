def get_url(url):
    soup = BeautifulSoup(open(url), 'html.parser')
    for div in soup.find_all("div", class_="product-compact__spacer"):
        i=0
        for href in div.find_all('a'):
            if(i<1):
                get_image_url(href.get('href'))
                i+=1

def get_image_url(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    imagefile = open('urls.txt','a')
    
    for img in soup.find_all("button", class_="bullet-clickable"):
        for src in img.find_all('img'):
            file = src.get('src').replace('?f=s', '')
            imagefile.write(file+'\n')
    imagefile.close()

if __name__ == '__main__':
	get_url('chairs/chairs2.html')
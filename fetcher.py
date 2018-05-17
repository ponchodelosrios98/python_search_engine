import urllib.request

def get_page(url):
    try:
        page = urllib.request.urlopen(url).read()
        return page.decode('utf-8')
    except:
        return ""
    return ""
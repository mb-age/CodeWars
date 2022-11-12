def domain_name(url):
    if '//' in url:
        url = url[url.find('//')+2:]
    if 'www.' in url:
        url = url[url.find('www.')+4:]
    if '/' in url:
        url = url[:url.find('/')]
    if '.' in url:
        url = url[:url.find('.')]
    return url
import webbrowser
print("What you want to search on internet?")
searchOnInternet = input("Enter here: ")
#searchUrl = ('https://www.google.com.tr/search?client=opera&q=' + searchOnInternet + '&sourceid=opera&ie=UTF-8&oe=UTF-8')
#searchUrl = ('https://duckduckgo.com/?q=' + searchOnInternet + '&t=h_&ia=videos')      #DuckDuckGo
#searchUrl = ('yandex.com/search/?lr=11505&oprnd=2855927709&text=' + searchOnInternet)      #Yandex
#searchUrl = ('https://search.yahoo.com/search?p=' + searchOnInternet + '&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8')      #Yahoo
#searchUrl = ('https://www.bing.com/search?q=' + searchOnInternet + '&qs=n&form=QBLH&sp=-1&pq=efe&sc=8-3&sk=&cvid=3FCCB84D5F8241FC8D8AF538B77C3D02')      #Bing
webbrowser.open(searchUrl)

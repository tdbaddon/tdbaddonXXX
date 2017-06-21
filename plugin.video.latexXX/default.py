import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin

AddonTitle     = "LatexXX"
addon_id       = 'plugin.video.latexXX'
ADDON          = xbmcaddon.Addon(id=addon_id)
dialog         = xbmcgui.Dialog()
addon_fanart   = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
next_icon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/next.png'))
search_icon    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/search.png'))

def CATEGORIES():

    url            = 'http://www.thelatextube.com'

    addDir("[B][COLOR white]SEARCH[/COLOR][/B]",url,5,search_icon,addon_fanart,'')

    r=requests.get('http://www.thelatextube.com/tubex/categories/')
    match=re.compile('<span class="video">(.+?)<div class="text-center">',re.DOTALL).findall(r.content)
    for item in match:
        name=re.compile('title="(.+?)"').findall(item)[0]
        image=re.compile('<img src="(.+?)" class="video-thumb" title=".+?"').findall(item)[0]
        url=re.compile('<a href="(.+?)">').findall(item)[0]
        image = "http://www.thelatextube.com" + str(image)
        url = "http://www.thelatextube.com" + str(url)
        if "tubex/category/latex" in url:
            url = 'http://www.thelatextube.com/tubex/category/latex/1'
        if "tubex/category/boots" in url:
            url = 'http://www.thelatextube.com/tubex/category/boots/1'
        if "tubex/category/leather" in url:
            url = 'http://www.thelatextube.com/tubex/category/leather/1'
        if "tubex/category/pvc" in url:
            url = 'http://www.thelatextube.com/tubex/category/pvc/1'
        if "tubex/category/shiny" in url:
            url = 'http://www.thelatextube.com/tubex/category/shiny/1'
        addDir('[B][COLOR pink]' + name + '[/COLOR][/B]',url,1,image,addon_fanart,'')

def GET_CONTENT(url):

    checker = url
    r=requests.get(url)
    match=re.compile('deo">(.+?)<span class="vi',re.DOTALL).findall(r.content)
    for item in match:
        title=re.compile('title="(.+?)"').findall(item)[0]
        url=re.compile('<a href="(.+?)"').findall(item)[0]
        iconimage=re.compile('<img src="(.+?)" class="video-thumb"').findall(item)[0]
        name = "[COLOR pink]" + title + "[/COLOR]"
        name = name.replace('"','')
        image = "http://www.thelatextube.com" + str(iconimage)
        url = "http://www.thelatextube.com" + str(url)
        addItem(name,url,3,image,addon_fanart,'')

    try:
        a,b = checker.split('.com/')
        c,d,e,f = b.split('/')
        new = int(float(f)) + 1
        url = a + ".com/" + c + "/" +  d + "/" +  e + "/" +  str(new)
        addDir('[COLOR yellow]Next Page >>[/COLOR]',url,1,next_icon,addon_fanart,'')       
    except:pass

def SEARCH(name,url,iconimage):

    string =''
    keyboard = xbmc.Keyboard(string, 'Enter Search Term')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText().replace(' ','+')
        if len(string)>1:
            url = "http://www.thelatextube.com/tubex/index.php?term=" + string + '&c=0&b.x=0&b.y=0&r=search'
            GET_CONTENT(url)
        else: quit()

def PLAY_URL(name,url,iconimage):

	original = OPEN_URL(url)
	failed = 0
	try:
		a = re.compile('<embed src="(.+?)&',re.DOTALL).findall(original)[0]
		b = a.split("id=")[1]
		result = OPEN_URL('http://redtube.com/' + str(b))
		url = re.compile('<source src="(.+?)"',re.DOTALL).findall(result)[0]
		url = "http:" + url
	except: failed = 1
	
	if failed == 1:
		failed = 0
		try:
			url = re.compile("file: '(.+?)'",re.DOTALL).findall(original)
			a = str(url)
			a = a.replace("['",'').replace("']",'').replace('%3A%2F%2F','://').replace('%2F','/')
			b,c = a.split('?u=')
			d,e = c.split('&un')
			url = str(d)
		except: failed = 1

	if failed == 1:	
		dialog.ok("LatexXX","Error playing video, please select another.")
		quit()

	if len(url) < 10:
		dialog.ok("LatexXX","Error playing video, please select another.")
		quit()

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	xbmc.Player ().play(url, liz, False)

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       

def OPEN_URL(url):

    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link  

def addItem(name,url,mode,iconimage,fanart,description=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addDir(name,url,mode,iconimage,fanart,description=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1: GET_CONTENT(url)
elif mode==3: PLAY_URL(name,url,iconimage)
elif mode==5: SEARCH(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

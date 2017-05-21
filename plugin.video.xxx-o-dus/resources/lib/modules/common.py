"""
    Copyright (C) 2016 ECHO Coder

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
#Imports
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import urllib2,urllib
import time
import base64
import re
from HTMLParser import HTMLParser
import plugintools
import client
import kodi

AddonTitle     = "[COLOR red]XXX-O-DUS[/COLOR]"
dialog         = xbmcgui.Dialog()
addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
DATA_FOLDER    = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id))
SEARCH_FILE    = xbmc.translatePath(os.path.join(DATA_FOLDER , 'search.xml'))

def Sort_Links(s, single=None):

    dialog.ok("22", str(s))
    u = []
    for i in s:
        c = client.request(i, output='headers')
        checks = ['video','mpegurl']
        if any(f for f in checks if f in c['Content-Type']): u.append((i, int(c['Content-Length'])))

    u = sorted(u, key=lambda x: x[1])[::-1]
    if single == False:
        return u
    else:
        u = client.request(u[0][0], output='geturl')
        return u

def Auto_Play(u,iconimage,sorted=None):

    p = 0
    timer = 0
    
    if sorted == True:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        while not xbmc.Player().isPlayingVideo():
            try:
                if timer == 0:
                    liz = xbmcgui.ListItem(u[p][0],iconImage=iconimage, thumbnailImage=iconimage)
                    url = u[p][0]
                    liz.setPath(url)
                    xbmc.Player().play(url, liz, False)
                time.sleep(1)
                timer += 1
                if timer == 8:
                    try: xbmc.Player.stop()
                    except: pass
                    kodi.notify(msg='Link %s failed. Trying next link.' % (str(p+1)), duration=2000, sound=True)
                    timer = 0
                    p += 1
            except:
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                kodi.notify(msg='Failed to play %s' % u[p][0], duration=5000, sound=True)
                quit()
        xbmc.executebuiltin("Dialog.Close(busydialog)")
    else:
        while not xbmc.Player().isPlayingVideo():
            try:
                xbmc.executebuiltin("ActivateWindow(busydialog)")
                if timer == 0:
                    url = u[p]
                    import urlresolver
                    if urlresolver.HostedMediaFile(url).valid_url(): 
                        url = urlresolver.HostedMediaFile(url).resolve()
                    liz = xbmcgui.ListItem(u[p],iconImage=iconimage, thumbnailImage=iconimage)
                    liz.setPath(url)
                    xbmc.Player().play(url, liz, False)
                time.sleep(1)
                timer += 1
                if timer == 30:
                    try: xbmc.Player.stop()
                    except: pass
                    kodi.notify(msg='Link %s failed. Trying next link.' % (str(p+1)), duration=2000, sound=True, icon_path=iconimage)
                    timer = 0
                    p += 1
            except:
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                kodi.notify(msg='Failed to play Link %s' % str(p), duration=5000, sound=True)
                quit()
        xbmc.executebuiltin("Dialog.Close(busydialog)")

def SEARCH_HISTORY(name,url):

    list = []
    
    mode = int(url)
    
    search_on_off  = plugintools.get_setting("search_setting")

    setting = "search_setting|SPLIT|" + search_on_off
    addDir('[COLOR pink][B]New Search...[/B][/COLOR]','null',mode,icon,fanart)
    addLink('[COLOR pink][B]Clear History[/B][/COLOR]','url',108,icon,fanart)
    addLink('[COLOR pink][B]Disable Search History[/B][/COLOR]',setting,109,icon,fanart)
    addLink('################## Recent Searches #########################','url',999,icon,fanart)

    f = open(SEARCH_FILE,mode='r'); msg = f.read(); f.close()
    msg = msg.replace('\n','')
    match = re.compile('<item>(.+?)</item>').findall(msg)
    for item in match:
        url=re.compile('<term>(.+?)</term>').findall(item)[0]
        if not url in str(list): addDir('[COLOR white]' + url + '[/COLOR]',url,mode,icon,fanart)
        list.append(url)

    SET_VIEW('list')

def GET_KODI_VERSION():

    xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
    version=float(xbmc_version[:4])
    if version >= 11.0 and version <= 11.9:
        codename = 'Eden'
    elif version >= 12.0 and version <= 12.9:
        codename = 'Frodo'
    elif version >= 13.0 and version <= 13.9:
        codename = 'Gotham'
    elif version >= 14.0 and version <= 14.9:
        codename = 'Helix'
    elif version >= 15.0 and version <= 15.9:
        codename = 'Isengard'
    elif version >= 16.0 and version <= 16.9:
        codename = 'Jarvis'
    elif version >= 17.0 and version <= 17.9:
        codename = 'Krypton'
    else: codename = "Decline"

    return codename

def SET_VIEW(name):

    list_mode   = plugintools.get_setting("list_view")
    thumb_mode  = plugintools.get_setting("thumb_view")

    kodi_name = GET_KODI_VERSION()

    if (list_mode == '0') or (list_mode == 0):
        if kodi_name == "Jarvis":
            list_mode='50'
        elif kodi_name == "Krypton":
            list_mode='55'
        else: list_mode='50'

    if (thumb_mode == '0') or (thumb_mode == 0):
        if kodi_name == "Jarvis":
            thumb_mode='500'
        elif kodi_name == "Krypton":
            thumb_mode='52'
        else: thumb_mode='500'

    if name == 'list':
        xbmc.executebuiltin(('Container.SetViewMode(%s)') % (list_mode))
    elif name == 'thumbs':
        xbmc.executebuiltin(('Container.SetViewMode(%s)') % (thumb_mode))
    else:
        xbmc.executebuiltin(('Container.SetViewMode(%s)') % (list_mode))
            
def GET_M3U_LIST(url):

    # req = urllib2.Request(url)
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    # response = urllib2.urlopen(req)
    # link=response.read()
    # response.close()
    # link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
    # url = re.compile('<link>(.+?)</link>').findall(link)[0]

    response = open_url(url)
    response = response.replace('#AAASTREAM:','#A:')
    response = response.replace('#EXTINF:','#A:')
    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)
    li = []
    for params, display_name, url in matches:
        item_data = {"params": params, "display_name": display_name, "url": url}
        li.append(item_data)
    m3u_list = []
    for channel in li:
        item_data = {"display_name": channel["display_name"], "url": channel["url"]}
        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
        for field, value in matches:
            field = field.replace('-',''); field = field.lstrip(); field = field.rstrip()
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        m3u_list.append(item_data)

    namelist = []; urllist = []; combinedlist = []
    for channel in sorted(m3u_list):
        name = GetEncodeString(channel["display_name"])
        url = GetEncodeString(channel["url"])
        name = name.replace('-',''); name = name.strip(); name = name.rstrip(); name = re.sub('[^A-Za-z0-9 ]+', '', name)
        name = name.lstrip(' ')
        namelist.append(name)
        urllist.append(url)
        combinedlist = list(zip(namelist,urllist))

    for name,url in sorted(combinedlist):
        if not '=' in name:
            if not 'http://exabytetv.info/exabytetv.mp4' in url:
                addLink('[COLOR pink]'+name.title()+'[/COLOR]',url,996,icon,fanart)

def GetEncodeString(str):
    try:
        import chardet
        str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
    except:
        try:
            str = str.encode("utf-8")
        except:
            pass
    return str

def CLEANUP(text):

    text = str(text)
    text = text.replace('\\r','')
    text = text.replace('\\n','')
    text = text.replace('\\t','')
    text = text.replace('\\','')
    text = text.replace('<br />','\n')
    text = text.replace('<hr />','')
    text = text.replace('&#039;',"'")
    text = text.replace('&quot;','"')
    text = text.replace('&rsquo;',"'")
    text = text.replace('&amp;',"&")
    text = text.replace('&#39;',"'")
    text = text.replace('&#8211;',"&")
    text = text.replace('&#8217;',"'")
    text = text.replace('&#038;',"&")
    text = text.lstrip(' ')
    text = text.lstrip('    ')

    return text

def TextBoxes(announce):
    class TextBox():
        WINDOW=10147
        CONTROL_LABEL=1
        CONTROL_TEXTBOX=5
        def __init__(self,*args,**kwargs):
            xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
            self.win=xbmcgui.Window(self.WINDOW) # get window
            xbmc.sleep(500) # give window time to initialize
            self.setControls()
        def setControls(self):
            self.win.getControl(self.CONTROL_LABEL).setLabel('[COLOR red]XXX-O-DUS[/COLOR]') # set heading
            try: f=open(announce); text=f.read()
            except: text=announce
            self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
            return
    TextBox()
    while xbmc.getCondVisibility('Window.IsVisible(10147)'):
        time.sleep(.5)

def _get_keyboard( default="", heading="", hidden=False ):
    """ shows a keyboard and returns a value """
    keyboard = xbmc.Keyboard( default, heading, hidden )
    keyboard.doModal()
    if ( keyboard.isConfirmed() ):
        return unicode( keyboard.getText(), "utf-8" )
    return default

def GET_LUCKY():

    import random
    lucky = random.randrange(10)
    
    dp = xbmcgui.DialogProgress()
    
    if lucky == 1:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]We are getting the moisturiser.[/COLOR]','[COLOR azure]Do you have the wipes ready?[/COLOR]' )
    elif lucky == 2:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]I am just taking off my pants.[/COLOR]','[COLOR azure]Darn belt![/COLOR]' )
    elif lucky == 3:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Are the curtains closed?[/COLOR]','[COLOR azure]Oh baby its cold outside![/COLOR]' )
    elif lucky == 4:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]This is my fifth time today.[/COLOR]','[COLOR azure]How about you?[/COLOR]' )
    elif lucky == 5:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Please no buffer, please no buffer![/COLOR]')
    elif lucky == 6:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]I think I am going blind :-/[/COLOR]','[COLOR azure]Oh no, just something in my eye.[/COLOR]' )
    elif lucky == 7:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Did I turn the oven off?[/COLOR]','[COLOR azure]It can wait![/COLOR]' )
    elif lucky == 8:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Your video is coming. Are you?[/COLOR]','[COLOR azure]Do you get it?[/COLOR]' )
    elif lucky == 9:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Kodi does not save your browsing history :-D[/COLOR]','[COLOR azure]Thats lucky isnt it :-)[/COLOR]' )
    else:
        dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]There are more XXX addons by ECHO.[/COLOR]','[COLOR azure]Just so you know.[/COLOR]' )

    return dp

def open_url(url):
    req = urllib2.Request(url)
    if not "referer" in url.lower():
        req.add_header('Referer', 'https://www.google.com/')
    if not "user-agent" in url.lower():
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    response = urllib2.urlopen(req, timeout = 10)
    link=response.read()
    response.close()
    return link

def addDir(name,url,mode,iconimage,fanartimage):

    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanartimage="+urllib.quote_plus(fanartimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanartimage )
    liz.setProperty( "icon_Image", iconimage )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name,url,mode,iconimage,fanartimage):

    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanartimage="+urllib.quote_plus(fanartimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanartimage )
    liz.setProperty( "icon_Image", iconimage )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def replaceHTMLCodes(txt):
    # Code from Lambdas ParseDOM file.
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    txt = txt.strip()
    return txt

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

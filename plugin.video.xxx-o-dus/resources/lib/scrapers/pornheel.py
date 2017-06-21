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
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs,urlparse
import urllib2,urllib
import time
import re
import json
from resources.lib.modules  import client
from resources.lib.modules  import dom_parser2
from resources.lib.modules  import common
from resources.lib.modules  import plugintools
import datetime

#Default veriables
AddonTitle     = "[COLOR red]XXX-O-DUS[/COLOR]"
dialog         = xbmcgui.Dialog()
addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/pornheel/fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/pornheel/icon.png'))
BASE           = 'http://x.ultra-vid.com/'
HISTORY_FILE   = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'history.xml'))
FAVOURITES_FILE= xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'favourites.xml'))

def MENU(url=None):
     
    u = client.request(url)
    r = dom_parser2.parse_dom(u, 'article')
    if r:
        for i in r:
            url = re.compile('<h3 class="entry-title"><a href="(.+?)"').findall(i.content)[0].encode('utf-8')
            name = re.compile('<h3 class="entry-title"><a href=".+?".+?>(.+?)</a>').findall(i.content)[0].encode('utf-8')
            iconimage = re.compile('<img src=\"([^"]+)').findall(i.content)[0].encode('utf-8')
            url = '%s|SPLIT|%s|SPLIT|%s' % (name,url,iconimage)
            common.addLink(name,url,731,iconimage,fanart)
        
        try:
            np = re.compile('<link rel="next" href="(.+?)"/>').findall(u)[0]
            common.addDir('Next Page -->',np,730,icon,fanart)
        except: pass

    common.SET_VIEW('thumbs')

def PLAY_URL(name,url,iconimage):
    
    hello = 1
    xbmc.executebuiltin("ActivateWindow(busydialog)")

    name,url,iconimage = url.split('|SPLIT|')

    r = client.request(url)

    s = re.findall('<a href="http:\/\/securely.link\/(.+?)" target="(.+?)"><\/a>', r) + re.findall('<a href="http:\/\/securely.link\/(.+?)" target="_blank">(.+?)<\/a>', r)
    s = [(urlparse.urljoin('http://securely.link/',a[0]),a[1].replace('_blank','Default')) for a in s if ('Streaming' in a[1])]

    auto_on_off  = plugintools.get_setting("film_auto")

    if auto_on_off == 'true':
        s = [client.request(i[0], output='geturl') for i in s if 'img' not in i]
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        common.Auto_Play(s,iconimage,sorted=False)
    else:
        streamname = []
        streamurl  = []
        
        for a,b in s:
            if not a in streamurl:
                if 'streaming ' in b.lower():
                    b = b.split('Streaming ')[1]
                    try: b = b.split('<')[0]
                    except: pass
                streamname.append(b)
                streamurl.append(a)
            
        xbmc.executebuiltin("Dialog.Close(busydialog)")

        select = dialog.select(name,streamname)
        if select < 0:
            quit()
        else:
            url = client.request(streamurl[select], output='geturl', referer=url)
            import urlresolver
            url = urlresolver.HostedMediaFile(url).resolve()
            liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
            xbmc.Player ().play(url, liz, False)

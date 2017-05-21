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
import re
import urlparse
import json
import urlresolver
from resources.lib.modules  import dom_parser2
from resources.lib.modules  import common
from resources.lib.modules  import plugintools
import datetime

#Default veriables
AddonTitle     = "[COLOR red]XXX-O-DUS[/COLOR]"
dialog         = xbmcgui.Dialog()
addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/freeomovie/fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/freeomovie/icon.png'))
BASE           = 'http://www.freeomovie.com'
HISTORY_FILE   = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'history.xml'))
FAVOURITES_FILE= xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'favourites.xml'))


def MENU(url=None):

    if url == 'None': url = BASE
    r = common.open_url(url)
    s = re.compile('<li><a href="(.+?)" rel="tag">(.+?)</a></li>').findall(r)
    
    if s:
        for url,name in s:
            common.addDir(name,url,722,icon,fanart)

    common.SET_VIEW('list')

def CATS(url=None):
     
    if url == 'None': url = BASE
    r = common.open_url(url)
    s = dom_parser2.parse_dom(r, 'div', {'class': 'postbox'})

    for i in s:
        name = dom_parser2.parse_dom(i.content, 'a', req='title')[0][0]['title'].encode('utf-8')
        name = common.strip_tags(name)
        url = dom_parser2.parse_dom(i.content, 'a')[0][0]['href'].encode('utf-8')
        iconimage = re.compile('src="(.+?)"').findall(i.content)[0].encode('utf-8')
        url = ('%s|SPLIT|%s|SPLIT|%s' % (name,url,iconimage))
        common.addLink(name,url,721,iconimage,fanart)

    try:
        np = dom_parser2.parse_dom(r, 'a', {'class': 'nextpostslink'})[0][0]['href']
        common.addDir('Load More...',str(np),722,icon,fanart)
    except: common.addLink('No more results found!','None',999,icon,fanart)

    common.SET_VIEW('thumbs')

def PLAY_URL(name,url,iconimage):
    
    dp = common.GET_LUCKY()
    name,url,iconimage = url.split('|SPLIT|')
    r = common.open_url(url)

    i = re.compile('URL\[\]=([^"]+)" rel="countrycontainer">',re.DOTALL).findall(r)

    check = ['flashx','streamcloud','streamin','openload','thevideo','datoporn']

    urllist = []

    for url2 in i:
        for a in check:
            if a in url2:
                urllist.append(url2)

    if len(urllist) == 0:
        dialog.ok(AddonTitle, 'Sorry, no links could be found for this video.'); quit()
    elif len(urllist) == 1:
        url = urllist[0]
    else:
        auto_on_off  = plugintools.get_setting("film_auto")
        if auto_on_off == 'true':
            dp.close()
            common.Auto_Play(urllist,iconimage,sorted=False)
            quit()
        else:
            domains = []
            urls    = []
            for link in urllist:
                domain = urlparse.urlsplit(link)[1].split(':')[0]
                if 'www.' in domain: domain=domain.replace('www.','')
                try: domain = domain.split('.')[0]
                except: pass
                domains.append(domain.title())
                urls.append(link)
                
            select = dialog.select(name,domains)
            if select < 0:
                quit()
            else:
                url = urls[select]
    url = urlresolver.HostedMediaFile(url).resolve()
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    dp.close()
    xbmc.Player ().play(url, liz, False)

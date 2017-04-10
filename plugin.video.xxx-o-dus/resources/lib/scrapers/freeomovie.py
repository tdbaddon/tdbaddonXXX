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
    s = dom_parser2.parse_dom(r, 'div', {'class': 'postbox'})

    for i in s:
        name = dom_parser2.parse_dom(i.content, 'a', req='title')[0][0]['title'].encode('utf-8')
        name = common.strip_tags(name)
        url = dom_parser2.parse_dom(i.content, 'a')[0][0]['href'].encode('utf-8')
        iconimage = dom_parser2.parse_dom(i.content, 'img')[0][0]['src'].encode('utf-8')
        url = ('%s|SPLIT|%s|SPLIT|%s' % (name,url,iconimage))
        common.addLink(name,url,721,iconimage,fanart)

    try:
        np = dom_parser2.parse_dom(r, 'a', {'class': 'nextpostslink'})[0][0]['href']
        common.addDir('Load More...',str(np),720,icon,fanart)
    except: common.addLink('No more results found!','None',999,icon,fanart)

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

    choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR pink]Watch Video[/COLOR]','[COLOR pink]Add to Favourites[/COLOR]','[COLOR pink]Download Video[/COLOR]'])

    if choice == 1:
        a=open(FAVOURITES_FILE).read()
        b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(name)+'</name>\n<link>'+str(url)+'</link>\n<site>Freeomovie</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
        f= open(FAVOURITES_FILE, mode='w')
        f.write(str(b))
        f.close()
        dp.close()
        dialog.ok(AddonTitle, "[COLOR pink]" + name + " has been added to your favourites. You can access your favourites on the main menu.[/COLOR]")
        quit()
    
    elif choice == 2:
        try:
            download_location   = plugintools.get_setting("download_location")
            download_folder = xbmc.translatePath(download_location)
            _in = url
            name = name.replace(' ','_').replace('[COLOR','').replace('[/COLOR','').replace('[I]','').replace(']','').replace('|','').replace('%','').replace('-','').replace('[/I','').replace('[/B','').replace('[','').replace('/','').replace(':','')
            _out = download_folder + name + '.mp4'
            dp.close()
            a=open(DOWNLOADS_FILE).read()
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(_out)+'</name>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(DOWNLOADS_FILE, mode='w')
            f.write(str(b))
            f.close()
            downloader.download(_in,_out,dp=None)
            dialog.ok(AddonTitle, "[COLOR pink]Your video has been successfully downloaded and can be viewed from the Your Downloads section on the main menu.[/COLOR]") 
        except: 
            try:
                os.remove(_out)
            except: pass
            dp.close()
            dialog.ok(AddonTitle, "[COLOR pink]Sorry, there was an error trying to download the video.[/COLOR]")
            quit()
    
    elif choice == 0:
        history_on_off  = plugintools.get_setting("history_setting")
        if history_on_off == "true":    
            date_now = datetime.datetime.now().strftime("%d-%m-%Y")
            time_now = datetime.datetime.now().strftime("%H:%M")
            a=open(HISTORY_FILE).read()
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<date>'+str(date_now)+'</date>\n<time>'+str(time_now)+'</time>\n<name>'+str(name)+'</name>\n<link>'+str(url)+'</link>\n<site>Freeomovie</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(HISTORY_FILE, mode='w')
            f.write(str(b))
            f.close()

        url = urlresolver.HostedMediaFile(url).resolve()
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        dp.close()
        xbmc.Player ().play(url, liz, False)

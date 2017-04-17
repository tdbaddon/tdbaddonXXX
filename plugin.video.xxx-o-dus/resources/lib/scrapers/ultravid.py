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
import json
from resources.lib.modules  import dom_parser2
from resources.lib.modules  import common
from resources.lib.modules  import plugintools
import datetime

#Default veriables
AddonTitle     = "[COLOR red]XXX-O-DUS[/COLOR]"
dialog         = xbmcgui.Dialog()
addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/ultravid/fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/ultravid/icon.png'))
BASE           = 'http://x.ultra-vid.com/'
HISTORY_FILE   = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'history.xml'))
FAVOURITES_FILE= xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'favourites.xml'))

def MENU(url=None):
     
    lists = []
    display = 0
    
    if url == 'None': i = 1
    else: i = int(url)
    
    end = i + 9
    
    while i <= end:
        if i == 1: response = common.open_url(BASE)
        else: response = common.open_url(BASE + 'page/%s/' % str(i))
        lists = dom_parser2.parse_dom(response, 'div', {'class': re.compile('home_post_cont.+?post_box')})
        i = i + 1
        if lists:
            for item in lists:
                try:
                    url = dom_parser2.parse_dom(item.content, 'a', req='href')[0][0]['href']
                    iconimage = dom_parser2.parse_dom(item.content, 'img', req='src')[0][0]['src']
                    name = dom_parser2.parse_dom(item.content, 'img', req='title')[0][0]['title']
                    name = re.findall('e\&quot;\&gt\;([^&]+)&',name)[0]; url = ('%s|SPLIT|%s|SPLIT|%s' % (name,url,iconimage))
                    display + 1
                    common.addLink(name,url,711,iconimage,fanart)
                except: pass
    if (lists and display >= 1):
        next = end + 1
        common.addDir('Load More...',str(next),710,icon,fanart)
    else: common.addLink('No more results found!','None',999,icon,fanart)

def PLAY_URL(name,url,iconimage):
    
    dp = common.GET_LUCKY()
    name,url,iconimage = url.split('|SPLIT|')

    response = common.open_url(url)

    url = re.compile('<iframe.+?(?:http)([^"]*)',re.I).findall(response)[0]; url = ('%s%s' % ('http',url))

    import urlresolver

    choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR pink]Watch Video[/COLOR]','[COLOR pink]Add to Favourites[/COLOR]','[COLOR pink]Download Video[/COLOR]'])

    if choice == 1:
        a=open(FAVOURITES_FILE).read()
        b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(name)+'</name>\n<link>'+str(url)+'</link>\n<site>Ultra-Vid</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
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
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<date>'+str(date_now)+'</date>\n<time>'+str(time_now)+'</time>\n<name>'+str(name)+'</name>\n<link>'+str(url)+'</link>\n<site>Ultra-Vid</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(HISTORY_FILE, mode='w')
            f.write(str(b))
            f.close()

        url = urlresolver.HostedMediaFile(url).resolve()
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        dp.close()
        xbmc.Player ().play(url, liz, False)
    else:
        dp.close()
        quit()

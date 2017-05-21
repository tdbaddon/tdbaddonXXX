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
import base64
import re
from resources.lib.modules  import client
from resources.lib.modules  import dom_parser2
from resources.lib.modules  import kodi
from resources.lib.modules  import adultresolver
adultresolver = adultresolver.streamer()
from resources.lib.modules  import common
from resources.lib.modules  import downloader
from resources.lib.modules  import plugintools
import datetime

#Default veriables
AddonTitle        = "[COLOR red]XXX-O-DUS[/COLOR]"
dialog            = xbmcgui.Dialog()
addon_id          = 'plugin.video.xxx-o-dus'
fanart            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/art/fourtube/fanart.jpg'))
icon              = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/fourtube/icon.png'))
HISTORY_FILE      = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'history.xml'))
FAVOURITES_FILE   = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'favourites.xml'))
DOWNLOADS_FILE    = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'downloads.xml'))
DATA_FOLDER       = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id))
SEARCH_FILE       = xbmc.translatePath(os.path.join(DATA_FOLDER , 'search.xml'))

def MAIN_MENU():

    common.addDir("[COLOR red][B]SEARCH[/B][/COLOR]","url",324,icon,fanart)

    u = client.request('https://www.4tube.com/tags')
    r = dom_parser2.parse_dom(u, 'div', {'class': 'col'})

    if r:
        for i in r:
            url = re.compile('href="(.+?)"').findall(i.content)[0]
            name = re.compile('title="(.+?)"').findall(i.content)[0]
            number = re.compile('<i class="icon icon-video"></i>(.+?)<').findall(i.content)[0]
            iconimage = re.compile('original="(.+?)"').findall(i.content)[0]
            name = '[COLOR white]%s - %s Videos[/COLOR]' % (name.title(),number)
            common.addDir(name,url,321,iconimage,fanart)
            
    common.SET_VIEW('list')

def GET_CONTENT(url):

    nextpage = 0
    try:
        a,url = url.split('|')
    except: nextpage = 1

    checker = url

    u = client.request(url)

    r = dom_parser2.parse_dom(u, 'div', {'class': re.compile('col\sthumb_video')})
    if r:
        for i in r:
            try:
                url = re.compile('href="(.+?)"').findall(i.content)[0]
                name = re.compile('class="thumb-link" title="(.+?)"').findall(i.content)[0]
                iconimage = re.compile('original="(.+?)"').findall(i.content)[0]
                try: quality = re.compile('<li class="topHD">(.+?)<').findall(i.content)[0]
                except: quality = 'SD'
                try: duration = re.compile('<li class="duration-top">(.+?)<').findall(i.content)[0]
                except: duration = 'Unknown'
                url = urlparse.urljoin('https://www.4tube.com',url)
                url = name + "|SPLIT|" + url + "|SPLIT|" + iconimage
                name = '[COLOR white]%s - %s - %s[/COLOR]' % (quality,name,duration)
                common.addLink(name,url,323,iconimage,fanart)
            except: pass
            
    if nextpage == 1:
        try:
            np=re.compile('href="([^>]+)"\sid').findall(u)[0]
            common.addDir('[COLOR white]Next Page >>[/COLOR]',np,321,icon,fanart)       
        except: pass

    common.SET_VIEW('thumbs')

def SEARCH_DECIDE():

    search_on_off  = plugintools.get_setting("search_setting")
    if search_on_off == "true":
        name = "null"
        url = "322"
        common.SEARCH_HISTORY(name,url)
    else:
        url = "null"
        SEARCH(url)

def SEARCH(url):

    if url == "null":
        string =''
        keyboard = xbmc.Keyboard(string, 'Enter Search Term')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_on_off  = plugintools.get_setting("search_setting")
            if search_on_off == "true":
                term = keyboard.getText()
                a=open(SEARCH_FILE).read()
                b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<term>'+str(term)+'</term>\n</item>\n')
                f= open(SEARCH_FILE, mode='w')
                f.write(str(b))
            string = keyboard.getText().replace(' ','+')
            if len(string)>1:
                url = "https://www.4tube.com/search?q=" + string.lower()
                GET_CONTENT(url)
            else: quit()
    else:
        string = url.replace(' ','+')
        url = "https://www.4tube.com/search?q=" + string.lower()
        GET_CONTENT(url)

def PLAY_URL(name,url,iconimage):

    name,url,iconimage = url.split('|SPLIT|')
    name = name.replace('[COLOR white]','').replace('[/COLOR]','').replace(' - ','')
    ref_url = url
    dp = common.GET_LUCKY()
    url = adultresolver.resolve(url)
    if url == None:
        kodi.notify(msg='Sorry no link found.', duration=2000, sound=True, icon_path=iconimage)
        quit()
        
    auto_play = plugintools.get_setting("extras_setting")
    
    if auto_play == 'false': choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR pink]Watch Video[/COLOR]','[COLOR pink]Add to Favourites[/COLOR]','[COLOR pink]Download Video[/COLOR]'])
    else: choice = 0
    
    if choice == 1:
        a=open(FAVOURITES_FILE).read()
        b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(name)+'</name>\n<link>'+str(url)+'</link>\n<site>4Tube</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
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
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<date>'+str(date_now)+'</date>\n<time>'+str(time_now)+'</time>\n<name>'+str(name)+'</name>\n<link>'+str(url)+'</link>\n<site>4Tube</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(HISTORY_FILE, mode='w')
            f.write(str(b))
            f.close()

        url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        dp.close()
        xbmc.Player ().play(url, liz, False)
        quit()
    else:
        dp.close()
        quit()
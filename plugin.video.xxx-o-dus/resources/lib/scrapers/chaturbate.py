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
from resources.lib.modules  import common
from resources.lib.modules  import plugintools
import datetime

#Default veriables
AddonTitle     = "[COLOR red]XXX-O-DUS[/COLOR]"
dialog         = xbmcgui.Dialog()
addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/icon.png'))
next_icon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/next.png'))
twitter_icon   = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/twitter.png'))
pc_icon        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/pc.png'))
featured_icon  = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/featured.png'))
female_icon    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/female.png'))
male_icon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/male.png'))
couple_icon    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/couples.png'))
trans_icon     = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/trans.png'))
BASE           = 'https://chaturbate.com'
F4M            = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.f4mTester'))
HISTORY_FILE   = xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'history.xml'))
FAVOURITES_FILE= xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'favourites.xml'))
CHATURBATE_FILE= xbmc.translatePath(os.path.join('special://profile/addon_data/' + addon_id , 'chaturbate.xml'))

def MAIN_MENU():

    chat_on_off  = 'true'
    chat_on_off  = plugintools.get_setting("chaturbate_setting")

    if chat_on_off == 'true': common.addDir("[COLOR pink]View Monitored Performers[/COLOR]","url",24,icon,fanart)
    else: common.addLink("[COLOR pink]Enable Performer Monitoring[/COLOR]","url",106,icon,fanart)
    result = common.open_url(BASE)
    
    match = re.compile('<ul class="sub-nav">(.+?)<div class="content">',re.DOTALL).findall(result)
    string = str(match)
    match2 = re.compile("<li(.+?)</li>",re.DOTALL).findall(string)
    fail = 0
    videos = 0
    common.addDir('[COLOR white]VIEW BY TAGS[/COLOR]','url',25,icon,fanart)
    for item in match2:
        url=re.compile('<a href="(.+?)">.+?</a>').findall(item)[0]
        title=re.compile('<a href=".+?">(.+?)</a>').findall(item)[0]
        url3 = url
        url4 = url3.replace('\\','')
        url = "http://www.chaturbate.com" + url4
        if "featured" in title.lower():
            name = "[COLOR white]" + title + "[/COLOR]"
            common.addDir(name,url,21,featured_icon,fanart)
        elif "female" in title.lower():
            name = "[COLOR white]Females[/COLOR]"
            common.addDir(name,url,21,female_icon,fanart)
        elif "male" in title.lower():
            name = "[COLOR white]Males[/COLOR]"
            common.addDir(name,url,21,male_icon,fanart)
        elif "couple" in title.lower():
            name = "[COLOR white]Couples[/COLOR]"
            common.addDir(name,url,21,couple_icon,fanart)
        elif "trans" in title.lower():
            name = "[COLOR white]Transexual[/COLOR]"
            common.addDir(name,url,21,trans_icon,fanart)


    common.addLink("[COLOR pink] ################# RANDOM PICKS #################[/COLOR]","url",999,twitter_icon,fanart)

    POP_NOW(BASE)

    kodi_name = common.GET_KODI_VERSION()

    if kodi_name == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif kodi_name == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')

def MONITORING():

    common.addLink("[COLOR orangered]Disable Performer Monitoring[/COLOR]","url",106,icon,fanart)

    if os.path.exists(CHATURBATE_FILE):
        f = open(CHATURBATE_FILE,mode='r'); msg = f.read(); f.close()
        if not '<item>' in msg:
            common.addLink('[COLOR pink]No Performers beging Monitored.[/COLOR]','url',999,icon,fanart)
        namelist = []; urllist = []; iconlist = []; countlist = []; combinedlists=[]
        msg = msg.replace('\n','')
        match = re.compile('<item>(.+?)</item>').findall(msg)
        for item in match:
            title=re.compile('<name>(.+?)</name>').findall(item)[0]
            link=re.compile('<url>(.+?)</url>').findall(item)[0]
            iconimage=re.compile('<icon>(.+?)</icon>').findall(item)[0]
            try:
                r = common.open_url(link)
                if not '<p><strong>Room is currently offline</strong></p>' in r:
                    try: 
                        iconimg=re.compile("posterUrl.+?\'([^']+)").findall(r)[0]
                        iconimg = iconimage + '1'
                    except: iconimg = iconimage
                    namelist.append(title)
                    urllist.append(link)
                    iconlist.append(iconimg)
                    countlist.append('0')
                    combinedlists = list(zip(countlist,namelist,urllist,iconlist))
                else: 
                    namelist.append(title)
                    urllist.append(link)
                    iconlist.append(iconimage)
                    countlist.append('1')
                    combinedlists = list(zip(countlist,namelist,urllist,iconlist))
            except: 
                namelist.append(title)
                urllist.append(link)
                iconlist.append(iconimage)
                countlist.append('1')
                combinedlists = list(zip(countlist,namelist,urllist,iconlist))
                pass
    else: common.addLink('[COLOR pink]No Performers beging Monitored.[/COLOR]','url',999,icon,fanart)

    if combinedlists: 
        tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=False)
        for count,title,url,iconimage in tup:
            if count == '0':
                url2 = title + '|SPLIT|' + url + '|SPLIT|' + iconimage
                common.addLink('[COLOR pink][B]' + title + ' is online now![/B][/COLOR]',url2,23,iconimage,fanart)
            else: common.addLink(title + ' is offline!','url',999,iconimage,fanart)

def POP_NOW(url):

    i = 1
    result = common.open_url(url)
    match = re.compile('<ul class="list">(.+?)<ul class="paging">',re.DOTALL).findall(result)
    string = str(match)
    match2 = re.compile("<li>(.+?)</li>",re.DOTALL).findall(string)
    for item in match2:
        if i <= 7:
            try:
                title=re.compile('<a href=".+?"> (.+?)</a>').findall(item)[0]
                url=re.compile('<a href="(.+?)">.+?</a>').findall(item)[0]
                iconimage=re.compile('<img src="(.+?)"').findall(item)[0]
                try:
                    age=re.compile('<span class="age gender.+?">(.+?)</span>').findall(item)[0]
                except: age = "Unknown"
                if 'thumbnail_label_c_hd">' in item:
                    name = "[COLOR pink]HD[/COLOR][COLOR white] - " + title + " - Age " + age + "[/COLOR]"
                elif 'label_c_new' in item:
                    name = "[COLOR blue]NEW[/COLOR][COLOR white] - " + title + " - Age " + age + "[/COLOR]"
                else:
                    name = "[COLOR white]" + title + " - Age " + age + "[/COLOR]"
                url2 = title + '|SPLIT|' + url + '|SPLIT|' + iconimage
                common.addLink(name,url2,23,iconimage,fanart)
                i = i + 1
            except: pass

def TAGS():

    result = common.open_url('https://chaturbate.com/tags/')
    match = re.compile('<ul class="sub-nav">(.+?)</ul>',re.DOTALL).findall(result)
    string = str(match)
    match2 = re.compile("<li(.+?)</li>",re.DOTALL).findall(string)
    for item in match2:
        try:
            name=re.compile('<a href=".+?">(.+?)</a>').findall(item)[0]
            url=re.compile('<a href="(.+?)">.+?</a>').findall(item)[0]
            common.addDir('[COLOR white]' + name.title() + '[/COLOR]',url,26,icon,fanart)
        except: pass

def GET_TAGS(url):

    result = common.open_url('https://chaturbate.com' + url)
    match = re.compile('<span class="tag">(.+?)<span class="room_thumbnails">',re.DOTALL).findall(result)
    for item in match:
        try:
            name=re.compile('title="(.+?)"').findall(item)[0]
            url=re.compile('<a href="(.+?)"').findall(item)[0]
            viewers=re.compile('<span class="viewers">(.+?)</span>').findall(item)[0]
            rooms=re.compile('<span class="rooms">(.+?)</span>').findall(item)[0]            
            common.addDir('[COLOR white]' + name.title() + ' - ' + viewers + ' Viewers - ' + rooms + ' Rooms[/COLOR]','https://chaturbate.com'+url,21,icon,fanart)
        except: pass

def GET_CONTENT(url):

    checker = url
    result = common.open_url(url)
    match = re.compile('<ul class="list">(.+?)<div class="c-1 featured_blog_posts">',re.DOTALL).findall(result)
    string = str(match)
    match2 = re.compile("<li>(.+?)</li>",re.DOTALL).findall(string)
    for item in match2:
        try:
            title=re.compile('<a href=".+?"> (.+?)</a>').findall(item)[0]
            url=re.compile('<a href="(.+?)">.+?</a>').findall(item)[0]
            iconimage=re.compile('<img src="(.+?)"').findall(item)[0]
            try:
                age=re.compile('<span class="age gender.+?">(.+?)</span>').findall(item)[0]
            except: age = "Unknown"
            if 'thumbnail_label_c_hd">' in item:
                name = "[COLOR pink]HD[/COLOR][COLOR white] - " + title + " - Age " + age + "[/COLOR]"
            elif 'label_c_new' in item:
                name = "[COLOR blue]NEW[/COLOR][COLOR white] - " + title + " - Age " + age + "[/COLOR]"
            else:
                name = "[COLOR white]" + title + " - Age " + age + "[/COLOR]"
            url2 = title + '|SPLIT|' + url + '|SPLIT|' + iconimage
            common.addLink(name,url2,23,iconimage,fanart)
        except: pass
        
    try:
        np=re.compile('<ul class="paging">(.+?)</ul>',re.DOTALL).findall(result)
        for item in np:
            next=re.compile('<li><a href="(.+?)" class="next endless_page_link">next</a></li>').findall(item)[0]
            url = "http://chaturbate.com" + str(next)
            common.addDir('[COLOR pink]Next Page >>[/COLOR]',url,21,next_icon,fanart)       
    except:pass

    kodi_name = common.GET_KODI_VERSION()

    if kodi_name == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(500)')
    elif kodi_name == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(52)')
    else: xbmc.executebuiltin('Container.SetViewMode(500)')


def PLAY_URL(name,url,iconimage):
    
    dp = common.GET_LUCKY()

    name,url,iconimage = url.split('|SPLIT|')
    if not 'http' in url: orig_url = "http://www.chaturbate.com" + url
    else: orig_url = url

    result = common.open_url(orig_url)
    match = re.compile('<head>(.+?)</html>',re.DOTALL).findall(result)
    string = str(match).replace('\\','').replace('(','').replace(')','')
    url = "null"
    try:
        url = re.compile("src='([^']+)'").findall(string)[0]
    except:
        if '<p><strong>Room is currently offline</strong></p>' in string:
            dialog.ok(AddonTitle, "This room is currently offline.")
            quit()
        else:
            dialog.ok(AddonTitle, "Sorry, we are unable to find a playable link.")
            quit()
    url2 = url + '|Referer=' + orig_url

    chat_on_off  = plugintools.get_setting("chaturbate_setting")

    if chat_on_off == "true":
        if not os.path.isfile(CHATURBATE_FILE):
            f = open(CHATURBATE_FILE,'w'); f.write('#START OF FILE#'); f.close()
        a=open(CHATURBATE_FILE).read()
        if '<name>' + str(name) not in a: choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR pink]Watch Stream[/COLOR]','[COLOR pink]Notify me when ' + str(name) + ' is online.[/COLOR]'])
        else: choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR pink]Watch Stream[/COLOR]','[COLOR pink]Stop Notifications for ' + str(name) + '[/COLOR]'])
    else: choice = 0
    
    if choice == 1:
        if not str(name) in a:
            if not '#START' in a:
                f = open(CHATURBATE_FILE,'w'); f.write('#START OF FILE#'); f.close()
                a=open(CHATURBATE_FILE).read()
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(name)+'</name>\n<url>'+str(orig_url)+'</url>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(CHATURBATE_FILE, mode='w')
            f.write(str(b))
            f.close()
            dp.close()
            dialog.ok(AddonTitle, "[COLOR pink]You will be notified when " + str(name) + " is online.[/COLOR]")
            quit()
        else:
            b=a.replace('<item>\n<name>'+str(name)+'</name>\n','<old>\n<name>disabled</name>\n')
            f= open(CHATURBATE_FILE, mode='w')
            f.write(str(b))
            f.close()
            dp.close()
            dialog.ok(AddonTitle, "[COLOR pink]Notifications for " + str(name) + " have been disabled.[/COLOR]")
            quit()        
    elif choice == 0:
 
        choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR pink]Play High Bandwidth Stream[/COLOR]','[COLOR pink]Play Low Bandwidth Stream[/COLOR]'])
        if choice == 1: url2 = url2.replace('_fast_aac','_aac')
        history_on_off  = plugintools.get_setting("history_setting")
        if history_on_off == "true":    
            date_now = datetime.datetime.now().strftime("%d-%m-%Y")
            time_now = datetime.datetime.now().strftime("%H:%M")
            a=open(HISTORY_FILE).read()
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<date>'+str(date_now)+'</date>\n<time>'+str(time_now)+'</time>\n<name>'+str(name)+'</name>\n<link>'+str(url2)+'</link>\n<site>Chaturbate</site>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(HISTORY_FILE, mode='w')
            f.write(str(b))
            f.close()
        dp.close()
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        xbmc.Player ().play(url2, liz, False)
    else: 
        dp.close()
        quit()
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
from resources.lib.modules  import kodi
from resources.lib.modules  import log_utils
from resources.lib.modules  import client
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
    hd_on_odd  = plugintools.get_setting("chaturbate_hd")

    common.addLink("[COLOR white][B]Search for Model[/B][/COLOR]","url",28,icon,fanart)
    if chat_on_off == 'true': common.addDir("[COLOR white][B]View Monitored Models[/B][/COLOR]","url",24,icon,fanart)
    else: common.addLink("[COLOR white][B]Enable Performer Monitoring[/B][/COLOR]","url",106,icon,fanart)
    if hd_on_odd == 'true': common.addLink("[COLOR white][B]Only Show HD Cams:[/B][/COLOR] [COLOR white][B]ON[/B][/COLOR]","url",106,icon,fanart)
    else: common.addLink("[COLOR white][B]Only Show HD Cams:[/B][/COLOR] [COLOR white][B]OFF[/B][/COLOR]","url",106,icon,fanart)
    result = common.open_url(BASE)
    match = re.compile("<dd>(.+?)</dd>",re.DOTALL).findall(result)
    common.addDir('[COLOR white]View By Tags[/COLOR]','url',25,icon,fanart)
    for item in match:
        if not 'Tokens' in item:
            if 'title=' in item: section = re.compile('<a href=\"(.+?)\".+?>(.+?)</a>').findall(item)
            else: section = re.compile('<a href=\"(.+?)\">(.+?)</a>').findall(item)
            for url,name in section:
                common.addDir('[COLOR white]' + name + '[/COLOR]','https://chaturbate.com' + url,21,icon,fanart)

    common.SET_VIEW('list')

def MONITORING():

    dp = xbmcgui.DialogProgress()
    combinedlists=[]
    dp.create(AddonTitle,"[COLOR white]Currently Checking......[/COLOR]" )
    dp.update(0)
    i = 0
    common.addLink("[COLOR white][B]Disable Model Monitoring[/B][/COLOR]","url",106,icon,fanart)
    common.addLink("[COLOR white][B]Add Model by Username[/B][/COLOR]","url",27,icon,fanart)
    common.addLink("--------------------------------------------------------","url",999,icon,fanart)

    if os.path.exists(CHATURBATE_FILE):
        f = open(CHATURBATE_FILE,mode='r'); msg = f.read(); f.close()
        if not '<item>' in msg:
            common.addLink('[COLOR white]No Performers beging Monitored.[/COLOR]','url',999,icon,fanart)
        else:
            namelist = []; urllist = []; iconlist = []; countlist = []
            msg = msg.replace('\n','')
            match = re.compile('<item>(.+?)</item>').findall(msg)
            j = len(match)
            for item in match:
                title=re.compile('<name>(.+?)</name>').findall(item)[0]
                link=re.compile('<url>(.+?)</url>').findall(item)[0]
                iconimage=re.compile('<icon>(.+?)</icon>').findall(item)[0]
                progress = 100 * int(i)/int(j)
                dp.update(progress,"[COLOR white]Currently Checking " + title + "[/COLOR]","[COLOR white]Checked " + str(i) + " of " + str(j) + "[/COLOR]")
                try:
                    r = common.open_url(link)
                    if '.m3u8' in r:
                        namelist.append(title)
                        urllist.append(link)
                        iconlist.append(iconimage)
                        countlist.append('0')
                        combinedlists = list(zip(countlist,namelist,urllist,iconlist))
                    else: 
                        try: 
                            last_seen=re.compile("<dt>Last Broadcast:<\/dt><dd>(.+?)<\/dd>").findall(r)[0]
                        except: last_seen = "Unknown"
                        namelist.append(title + '|SPLIT|' + last_seen)
                        urllist.append(link)
                        iconlist.append(iconimage)
                        countlist.append('1')
                        combinedlists = list(zip(countlist,namelist,urllist,iconlist))
                except: 
                    namelist.append(title)
                    urllist.append(link)
                    iconlist.append(iconimage)
                    countlist.append('2')
                    combinedlists = list(zip(countlist,namelist,urllist,iconlist))
                    pass
                i += 1
    else: common.addLink('[COLOR white]No Performers beging Monitored.[/COLOR]','url',999,icon,fanart)

    if combinedlists: 

        progress = 100 * int(i)/int(j)
        dp.update(progress,"","[COLOR white]Checked " + str(i) + " of " + str(j) + "[/COLOR]")

        tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=False)
        for count,title,url,iconimage in tup:
            iconimage = 'https://roomimg.stream.highwebmedia.com/ri/%s.jpg' % title
            if count == '0':
                url2 = title + '|SPLIT|' + url + '|SPLIT|' + iconimage
                log_utils.log(iconimage, log_utils.LOGNOTICE)
                common.addLink('[COLOR white][B]' + title + ' is online now![/B][/COLOR]',url2,23,iconimage,fanart)
            elif count == '1':
                title,last_seen = title.split('|SPLIT|')
                url2 = title + '|SPLIT|' + url + '|SPLIT|' + iconimage
                common.addLink('[COLOR white][B]' + title + '[/B][/COLOR] - Offline! - Last Broadcast: ' + last_seen,url2,23,icon,fanart)
            else: common.addLink('[COLOR white][B]' + title + '[/B][/COLOR] - Error Checking!',url2,23,icon,fanart)
    
    dp.close()
    common.SET_VIEW('list')

def FOLLOW_USER():

    string =''
    keyboard = xbmc.Keyboard(string, 'Enter Username')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string)>1:
            string = string.replace(' ','_')
            xbmc.executebuiltin("ActivateWindow(busydialog)")
            a=open(CHATURBATE_FILE).read()
            if not '#START' in a:
                f = open(CHATURBATE_FILE,'w'); f.write('#START OF FILE#'); f.close()
            a=open(CHATURBATE_FILE).read()
            if '<name>'+string.lower()+'</name>' in a.lower():
                dialog.ok(AddonTitle, string + ' is already being monitored.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                quit()
            url = 'https://chaturbate.com/' + urllib.quote_plus(string)
            try:
                r = common.open_url(url)
            except:
                dialog.ok(AddonTitle, 'We could not find any model matching the username ' + string + '. Please check the username and try again.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                quit()
            if not 'Bio and Free Webcam' in r:
                dialog.ok(AddonTitle, 'We could not find any model matching the username ' + string + '. Please check the username and try again.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                quit()
            else:
                iconimg = 'https://roomimg.stream.highwebmedia.com/ri/' + string + '.jpg'
                a=open(CHATURBATE_FILE).read()
                b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(string)+'</name>\n<url>'+str(url)+'</url>\n<icon>'+str(iconimg)+'</icon>\n</item>\n')
                f= open(CHATURBATE_FILE, mode='w')
                f.write(str(b))
                f.close()
                dialog.ok(AddonTitle, string + ' has been added to the monitor list.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                xbmc.executebuiltin('Container.Refresh')
                quit()
        else:
            dialog.ok(AddonTitle, 'No username entered. Please try again.')
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            quit()

def SEARCH():

    string =''
    keyboard = xbmc.Keyboard(string, 'Enter Username')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string)>1:
            string = string.replace(' ','_')
            xbmc.executebuiltin("ActivateWindow(busydialog)")
            url = 'https://chaturbate.com/' + urllib.quote_plus(string)
            try:
                r = common.open_url(url)
            except:
                dialog.ok(AddonTitle, 'We could not find any model matching the username ' + string + '. Please check the username and try again.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                quit()
            if not 'Bio and Free Webcam' in r:
                dialog.ok(AddonTitle, 'We could not find any model matching the username ' + string + '. Please check the username and try again.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                quit()
            try: 
                iconimg = 'https://roomimg.stream.highwebmedia.com/ri/%s.jpg' % string
            except: iconimg = icon
            url2 = string + '|SPLIT|' + url + '|SPLIT|' + iconimg
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            PLAY_URL(string,url2,iconimg)
        else:
            dialog.ok(AddonTitle, 'No username entered. Please try again.')
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            quit()

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

    common.SET_VIEW('list')

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

    common.SET_VIEW('list')

def GET_CONTENT(url):

    hd_on_odd  = plugintools.get_setting("chaturbate_hd")

    checker = url
    result = common.open_url(url)
    match = re.compile('<ul class="list">(.+?)<div class="banner">',re.DOTALL).findall(result)
    string = str(match)
    match2 = re.compile('<li>(.+?)ewers',re.DOTALL).findall(string)
    for item in match2:
        try:
            title=re.compile('<a href=".+?"> (.+?)</a>').findall(item)[0]
            url=re.compile('<a href="(.+?)">.+?</a>').findall(item)[0]
            iconimage=re.compile('<img src="(.+?)"').findall(item)[0]
            try: age=re.compile('<span class="age gender.+?">(.+?)</span>').findall(item)[0]
            except: age = "Unknown"
            try: stats=re.compile('<li class="cams">(.+?)vi').findall(item)[0]
            except: stats = '? mins, ?'
            if 'thumbnail_label_c_hd">' in item: name = "[COLOR white]HD[/COLOR][COLOR white] - " + title + " - Age " + age + " - (" + stats + "viewers)[/COLOR]"
            elif 'label_c_new' in item: name = "[COLOR blue]NEW[/COLOR][COLOR white] - " + title + " - Age " + age + " - (" + stats + "viewers)[/COLOR]"
            else: name = "[COLOR white]" + title + " - Age " + age + " - (" + stats + "viewers)[/COLOR]"
            url2 = title + '|SPLIT|' + url + '|SPLIT|' + iconimage
            try: part1 = re.compile('<li title=".+?">(.+?)</li>').findall(item)[0].encode('utf-8')
            except: part1 = ''
            try: part2 = re.compile('<li class=".+?">(.+?)</li>').findall(item)[0]
            except: part2 = ''
            try:
                part1 = re.sub(r'<.+?>','',part1)
                part1 = part1.replace('\\x','REPL').replace('\\','')
                part1 = re.sub("""REPL[0-f][0-f]""",'',str(part1)) 
                part2 = re.sub(r'<.+?>','',part2)
                part2 = part2.replace('\\x','REPL')
                part2 = re.sub("""REPL[0-f][0-f]""",'',str(part2))
            except: pass
            try:
                part3,part4 = stats.split(',')
                description = ('Location: %s\nOnline: %s\nViewers: %s\n\n%s' % (part2,part3,part4,part1))
            except: description = ''
            if hd_on_odd == 'true':
                if 'thumbnail_label_c_hd">' in item: common.addLink(name,url2,23,iconimage,fanart,description)
            else: common.addLink(name,url2,23,iconimage,fanart,description)
        except: pass
        
    try:
        np=re.compile('<ul class="paging">(.+?)</ul>',re.DOTALL).findall(result)
        for item in np:
            next=re.compile('<li><a href="(.+?)" class="next endless_page_link">next</a></li>').findall(item)[0]
            url = "http://chaturbate.com" + str(next)
            common.addDir('[COLOR white]Next Page >>[/COLOR]',url,21,next_icon,fanart)       
    except:pass

    common.SET_VIEW('list')

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
        un = orig_url.replace('http://www.chaturbate.com/','').replace('https://www.chaturbate.com/','').replace('https://chaturbate.com/','').replace('http://chaturbate.com/','')
        un = un.rstrip('/')
        iconimage = 'https://roomimg.stream.highwebmedia.com/ri/%s.jpg' % un
    except: iconimage = icon    
    try:
        url = re.compile("source src='([^']+)'").findall(string)[0]
    except:
        if '<p><strong>Room is currently offline</strong></p>' in string:
            chat_on_off  = plugintools.get_setting("chaturbate_setting")
            if chat_on_off == "true":
                if not os.path.isfile(CHATURBATE_FILE):
                    f = open(CHATURBATE_FILE,'w'); f.write('#START OF FILE#'); f.close()
                a=open(CHATURBATE_FILE).read()
                if '<name>' + str(name) not in a: choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR red]ROOM CURRENTLY OFFLINE[/COLOR]','[COLOR white]Notify me when ' + str(name) + ' is online.[/COLOR]'])
                else: choice = dialog.select("[COLOR red]Please select an option[/COLOR]", ['[COLOR red]ROOM CURRENTLY OFFLINE[/COLOR]','[COLOR white]Stop Notifications for ' + str(name) + '[/COLOR]'])
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
                        dialog.ok(AddonTitle, "[COLOR white]You will be notified when " + str(name) + " is online.[/COLOR]")
                        quit()
                    else:
                        b=a.replace('<item>\n<name>'+str(name)+'</name>\n','<old>\n<name>disabled</name>\n')
                        f= open(CHATURBATE_FILE, mode='w')
                        f.write(str(b))
                        f.close()
                        dp.close()
                        dialog.ok(AddonTitle, "[COLOR white]Notifications for " + str(name) + " have been disabled.[/COLOR]")
                        quit()
                else: quit()
            else:
                dialog.ok(AddonTitle, "This room is currently offline.")
                quit()
        else:
            dialog.ok(AddonTitle, "Sorry, we are unable to find a playable link.")
            quit()
    url2 = url + '|Referer=' + orig_url

    subject = re.compile('default_subject:\s\"([^,]+)",').findall(result)[0]; subject = urllib.unquote_plus(subject)
    chat_on_off  = plugintools.get_setting("chaturbate_setting")

    if chat_on_off == "true":
        if not os.path.isfile(CHATURBATE_FILE):
            f = open(CHATURBATE_FILE,'w'); f.write('#START OF FILE#'); f.close()
        a=open(CHATURBATE_FILE).read()
        if '<name>' + str(name) not in a: choice = dialog.select("[COLOR white]" + subject + "[/COLOR]", ['[COLOR white]Watch Stream[/COLOR]','[COLOR white]View ' + str(name) + "'s Bio[/COLOR]",'[COLOR white]Notify me when ' + str(name) + ' is online.[/COLOR]'])
        else: choice = dialog.select("[COLOR white]" + subject + "[/COLOR]", ['[COLOR white]Watch Stream[/COLOR]','[COLOR white]View ' + str(name) + "'s Bio[/COLOR]",'[COLOR white]Stop Notifications for ' + str(name) + '[/COLOR]'])
    else: choice = 0
    
    if choice == 1:
        try:
            bio = re.compile('<h1>(.+?)</div>',re.DOTALL).findall(result)[0]; bio.replace('<dl style="margin: 0;padding: 0;">','')
            bio = re.sub('<(.+?)>','',bio); bio = bio.replace(':', ': '); bio = bio.replace('Pics & Videos:', '')
            a = common.CLEANUP(bio)
            common.TextBoxes("%s" % a)
        except: 
            dialog.ok(AddonTitle, "Sorry we could not get the information at this time. Please try again later.")
            quit()
    elif choice == 2:
        if not str(name) in a:
            if not '#START' in a:
                f = open(CHATURBATE_FILE,'w'); f.write('#START OF FILE#'); f.close()
                a=open(CHATURBATE_FILE).read()
            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(name)+'</name>\n<url>'+str(orig_url)+'</url>\n<icon>'+str(iconimage)+'</icon>\n</item>\n')
            f= open(CHATURBATE_FILE, mode='w')
            f.write(str(b))
            f.close()
            dp.close()
            dialog.ok(AddonTitle, "[COLOR white]You will be notified when " + str(name) + " is online.[/COLOR]")
            quit()
        else:
            a=open(CHATURBATE_FILE).read()
            b=a.replace('<item>\n<name>'+str(name)+'</name>\n','<old>\n<name>disabled</name>\n')
            f= open(CHATURBATE_FILE, mode='w')
            f.write(str(b))
            f.close()
            dp.close()
            dialog.ok(AddonTitle, "[COLOR white]Notifications for " + str(name) + " have been disabled.[/COLOR]")
            quit()        
    elif choice == 0:
 
        bandwidth = plugintools.get_setting("chaturbate_band")
        if bandwidth == '0': url2 = url2.replace('_fast_aac','_aac')
        elif bandwidth == '2':
            choice = dialog.select("[COLOR white]" + subject + "[/COLOR]", ['[COLOR white]Play High Bandwidth Stream[/COLOR]','[COLOR white]Play Low Bandwidth Stream[/COLOR]'])
            if choice == 1: url2 = url2.replace('_fast_aac','_aac')
            elif choice == 0: pass
            else: quit()
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
        notify_subject = plugintools.get_setting("chaturbate_subject")
        if notify_subject == "true":
            sleeper = plugintools.get_setting("chaturbate_subject_refresh")
            i = 0
            while not xbmc.Player().isPlayingVideo():
                time.sleep(1)
                i += 1
                if i == 7: quit()
            while xbmc.Player().isPlayingVideo():
                subject = re.compile('default_subject:\s\"([^,]+)",').findall(result)[0]; subject = urllib.unquote_plus(subject)
                kodi.notify(msg=subject, duration=8500, sound=True, icon_path=iconimage)
                time.sleep(int(sleeper))
    else: 
        dp.close()
        quit()
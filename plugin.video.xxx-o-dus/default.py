import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,shutil,hashlib
import base64,time,datetime
from resources.lib.modules  import plugintools
from resources.lib.modules  import menus
from resources.lib.modules  import common
from resources.lib.modules  import checker
from resources.lib.modules  import cache
from resources.lib.modules  import downloader
from resources.lib.modules  import extract
from resources.lib.scrapers import live
from resources.lib.scrapers import chaturbate
from resources.lib.scrapers import xnxx
from resources.lib.scrapers import youporn
from resources.lib.scrapers import porncom
from resources.lib.scrapers import pornhd
from resources.lib.scrapers import redtube
from resources.lib.scrapers import xhamster
from resources.lib.scrapers import pornfun
from resources.lib.scrapers import motherless
from resources.lib.scrapers import spankbang
from resources.lib.scrapers import porn00
from resources.lib.scrapers import virtualpornstars
from resources.lib.scrapers import watchxxxfree
from resources.lib.scrapers import perfectgirls
from resources.lib.scrapers import justpornotv
from resources.lib.scrapers import eporner
from resources.lib.scrapers import pornxs
from resources.lib.scrapers import xvideos
from resources.lib.scrapers import nxgx
from resources.lib.scrapers import madthumbs
from resources.lib.scrapers import ultravid
from resources.lib.scrapers import freeomovie

addon_id            = 'plugin.video.xxx-o-dus'
AddonTitle          = '[COLOR orangered]XXX-O-DUS[/COLOR]'
fanart              = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon                = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

BASE                = base64.decodestring('aHR0cDovL2VjaG9jb2Rlci5jb20vcHJpdmF0ZS9hZGRvbnMvc3BvcnRpZS9tZW51cy9tYWluLnhtbA==') 
dialog              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()

HOME                = xbmc.translatePath('special://home/')
DATA_FOLDER         = xbmc.translatePath(os.path.join('special://profile/addon_data/', addon_id))
XXX_SETTINGS         = os.path.join(DATA_FOLDER, 'settings.xml')
PARENTAL_FOLDER     = os.path.join(DATA_FOLDER, 'parental')
ADDON_FOLDER        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id))
F4M_TESTER          = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.f4mTester'))
PARENTAL_FILE       = xbmc.translatePath(os.path.join(PARENTAL_FOLDER , 'control.txt'))
PARENTAL_CHECK_FILE = xbmc.translatePath(os.path.join(PARENTAL_FOLDER , 'check_pin_time.txt'))
TERMS               = xbmc.translatePath(os.path.join(ADDON_FOLDER , 'resources/disclaimer.txt'))
INFO                = xbmc.translatePath(os.path.join(ADDON_FOLDER , 'resources/information.txt'))
REPO_INFO           = xbmc.translatePath(os.path.join(ADDON_FOLDER , 'resources/repository.txt'))
RESET_NOTICE        = xbmc.translatePath(os.path.join(ADDON_FOLDER , 'resources/reset.txt'))
I_AGREE             = xbmc.translatePath(os.path.join(DATA_FOLDER , 'agreed.txt'))
HISTORY_FILE        = xbmc.translatePath(os.path.join(DATA_FOLDER , 'history.xml'))
FAVOURITES_FILE     = xbmc.translatePath(os.path.join(DATA_FOLDER , 'favourites.xml'))
DOWNLOADS_FILE      = xbmc.translatePath(os.path.join(DATA_FOLDER , 'downloads.xml'))
SEARCH_FILE         = xbmc.translatePath(os.path.join(DATA_FOLDER , 'search.xml'))
REPO_FOLDER         = xbmc.translatePath(os.path.join('special://home/addons/repository.xxxecho'))
download_location   = plugintools.get_setting("download_location")
DOWNLOAD_FOLDER = xbmc.translatePath(download_location)

SEND_TO_CHECK = REPO_FOLDER + '|SPLIT|' + REPO_INFO
checker.check(SEND_TO_CHECK)

def GetMenu():

    history_on_off  = plugintools.get_setting("history_setting")
    
    if not os.path.exists(PARENTAL_FILE): common.addDir("[COLOR orangered]PARENTAL CONTROLS - [COLOR orangered]OFF[/COLOR][/COLOR]","url",900,icon,fanart)
    else: common.addDir("[COLOR orangered]PARENTAL CONTROLS - [COLOR lime]ON[/COLOR][/COLOR]","url",900,icon,fanart)
    common.addDir("[COLOR white]Search...[/COLOR]","url",1,icon,fanart)
    common.addDir("[COLOR white]Live Cams & Channels[/COLOR]","url",3,icon,fanart)
    common.addDir("[COLOR white]Films[/COLOR]","url",7,icon,fanart)
    common.addDir("[COLOR white]Videos[/COLOR]","url",2,icon,fanart)
    common.addDir("[COLOR white]Photos[/COLOR]","url",4,icon,fanart)
    common.addDir("[COLOR white]Stories[/COLOR]","url",5,icon,fanart)
    if history_on_off == "true": common.addDir("[COLOR pink]Your History[/COLOR] - [COLOR lime]ON[/COLOR]",BASE,101,icon,fanart)
    else: common.addDir("[COLOR pink]Your History[/COLOR] - [COLOR red]OFF[/COLOR]",BASE,101,icon,fanart)
    common.addDir("[COLOR pink]Your Favourites[/COLOR]",BASE,102,icon,fanart)
    common.addDir("[COLOR pink]Your Downloads[/COLOR]",BASE,105,icon,fanart)
    common.addLink("[COLOR pink]Your Settings[/COLOR]",BASE,106,icon,fanart)
    common.addLink("[COLOR white]View Disclaimer[/COLOR]",TERMS,998,icon,fanart)
    common.addLink("[COLOR white]View Addon Information[/COLOR]",INFO,998,icon,fanart)
    common.addLink("[COLOR orangered]RESET XXX-O-DUS[/COLOR]",'url',997,icon,fanart)
 
    common.SET_VIEW('list')

def SEARCH_DECIDE():

    search_on_off  = plugintools.get_setting("search_setting")
    if search_on_off == "true":
        name = "null"
        url = "100"
        common.SEARCH_HISTORY(name,url)
    else:
        url = "null"
        SEARCH_HOME(url)

def SEARCH_HOME(url):

    term = url
    total = 19
    i = 0
    if term == "null":
        string =''
        keyboard = xbmc.Keyboard(string, 'Enter Search Term')
        keyboard.doModal()
        if keyboard.isConfirmed():
            entry = keyboard.getText()
            term = entry
            string = entry.replace(' ','+')
            if not len(string)>1:
                quit()
        else: quit()
    else: string = term.replace(' ','+')

    search_on_off  = plugintools.get_setting("search_setting")
    if search_on_off == "true":
        a=open(SEARCH_FILE).read()
        b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<term>'+str(term)+'</term>\n</item>\n')
        f= open(SEARCH_FILE, mode='w')
        f.write(str(b))

    try:
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.create(AddonTitle, '[COLOR white]Searching: [/COLOR] [COLOR orangered]YouPorn[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        url = "http://www.youporn.com/search/?query=" + string.lower()
        url = 'split|'+url
        dp.update(progress)
        try:
            youporn.GET_CONTENT(url)
        except: pass
        url = "http://www.xnxx.com/?k=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]XNXX[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            xnxx.GET_CONTENT(url)
        except: pass
        url = "https://xhamster.com/search.php?from=&new=&q=" + string.lower() + "&qcat=video"
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Xhamster[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            xhamster.GET_CONTENT(url)
        except: pass
        url = "https://www.pornhd.com/search?search=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornHD[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            pornhd.GET_CONTENT(url)
        except: pass
        url = "https://www.porn.com/videos/search?q=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn.com[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            porncom.GET_CONTENT(url)
        except: pass
        url = "https://www.redtube.com/?search=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]RedTube[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            redtube.GET_CONTENT(url)
        except: pass
        url = "https://pornfun.com/search/?q=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornFun[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            pornfun.GET_CONTENT(url)
        except: pass
        url = "http://spankbang.com/s/" + string.lower() + "/"
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Spankbang[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            spankbang.GET_CONTENT(url)
        except: pass
        url = "http://www.porn00.org/?s=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn00[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            porn00.GET_CONTENT('none',url,'none')
        except: pass
        url = "http://virtualpornstars.com/?s=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Virtual Porn Stars[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            virtualpornstars.GET_CONTENT(url)
        except: pass
        url = "https://watchxxxfree.com/?s=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Watch XXX Free[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            watchxxxfree.GET_CONTENT(url)
        except: pass
        string = string.replace('+','%20')
        url = "http://www.perfectgirls.net/search/" + string.lower() + '/'
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Perfect Girls[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            perfectgirls.GET_CONTENT(url)
        except: pass
        string = string.replace('+','%20')
        url = "http://motherless.com/term/" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Motherless[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            motherless.GET_CONTENT(url)
        except: pass
        string = string.replace('+','%20')
        url = "http://justporno.tv/search?query=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Just Porno TV[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            justporno.GET_CONTENT(url)
        except: pass
        string = string.replace('+','-')
        url = "https://www.eporner.com/search/" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Eporner[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            eporner.GET_CONTENT(url)
        except: pass
        url = "http://pornxs.com/search.php?s=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornXS[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            pornxs.GET_CONTENT(url)
        except: pass
        url = "http://www.xvideos.com/?k=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]Xvideos[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            xvideos.GET_CONTENT(url)
        except: pass
        stringnx = string.replace('+','-')
        url = "http://www.nxgx.com/search/" + stringnx.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]NXGX[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            nxgx.GET_CONTENT(url)
        except: pass
        url = "http://www.madthumbs.com/search?q=" + string.lower()
        url = 'split|'+url
        i = i + 1
        progress = 100 * int(i)/int(total)
        dp.update(progress, '[COLOR white]Searching: [/COLOR] [COLOR orangered]MadThumbs[/COLOR]','[COLOR white]Term: [/COLOR][COLOR deeppink]' + term.lower() + '[/COLOR]','[COLOR white]Source: [/COLOR][COLOR pink]' + str(i) + ' of '+  str(total) + '[/COLOR]')
        try:
            madthumbs.GET_CONTENT(url)
        except: pass
        dp.close()
    except:
        dialog.ok(AddonTitle, '[COLOR pink]Sorry, there was an error searching for ' + string.lower() + ' please try again later.[/COLOR]')
        quit()

    common.SET_VIEW('list')

def PARENTAL_CONTROLS():

    found = 0
    if not os.path.exists(PARENTAL_FILE):
        found = 1
        common.addLink("[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]","url",999,icon,fanart)
        common.addLink("[COLOR white]Setup Parental Password[/COLOR]","url",901,icon,fanart)
    else:
        found = 1
        common.addLink("[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR lime]ON[/COLOR]","url",999,icon,fanart)
        common.addLink("[COLOR lime]Change Password[/COLOR]","url",901,icon,fanart)
        common.addLink("[COLOR orangered]Disable Password[/COLOR]","url",902,icon,fanart)

    if found == 0:
        common.addLink("[COLOR rose]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]","url",999,icon,fanart)
        common.addLink("[COLOR white]Setup Parental Password[/COLOR]","url",902,icon,fanart)

def GET_HISTORY():

    list = []
    
    history_on_off  = plugintools.get_setting("history_setting")

    setting = "history_setting|SPLIT|" + history_on_off
    
    if history_on_off == "true":
        common.addLink('[COLOR deeppink]Clear History[/COLOR]',BASE,104,icon,fanart)
        common.addLink('[COLOR orangered]Disable History[/COLOR]',setting,109,icon,fanart)
        common.addLink('###########################################',BASE,999,icon,fanart)

        f = open(HISTORY_FILE,mode='r'); msg = f.read(); f.close()
        msg = msg.replace('\n','')
        match = re.compile('<item>(.+?)</item>').findall(msg)
        for item in match:
            date=re.compile('<date>(.+?)</date>').findall(item)[0]
            time=re.compile('<time>(.+?)</time>').findall(item)[0]
            title=re.compile('<name>(.+?)</name>').findall(item)[0]
            url=re.compile('<link>(.+?)</link>').findall(item)[0]
            site=re.compile('<site>(.+?)</site>').findall(item)[0]
            iconimage=re.compile('<icon>(.+?)</icon>').findall(item)[0]
            url = title + '|SPLIT|' + url + '|SPLIT|' + site + '|SPLIT|' + iconimage + '|SPLIT|' + url
            if not url in str(list): common.addLink('[COLOR pink]' + date + ' | ' + '[/COLOR][COLOR deeppink]' + time + '[/COLOR] - [COLOR orangered]' + site + '[/COLOR][COLOR pink] - ' + title + '[/COLOR]',url,800,iconimage,fanart)
            list.append(url)
    else: 
        common.addLink('[COLOR orangered]Enable History Monitoring[/COLOR]',setting,109,icon,fanart)
        common.addLink('############################################',BASE,999,icon,fanart)
        common.addLink('[COLOR pink]History monitoring is currently disabled.[/COLOR]',setting,109,icon,fanart)

def GET_FAVOURITES():

    common.addLink('[COLOR deeppink]Your Favourites[/COLOR]',BASE,999,icon,fanart)
    common.addLink('###########################################',BASE,999,icon,fanart)

    f = open(FAVOURITES_FILE,mode='r'); msg = f.read(); f.close()
    msg = msg.replace('\n','')
    match = re.compile('<item>(.+?)</item>').findall(msg)
    for item in match:
        title=re.compile('<name>(.+?)</name>').findall(item)[0]
        url=re.compile('<link>(.+?)</link>').findall(item)[0]
        site=re.compile('<site>(.+?)</site>').findall(item)[0]
        iconimage=re.compile('<icon>(.+?)</icon>').findall(item)[0]
        url = title + '|SPLIT|' + url + '|SPLIT|' + site + '|SPLIT|' + iconimage + '|SPLIT|' + url
        common.addLink('[COLOR orangered]' + site + '[/COLOR][COLOR pink] - ' + title + '[/COLOR]',url,103,iconimage,fanart)

def DECIDE_FAVOURITES(name,url,iconimage):

    original = url
    a,b,c,d,url = url.split('|SPLIT|')
    
    string = '\n<item>\n<name>'+a+'</name>\n<link>'+b+'</link>\n<site>'+c+'</site>\n<icon>'+d+'</icon>\n</item>\n'

    choice = dialog.select("[COLOR orangered][B]Please select an option[/B][/COLOR]", ['[COLOR pink][B]Watch Video[/B][/COLOR]','[COLOR pink][B]Remove from Favourites[/B][/COLOR]'])

    if choice == 0:
        PLAYER(name,original,iconimage)
    else:
        e=open(FAVOURITES_FILE).read()
        f=e.replace(string,'\n')
        g= open(FAVOURITES_FILE, mode='w')
        g.write(str(f))
        g.close()
        xbmc.executebuiltin("Container.Refresh")
        quit()

def DECIDE_DOWNLOAD(name,url,iconimage):

    original = url
    a,b,c,d,url = url.split('|SPLIT|')

    choice = dialog.select("[COLOR orangered][B]Please select an option[/B][/COLOR]", ['[COLOR pink][B]Watch Video[/B][/COLOR]','[COLOR pink][B]Delete Download[/B][/COLOR]'])

    if choice == 0:
        PLAYER(name,original,iconimage)
    else:
        os.remove(url)
        xbmc.executebuiltin("Container.Refresh")

def CLEAR_HISTORY():

    if os.path.isfile(HISTORY_FILE):
        choice = xbmcgui.Dialog().yesno(AddonTitle, '[COLOR white]Would you like to clear all stored history?[/COLOR]','',yeslabel='[COLOR lime]YES[/COLOR]',nolabel='[B][COLOR orangered]NO[/COLOR][/B]')
        if choice == 1:
            os.remove(HISTORY_FILE)
            f = open(HISTORY_FILE,'w')
            f.write('#START OF FILE#')
            f.close()
    xbmc.executebuiltin("Container.Refresh")

def CLEAR_SEARCH():

    if os.path.isfile(SEARCH_FILE):
        choice = xbmcgui.Dialog().yesno(AddonTitle, '[COLOR white]Would you like to clear all stored search history?[/COLOR]','',yeslabel='[COLOR lime]YES[/COLOR]',nolabel='[B][COLOR orangered]NO[/COLOR][/B]')
        if choice == 1:
            os.remove(SEARCH_FILE)
            f = open(SEARCH_FILE,'w')
            f.write('#START OF FILE#')
            f.close()
    xbmc.executebuiltin("Container.Refresh")

def GET_DOWNLOADS():

    download_location   = plugintools.get_setting("download_location")
    download_folder = xbmc.translatePath(download_location)
    common.addLink('[COLOR deeppink]Download Location: [/COLOR]',BASE,999,icon,fanart)
    common.addLink(download_folder,BASE,999,icon,fanart)
    common.addLink('[COLOR orangered]Change Download Location[/COLOR]',BASE,106,icon,fanart)
    common.addLink('###########################################',BASE,999,icon,fanart)

    extensions = ['.mp4']

    for file in os.listdir(download_folder):
        for extension in extensions:
            if file.endswith(extension):
                iconimage = icon
                f = open(DOWNLOADS_FILE,mode='r'); msg = f.read(); f.close()
                msg = msg.replace('\n','')
                match = re.compile('<item>(.+?)</item>').findall(msg)
                for item in match:
                    title=re.compile('<name>(.+?)</name>').findall(item)[0]
                    iconimage2=re.compile('<icon>(.+?)</icon>').findall(item)[0]
                    if file in title:
                        iconimage = iconimage2
                url =  xbmc.translatePath(os.path.join(download_folder,file))
                if "http" in iconimage:
                    url2 = file + '|SPLIT|' + url + '|SPLIT|Downloaded|SPLIT|' + iconimage + '|SPLIT|' + url
                else:
                    url2 = file + '|SPLIT|' + url + '|SPLIT|Downloaded|SPLIT|None|SPLIT|' + url
                common.addLink('[COLOR pink]' + file + '[/COLOR]',url2,107,iconimage,fanart)

def CHANGE_DOWNLOADS():

    download_location   = plugintools.get_setting("download_location")
    _out = dialog.browse(3, AddonTitle, 'files', '', False, False, HOME)
    e=open(XXX_SETTINGS).read()
    f=e.replace(download_location, _out)
    g= open(XXX_SETTINGS, mode='w')
    g.write(str(f))
    g.close()
    xbmc.executebuiltin("Container.Refresh")

def PLAYER(name,url,iconimage):

    a,b,c,d,url = url.split('|SPLIT|')
    name = a
    date_now = datetime.datetime.now().strftime("%d-%m-%Y")
    time_now = datetime.datetime.now().strftime("%H:%M")
    string = '\n<item>\n<date>'+date_now+'</date>\n<time>'+time_now+'</time>\n<name>'+a+'</name>\n<link>'+b+'</link>\n<site>'+c+'</site>\n<icon>'+d+'</icon>\n</item>\n'
    a=open(HISTORY_FILE).read()
    b=a.replace('#START OF FILE#', '#START OF FILE#' + string)
    f= open(HISTORY_FILE, mode='w')
    f.write(str(b))
    f.close()

    if iconimage == "None":
        iconimage = icon

    if "highwebmedia" in url:
        dialog.ok(AddonTitle, '[COLOR pink]Chaturbate links are taken at the time of broadcasting. If this broadcast has ended the link will no longer play. [/COLOR]')
    import urlresolver
    if urlresolver.HostedMediaFile(url).valid_url(): 
        url = urlresolver.HostedMediaFile(url).resolve()
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    xbmc.Player ().play(url, liz, False)

def LIVE_PLAYER(name,url,iconimage):

    if not 'f4m'in url:
        if '.m3u8'in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage
        elif '.ts'in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage 

    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    xbmc.Player().play(url,liz,False)

def PARENTAL_CONTROLS_PIN():

    vq = common._get_keyboard( heading="Please Set Password" )
    if ( not vq ):
        dialog.ok(AddonTitle,"Sorry, no password was entered.")
        sys.exit(0)
    pass_one = vq

    vq = common._get_keyboard( heading="Please Confirm Your Password" )
    if ( not vq ):
        dialog.ok(AddonTitle,"Sorry, no password was entered.")
        sys.exit(0)
    pass_two = vq
        
    if not os.path.exists(PARENTAL_FILE):
        if not os.path.exists(PARENTAL_FOLDER):
            os.makedirs(PARENTAL_FOLDER)
        open(PARENTAL_FILE, 'w')

        if pass_one == pass_two:
            #writeme = base64.b64encode(pass_one)
            writeme = hashlib.sha256(pass_one).hexdigest()
            f = open(PARENTAL_FILE,'w')
            f.write('<password>'+str(writeme)+'</password>')
            f.close()
            dialog.ok(AddonTitle,'Your password has been set and parental controls have been enabled.')
            xbmc.executebuiltin("Container.Refresh")
        else:
            dialog.ok(AddonTitle,'The passwords do not match, please try again.')
            sys.exit(0)
    else:
        os.remove(PARENTAL_FILE)
        
        if pass_one == pass_two:
            #writeme = base64.b64encode(pass_one)
            writeme = hashlib.sha256(pass_one).hexdigest()
            f = open(PARENTAL_FILE,'w')
            f.write('<password>'+str(writeme)+'</password>')
            f.close()
            dialog.ok(AddonTitle,'Your password has been set and parental controls have been enabled.')
            xbmc.executebuiltin("Container.Refresh")
        else:
            dialog.ok(AddonTitle,'The passwords do not match, please try again.')
            sys.exit(0)

def PARENTAL_CONTROLS_OFF():

    vq = common._get_keyboard( heading="Please Enter Your Password" )
    if ( not vq ): 
        dialog.ok(AddonTitle,"Sorry, no password was entered.")
        sys.exit(0)
    pass_one = hashlib.sha256(vq).hexdigest()

    vers = open(PARENTAL_FILE, "r")
    regex = re.compile(r'<password>(.+?)</password>')
    for line in vers:
        file = regex.findall(line)
        for password in file:
            if not password == pass_one:
                vers.close()
                dialog.ok(AddonTitle,"Sorry, the password you entered was incorrect.")
                quit()
    vers.close()
    try:
        os.remove(PARENTAL_FILE)
        dialog.ok(AddonTitle,'Parental controls have been disabled.')
        xbmc.executebuiltin("Container.Refresh")
    except:
        dialog.ok(AddonTitle,'There was an error disabling the parental controls.')
        xbmc.executebuiltin("Container.Refresh")

def SET_SETTINGS(url):

    name,setting = url.split("|SPLIT|")

    if setting == "true": setting = "false"
    elif setting == "false": setting = "true"
    plugintools.set_setting( str(name) , str(setting) )
    
    xbmc.executebuiltin("Container.Refresh")

def VIEW_DIALOG(url):

    f = open(url,mode='r'); msg = f.read(); f.close()
    common.TextBoxes("%s" % msg)

    if url == RESET_NOTICE:
        return

def RESET():

    try:
        VIEW_DIALOG(RESET_NOTICE)
        
        choice = xbmcgui.Dialog().yesno("[COLOR orangered][B]RESET XXX-O-DUS?[/B][/COLOR]", '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]','',yeslabel='[COLOR green]YES[/COLOR]',nolabel='[COLOR orangered]NO[/COLOR]')
        if choice == 1:
            download_location   = plugintools.get_setting("download_location")
            download_folder = xbmc.translatePath(download_location)

            extensions = ['.mp4']

            for file in os.listdir(download_folder):
                for extension in extensions:
                    if file.endswith(extension):
                        try:
                            path = xbmc.translatePath(os.path.join(download_folder, file))
                            os.remove(path)
                        except:
                            dialog.ok(AddonTitle, "[COLOR white]There was an error deleting " + file + "[/COLOR]")
                            pass
            try:
                shutil.rmtree(DATA_FOLDER)
            except:
                dialog.ok(AddonTitle, "[COLOR white]There was an error deleting deleting the data directory.[/COLOR]")
                pass
            dialog.ok(AddonTitle, "[COLOR white]XXX-O-DUS has been reset to the factory state.[/COLOR]","[COLOR white]Press OK to continue.[/COLOR]")
            xbmc.executebuiltin("Container.Refresh")
    except:
        dialog.ok(AddonTitle, "[COLOR white]Sorry, something went wrong.[/COLOR]","[COLOR white]Please report this issue to @EchoCoder on Twitter.[/COLOR]")
        quit()

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

###################################################################
###################################################################
##############CHECKS NEEDED TO BE RUN ON EVERY DIR#################
###################################################################
###################################################################

if not os.path.exists(DOWNLOAD_FOLDER): os.makedirs(DOWNLOAD_FOLDER)

if not os.path.isfile(HISTORY_FILE):
    f = open(HISTORY_FILE,'w'); f.write('#START OF FILE#'); f.close()
if not os.path.isfile(FAVOURITES_FILE):
    f = open(FAVOURITES_FILE,'w'); f.write('#START OF FILE#'); f.close()
if not os.path.isfile(DOWNLOADS_FILE):
    f = open(DOWNLOADS_FILE,'w'); f.write('#START OF FILE#'); f.close()
if not os.path.isfile(SEARCH_FILE):
    f = open(SEARCH_FILE,'w'); f.write('#START OF FILE#'); f.close()
try:
    search_on_off  = plugintools.get_setting("search_setting")
    if not search_on_off == "true" or "false": plugintools.set_setting("search_setting", "true")
except: plugintools.set_setting("search_setting", "true")

if not os.path.exists(PARENTAL_FOLDER): os.makedirs(PARENTAL_FOLDER)

if os.path.exists(PARENTAL_FILE):

    new = False
    if not os.path.exists(PARENTAL_CHECK_FILE):
        file = open(PARENTAL_CHECK_FILE, 'w'); file.close()
        new = True

    fileCreation = os.path.getmtime(PARENTAL_CHECK_FILE)

    now = time.time()
    check = now - 60*30
    
    if (fileCreation < check or new==True):

        vq = common._get_keyboard( heading="Please Enter Your Password - [B][COLOR red](30 Minute Session)[/COLOR][/B]" )
        if ( not vq ): 
            dialog.ok(AddonTitle,"Sorry, no password was entered.")
            sys.exit(0)
        pass_one = hashlib.sha256(vq).hexdigest()

        vers = open(PARENTAL_FILE, "r")
        regex = re.compile(r'<password>(.+?)</password>')
        for line in vers:
            file = regex.findall(line)
            for password in file:
                if not password == pass_one:
                    dialog.ok(AddonTitle,"Sorry, the password you entered was incorrect.")
                    sys.exit(0)
                else:
                    try: os.remove(PARENTAL_CHECK_FILE)
                    except: pass
                    file = open(PARENTAL_CHECK_FILE, 'w'); file.close()
                    dialog.ok(AddonTitle,'Login successful!','You now have a 30 minute session before you will be asked for the password again.')

###################################################################
###################################################################
#########################PARAMS AND MODES##########################
###################################################################
###################################################################

params=get_params(); name=None; url=None; mode=None; iconimage=None; fanartimage=None
try: name=urllib.unquote_plus(params["name"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanartimage=urllib.quote_plus(params["fanartimage"])
except: pass

if mode==None or url==None or len(url)<1: GetMenu()
elif mode==1:menus.SEARCH()
elif mode==2:menus.VIDEOS()
elif mode==3:menus.LIVE()
elif mode==4:menus.PICTURES()
elif mode==5:menus.STORIES()
elif mode==6:menus.ALL()
elif mode==7:menus.FILMS()
elif mode==10:xhamster.MAIN_MENU()
elif mode==11:xhamster.GET_CONTENT(url)
elif mode==12:xhamster.SEARCH(url)
elif mode==13:xhamster.PLAY_URL(name,url,iconimage)
elif mode==14:xhamster.SEARCH_DECIDE()
elif mode==20:chaturbate.MAIN_MENU()
elif mode==21:chaturbate.GET_CONTENT(url)
elif mode==22:chaturbate.SEARCH(url)
elif mode==23:chaturbate.PLAY_URL(name,url,iconimage)
elif mode==29:xnxx.SEARCH_DECIDE()
elif mode==30:xnxx.MAIN_MENU()
elif mode==31:xnxx.GET_CONTENT(url)
elif mode==32:xnxx.SEARCH(url)
elif mode==33:xnxx.PLAY_URL(name,url,iconimage)
elif mode==34:xnxx.PICTURE_MENU()
elif mode==35:xnxx.PICTURE_CONTENT(url)
elif mode==36:xnxx.SCRAPE_GALLERY(url)
elif mode==37:xnxx.DISPLAY_PICTURE(url)
elif mode==38:xnxx.STORY_MENU()
elif mode==39:xnxx.LIST_STORIES(url)
elif mode==40:xnxx.DISPLAY_STORY(url)
elif mode==41:redtube.MAIN_MENU()
elif mode==42:redtube.GET_CONTENT(url)
elif mode==43:redtube.SEARCH(url)
elif mode==44:redtube.PLAY_URL(name,url,iconimage)
elif mode==45:redtube.SEARCH_DECIDE()
elif mode==50:pornhd.MAIN_MENU()
elif mode==51:pornhd.GET_CONTENT(url)
elif mode==52:pornhd.SEARCH(url)
elif mode==53:pornhd.PLAY_URL(name,url,iconimage)
elif mode==54:pornhd.SEARCH_DECIDE()
elif mode==60:porncom.MAIN_MENU()
elif mode==61:porncom.GET_CONTENT(url)
elif mode==62:porncom.SEARCH(url)
elif mode==63:porncom.PLAY_URL(name,url,iconimage)
elif mode==64:porncom.SEARCH_DECIDE()
elif mode==70:youporn.MAIN_MENU()
elif mode==71:youporn.GET_CONTENT(url)
elif mode==72:youporn.SEARCH(url)
elif mode==73:youporn.PLAY_URL(name,url,iconimage)
elif mode==74:youporn.SEARCH_DECIDE()
elif mode==80:pornfun.MAIN_MENU()
elif mode==81:pornfun.GET_CONTENT(url)
elif mode==82:pornfun.SEARCH(url)
elif mode==83:pornfun.PLAY_URL(name,url,iconimage)
elif mode==84:pornfun.SEARCH_DECIDE()
elif mode==90:motherless.MAIN_MENU_PICTURES()
elif mode==91:motherless.GET_CONTENT_PICTURES(url)
elif mode==92:motherless.DISPLAY_PICTURE(url)
elif mode==93:motherless.MAIN_MENU()
elif mode==94:motherless.GET_CONTENT(url)
elif mode==95:motherless.SEARCH(url)
elif mode==96:motherless.PLAY_URL(name,url,iconimage)
elif mode==97:motherless.SEARCH_DECIDE()
elif mode==300:watchxxxfree.MAIN_MENU()
elif mode==301:watchxxxfree.GET_CONTENT(url)
elif mode==302:watchxxxfree.SEARCH(url)
elif mode==303:watchxxxfree.PLAY_URL(name,url,iconimage)
elif mode==304:watchxxxfree.SEARCH_DECIDE()
elif mode==310:perfectgirls.MAIN_MENU()
elif mode==311:perfectgirls.GET_CONTENT(url)
elif mode==312:perfectgirls.SEARCH(url)
elif mode==313:perfectgirls.PLAY_URL(name,url,iconimage)
elif mode==314:perfectgirls.SEARCH_DECIDE()
elif mode==99:SEARCH_DECIDE();
elif mode==100:SEARCH_HOME(url);
elif mode==101:GET_HISTORY()
elif mode==102:GET_FAVOURITES()
elif mode==103:DECIDE_FAVOURITES(name,url,iconimage)
elif mode==104:CLEAR_HISTORY()
elif mode==105:GET_DOWNLOADS()
elif mode==106:plugintools.open_settings_dialog();  xbmc.executebuiltin('Container.Refresh')
elif mode==107:DECIDE_DOWNLOAD(name,url,iconimage)
elif mode==108:CLEAR_SEARCH()
elif mode==109:SET_SETTINGS(url)
elif mode==200:spankbang.MAIN_MENU()
elif mode==201:spankbang.SUB_MENU(url)
elif mode==202:spankbang.GET_CONTENT(url)
elif mode==203:spankbang.SEARCH(url)
elif mode==204:spankbang.PLAY_URL(name,url,iconimage)
elif mode==205:spankbang.SEARCH_DECIDE()
elif mode==210:porn00.MAIN_MENU()
elif mode==211:porn00.GET_CONTENT(name,url,iconimage)
elif mode==212:porn00.SEARCH(url)
elif mode==213:porn00.PLAY_URL(name,url,iconimage)
elif mode==214:porn00.SEARCH_DECIDE()
elif mode==220:virtualpornstars.MAIN_MENU()
elif mode==221:virtualpornstars.GET_CONTENT(url)
elif mode==222:virtualpornstars.SEARCH(url)
elif mode==223:virtualpornstars.PLAY_URL(name,url,iconimage)
elif mode==224:virtualpornstars.SEARCH_DECIDE()
elif mode==230:justpornotv.MAIN_MENU()
elif mode==231:justpornotv.GET_CONTENT(url)
elif mode==232:justpornotv.SEARCH(url)
elif mode==233:justpornotv.PLAY_URL(name,url,iconimage)
elif mode==234:justpornotv.SEARCH_DECIDE()
elif mode==240:eporner.MAIN_MENU()
elif mode==241:eporner.GET_CONTENT(url)
elif mode==242:eporner.SEARCH(url)
elif mode==243:eporner.PLAY_URL(name,url,iconimage)
elif mode==244:eporner.SEARCH_DECIDE()
elif mode==250:pornxs.MAIN_MENU()
elif mode==251:pornxs.GET_CONTENT(url)
elif mode==252:pornxs.SEARCH(url)
elif mode==253:pornxs.PLAY_URL(name,url,iconimage)
elif mode==254:pornxs.SEARCH_DECIDE()
elif mode==260:xvideos.MAIN_MENU()
elif mode==261:xvideos.GET_CONTENT(url)
elif mode==262:xvideos.SEARCH(url)
elif mode==263:xvideos.PLAY_URL(name,url,iconimage)
elif mode==264:xvideos.SEARCH_DECIDE()
elif mode==270:nxgx.MAIN_MENU()
elif mode==271:nxgx.GET_CONTENT(url)
elif mode==272:nxgx.SEARCH(url)
elif mode==273:nxgx.PLAY_URL(name,url,iconimage)
elif mode==274:nxgx.SEARCH_DECIDE()
elif mode==280:madthumbs.MAIN_MENU()
elif mode==281:madthumbs.GET_CONTENT(url)
elif mode==282:madthumbs.SEARCH(url)
elif mode==283:madthumbs.PLAY_URL(name,url,iconimage)
elif mode==284:madthumbs.SEARCH_DECIDE()
elif mode==700:live.LIVE_CHANNELS()
elif mode==710:ultravid.MENU(url)
elif mode==711:ultravid.PLAY_URL(name,url,iconimage)
elif mode==720:freeomovie.MENU(url)
elif mode==721:freeomovie.PLAY_URL(name,url,iconimage)
elif mode==800:PLAYER(name,url,iconimage)
elif mode==900:PARENTAL_CONTROLS()
elif mode==901:PARENTAL_CONTROLS_PIN()
elif mode==902:PARENTAL_CONTROLS_OFF()
elif mode==995:common.GET_M3U_LIST(url)
elif mode==996:LIVE_PLAYER(name,url,iconimage)
elif mode==997:RESET()
elif mode==998:VIEW_DIALOG(url)

if mode==None: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=False)
else: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
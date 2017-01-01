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
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/motherless/fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/motherless/icon.png'))
BASE 		   = 'http://motherless.com/images'
HISTORY_FILE   = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id , 'history.xml'))
FAVOURITES_FILE= xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id , 'favourites.xml'))

def MAIN_MENU():

	result = common.open_url(BASE)
	
	match = re.compile('<div class="sub_menu dark-menu">(.+?)<a class="feed-link medium"',re.DOTALL).findall(result)
	string = str(match)
	match2 = re.compile("<a(.+?)/a>",re.DOTALL).findall(string)

	for item in match2:
		url=re.compile('href="(.+?)" title=".+?">.+?<').findall(item)[0]
		name=re.compile('href=".+?" title=".+?">(.+?)<').findall(item)[0]
		url = "http://www.motherless.com" + url
		common.addDir(name,url,91,icon,fanart)

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GET_CONTENT(url):

	checker = url
	result = common.open_url(url)
	match = re.compile('<div class="content-inner">(.+?)</html>',re.DOTALL).findall(result)
	string = str(match)
	match2 = re.compile('<div class="thumb-container(.+?)<div class="clear:both;">',re.DOTALL).findall(string)
	for item in match2:
		try:
			title=re.compile('<h2 class="caption title">(.+?)</h2>').findall(item)[0]
			iconimage=re.compile('<img class="static" src="(.+?)"').findall(item)[0]
			hits=re.compile('<div class="caption right">(.+?)</div>').findall(item)[0]
			date=re.compile('<div class="caption right">(.+?)</div>').findall(item)[1]
			title = common.CLEANUP(title)
			name = title + ' - ' + hits + ' | ' + date
			common.addLink(name,iconimage,92,iconimage,fanart)
		except: pass

	try:
		next=re.compile('<a href="([^"]*)" class="pop".+?>NEXT').findall(result)[0]
		url = "http://motherless.com" + str(next)
		common.addDir('[COLOR orangered]Next Page >>[/COLOR]',url,91,icon,fanart)       
	except:pass

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(500)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(52)')
	else: xbmc.executebuiltin('Container.SetViewMode(500)')

def DISPLAY_PICTURE(url):

    SHOW = "ShowPicture(" + url + ')'
    xbmc.executebuiltin(SHOW)

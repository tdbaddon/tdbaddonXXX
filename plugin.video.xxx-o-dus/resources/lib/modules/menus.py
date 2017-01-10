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

addon_id            = 'plugin.video.xxx-o-dus'
AddonTitle          = '[COLOR orangered]XXX-O-DUS[/B][/COLOR]'
fanart              = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon                = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
xhamster_icon       = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/xhamster/icon.png'))
xhamster_fanart     = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/xhamster/fanart.jpg'))
chaturbate_icon     = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/icon.png'))
chaturbate_fanart   = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/chaturbate/fanart.jpg'))
xnxx_icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/xnxx/icon.png'))
xnxx_fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/xnxx/fanart.jpg'))
redtube_icon        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/redtube/icon.png'))
redtube_fanart      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/redtube/fanart.jpg'))
pornhd_icon         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/pornhd/icon.png'))
pornhd_fanart       = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/pornhd/fanart.jpg'))
porncom_icon        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/porncom/icon.png'))
porncom_fanart      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/porncom/fanart.jpg'))
youporn_icon        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/youporn/icon.png'))
youporn_fanart      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/youporn/fanart.jpg'))
pornfun_icon        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/pornfun/icon.png'))
pornfun_fanart      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/pornfun/fanart.jpg'))
motherless_icon     = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/motherless/icon.png'))
motherless_fanart   = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/motherless/fanart.jpg'))
spankbang_icon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/spankbang/icon.png'))
spankbang_fanart    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/spankbang/fanart.jpg'))
porn00_icon         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/porn00/icon.png'))
porn00_fanart       = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/porn00/fanart.jpg'))
virtualpornstars_icon   = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/virtualpornstars/icon.png'))
virtualpornstars_fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/art/virtualpornstars/fanart.jpg'))

def SEARCH():

	common.addDir("[COLOR white][B]SEARCH ALL WESBITES[/B][/COLOR]","url",100,icon,fanart)
	common.addLink("[COLOR darkgray]#################################[/B][/COLOR]","url",999,icon,fanart)
	common.addDir("[COLOR white][B]Search Xhamster[/B][/COLOR]","url",12,xhamster_icon,xhamster_fanart)
	common.addDir("[COLOR white][B]Search XNXX[/B][/COLOR]","url",32,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR white][B]Search RedTube[/B][/COLOR]","url",43,redtube_icon,redtube_fanart)
	common.addDir("[COLOR white][B]Search PornHD[/B][/COLOR]","url",52,pornhd_icon,pornhd_fanart)
	common.addDir("[COLOR white][B]Search Porn.com[/B][/COLOR]","url",62,porncom_icon,porncom_fanart)
	common.addDir("[COLOR white][B]Search YouPorn[/B][/COLOR]","url",72,youporn_icon,youporn_fanart)
	common.addDir("[COLOR white][B]Search PornFun[/B][/COLOR]","url",82,pornfun_icon,pornfun_fanart)
	common.addDir("[COLOR white][B]Search Spankbang[/B][/COLOR]","url",202,spankbang_icon,spankbang_fanart)
	common.addDir("[COLOR white][B]Search Porn00[/B][/COLOR]","url",212,porn00_icon,porn00_fanart)
	common.addDir("[COLOR white][B]Search Virtual Porn Stars[/B][/COLOR]","url",222,virtualpornstars_icon,virtualpornstars_fanart)

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')
	
def VIDEOS():

	common.addDir("[COLOR white][B]Xhamster.com[/B][/COLOR]",'url',10,xhamster_icon,xhamster_fanart)
	common.addDir("[COLOR white][B]XNXX.com[/B][/COLOR]",'url',30,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR white][B]RedTube.com[/B][/COLOR]",'url',41,redtube_icon,redtube_fanart)
	common.addDir("[COLOR white][B]PornHD.com[/B][/COLOR]",'url',50,pornhd_icon,pornhd_fanart)
	common.addDir("[COLOR white][B]Porn.com[/B][/COLOR]",'url',60,porncom_icon,porncom_fanart)
	common.addDir("[COLOR white][B]YouPorn.com[/B][/COLOR]",'url',70,youporn_icon,youporn_fanart)
	common.addDir("[COLOR white][B]PornFun.com[/B][/COLOR]",'url',80,pornfun_icon,pornfun_fanart)
	common.addDir("[COLOR white][B]Spankbang.com[/B][/COLOR]",'url',200,spankbang_icon,spankbang_fanart)
	common.addDir("[COLOR white][B]Porn00.org[/B][/COLOR]",'url',210,porn00_icon,porn00_fanart)
	common.addDir("[COLOR white][B]Virtualpornstars.com[/B][/COLOR]",'url',220,virtualpornstars_icon,virtualpornstars_fanart)

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')
	
def LIVE():

	common.addDir("[COLOR white][B]Chaturbate.com[/B][/COLOR]",'url',20,chaturbate_icon,chaturbate_fanart)

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')
	
def PICTURES():

	common.addDir("[COLOR white][B]XNXX Pictures[/B][/COLOR]","url",34,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR white][B]Motherless Pictures[/B][/COLOR]","url",90,motherless_icon,motherless_fanart)
	
	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')
	
def STORIES():

	common.addDir("[COLOR white][B]XNXX Stories[/B][/COLOR]","url",38,xnxx_icon,xnxx_fanart)

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')
	
def ALL():

	common.addDir("[COLOR white][B]Xhamster.com[/B][/COLOR]",'url',10,xhamster_icon,xhamster_fanart)
	common.addDir("[COLOR white][B]Chaturbate.com[/B][/COLOR]",'url',20,chaturbate_icon,chaturbate_fanart)
	common.addDir("[COLOR white][B]XNXX.com[/B][/COLOR]",'url',30,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR white][B]RedTube.com[/B][/COLOR]",'url',41,redtube_icon,redtube_fanart)
	common.addDir("[COLOR white][B]PornHD.com[/B][/COLOR]",'url',50,pornhd_icon,pornhd_fanart)
	common.addDir("[COLOR white][B]Porn.com[/B][/COLOR]",'url',60,porncom_icon,porncom_fanart)
	common.addDir("[COLOR white][B]YouPorn.com[/B][/COLOR]",'url',70,youporn_icon,youporn_fanart)
	common.addDir("[COLOR white][B]PornFun.com[/B][/COLOR]",'url',80,pornfun_icon,pornfun_fanart)
	common.addDir("[COLOR white][B]Motherless.com[/B][/COLOR]",'url',90,motherless_icon,motherless_fanart)
	common.addDir("[COLOR white][B]Spankbang.com[/B][/COLOR]",'url',200,spankbang_icon,spankbang_fanart)
	common.addDir("[COLOR white][B]Porn00.org[/B][/COLOR]",'url',210,porn00_icon,porn00_fanart)
	common.addDir("[COLOR white][B]Virtualpornstars.com[/B][/COLOR]",'url',220,virtualpornstars_icon,virtualpornstars_fanart)

	kodi_name = common.GET_KODI_VERSION()

	if kodi_name == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(50)')
	elif kodi_name == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(50)')
	
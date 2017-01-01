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
AddonTitle          = '[COLOR orangered]XXX-O-DUS[/COLOR]'
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

def SEARCH():

	common.addDir("[COLOR white]SEARCH ALL WESBITES[/COLOR]","url",100,icon,fanart)
	common.addLink("[COLOR darkgray]#################################[/COLOR]","url",999,icon,fanart)
	common.addDir("[COLOR white]Search Xhamster[/COLOR]","url",12,xhamster_icon,xhamster_fanart)
	common.addDir("[COLOR white]Search XNXX[/COLOR]","url",32,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR white]Search RedTube[/COLOR]","url",43,redtube_icon,redtube_fanart)
	common.addDir("[COLOR white]Search PornHD[/COLOR]","url",52,pornhd_icon,pornhd_fanart)
	common.addDir("[COLOR white]Search Porn.com[/COLOR]","url",62,porncom_icon,porncom_fanart)
	common.addDir("[COLOR white]Search YouPorn[/COLOR]","url",72,youporn_icon,youporn_fanart)
	common.addDir("[COLOR white]Search PornFun[/COLOR]","url",82,pornfun_icon,pornfun_fanart)

def VIDEOS():

	common.addDir("[COLOR pink]Xhamster.com[/COLOR]",'url',10,xhamster_icon,xhamster_fanart)
	common.addDir("[COLOR pink]XNXX.com[/COLOR]",'url',30,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR pink]RedTube.com[/COLOR]",'url',41,redtube_icon,redtube_fanart)
	common.addDir("[COLOR pink]PornHD.com[/COLOR]",'url',50,pornhd_icon,pornhd_fanart)
	common.addDir("[COLOR pink]Porn.com[/COLOR]",'url',60,porncom_icon,porncom_fanart)
	common.addDir("[COLOR pink]YouPorn.com[/COLOR]",'url',70,youporn_icon,youporn_fanart)
	common.addDir("[COLOR pink]PornFun.com[/COLOR]",'url',80,pornfun_icon,pornfun_fanart)

def LIVE():

	common.addDir("[COLOR pink]Chaturbate.com[/COLOR]",'url',20,chaturbate_icon,chaturbate_fanart)

def PICTURES():

	common.addDir("[COLOR white]XNXX Pictures[/COLOR]","url",34,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR white]Motherless Pictures[/COLOR]","url",90,motherless_icon,motherless_fanart)

def STORIES():

	common.addDir("[COLOR white]XNXX Stories[/COLOR]","url",38,xnxx_icon,xnxx_fanart)

def ALL():

	common.addDir("[COLOR pink]Xhamster.com[/COLOR]",'url',10,xhamster_icon,xhamster_fanart)
	common.addDir("[COLOR pink]Chaturbate.com[/COLOR]",'url',20,chaturbate_icon,chaturbate_fanart)
	common.addDir("[COLOR pink]XNXX.com[/COLOR]",'url',30,xnxx_icon,xnxx_fanart)
	common.addDir("[COLOR pink]RedTube.com[/COLOR]",'url',41,redtube_icon,redtube_fanart)
	common.addDir("[COLOR pink]PornHD.com[/COLOR]",'url',50,pornhd_icon,pornhd_fanart)
	common.addDir("[COLOR pink]Porn.com[/COLOR]",'url',60,porncom_icon,porncom_fanart)
	common.addDir("[COLOR pink]YouPorn.com[/COLOR]",'url',70,youporn_icon,youporn_fanart)
	common.addDir("[COLOR pink]PornFun.com[/COLOR]",'url',80,pornfun_icon,pornfun_fanart)
	common.addDir("[COLOR pink]Motherless.com[/COLOR]",'url',90,motherless_icon,motherless_fanart)

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
import base64
import re

AddonTitle     = "[COLOR red]XXX-O-DUS[/COLOR]"

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

def CLEANUP(text):

	text = str(text)
	text = text.replace('\\r','')
	text = text.replace('\\n','')
	text = text.replace('\\t','')
	text = text.replace('\\','')
	text = text.replace('<br />','\n')
	text = text.replace('<hr />','')
	text = text.replace('&#039;',"'")
	text = text.replace('&quot;','"')
	text = text.replace('&rsquo;',"'")
	text = text.replace('&amp;',"&")

	return text

def TextBoxes(announce):
	class TextBox():
		WINDOW=10147
		CONTROL_LABEL=1
		CONTROL_TEXTBOX=5
		def __init__(self,*args,**kwargs):
			xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
			self.win=xbmcgui.Window(self.WINDOW) # get window
			xbmc.sleep(500) # give window time to initialize
			self.setControls()
		def setControls(self):
			self.win.getControl(self.CONTROL_LABEL).setLabel('[COLOR red]XXX-O-DUS[/COLOR]') # set heading
			try: f=open(announce); text=f.read()
			except: text=announce
			self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
			return
	TextBox()
	while xbmc.getCondVisibility('Window.IsVisible(10147)'):
		time.sleep(.5)

def _get_keyboard( default="", heading="", hidden=False ):
    """ shows a keyboard and returns a value """
    keyboard = xbmc.Keyboard( default, heading, hidden )
    keyboard.doModal()
    if ( keyboard.isConfirmed() ):
        return unicode( keyboard.getText(), "utf-8" )
    return default

def GET_LUCKY():

	import random
	lucky = random.randrange(10)
	
	dp = xbmcgui.DialogProgress()
	
	if lucky == 1:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]We are getting the moisturiser.[/COLOR]','[COLOR azure]Do you have the wipes ready?[/COLOR]' )
	elif lucky == 2:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]I am just taking off my pants.[/COLOR]','[COLOR azure]Darn belt![/COLOR]' )
	elif lucky == 3:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Are the curtains closed?[/COLOR]','[COLOR azure]Oh baby its cold outside![/COLOR]' )
	elif lucky == 4:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]This is my fifth time today.[/COLOR]','[COLOR azure]How about you?[/COLOR]' )
	elif lucky == 5:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Please no buffer, please no buffer![/COLOR]')
	elif lucky == 6:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]I think I am going blind :-/[/COLOR]','[COLOR azure]Oh no, just something in my eye.[/COLOR]' )
	elif lucky == 7:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Did I turn the oven off?[/COLOR]','[COLOR azure]It can wait![/COLOR]' )
	elif lucky == 8:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Your video is coming. Are you?[/COLOR]','[COLOR azure]Do you get it?[/COLOR]' )
	elif lucky == 9:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]Kodi does not save your browsing history :-D[/COLOR]','[COLOR azure]Thats lucky isnt it :-)[/COLOR]' )
	else:
		dp.create(AddonTitle,"[COLOR yellow]Please wait.[/COLOR]",'[COLOR pink]There are more XXX addons by ECHO.[/COLOR]','[COLOR azure]Just so you know.[/COLOR]' )

	return dp

def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def addDir(name,url,mode,iconimage,fanartimage):

	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanartimage="+urllib.quote_plus(fanartimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setProperty( "fanart_Image", fanartimage )
	liz.setProperty( "icon_Image", iconimage )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def addLink(name,url,mode,iconimage,fanartimage):

	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+iconimage+"&fanartimage="+urllib.quote_plus(fanartimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setProperty( "fanart_Image", fanartimage )
	liz.setProperty( "icon_Image", iconimage )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok
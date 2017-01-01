import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , shutil
import base64 , time , datetime
from resources . lib . modules import plugintools
from resources . lib . modules import menus
from resources . lib . modules import common
from resources . lib . modules import checker
from resources . lib . modules import downloader
from resources . lib . modules import extract
from resources . lib . scrapers import chaturbate
from resources . lib . scrapers import xnxx
from resources . lib . scrapers import youporn
from resources . lib . scrapers import porncom
from resources . lib . scrapers import pornhd
from resources . lib . scrapers import redtube
from resources . lib . scrapers import xhamster
from resources . lib . scrapers import pornfun
from resources . lib . scrapers import motherless
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xxx-o-dus'
Oo0Ooo = '[COLOR orangered]XXX-O-DUS[/COLOR]'
O0O0OO0O0O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'fanart.jpg' ) )
iiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'icon.png' ) )
ooo0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/xhamster/icon.png' ) )
II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/xhamster/fanart.jpg' ) )
O00ooooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/chaturbate/icon.png' ) )
I1IiiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/chaturbate/fanart.jpg' ) )
IIi1IiiiI1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/xnxx/icon.png' ) )
I11i11Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/xnxx/fanart.jpg' ) )
oO00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/redtube/icon.png' ) )
OOOo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/redtube/fanart.jpg' ) )
Oooo000o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/pornhd/icon.png' ) )
IiIi11iIIi1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/pornhd/fanart.jpg' ) )
Oo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/porncom/icon.png' ) )
IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/porncom/fanart.jpg' ) )
ooOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/youporn/icon.png' ) )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/youporn/fanart.jpg' ) )
o0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/pornfun/icon.png' ) )
IiiIII111iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/pornfun/fanart.jpg' ) )
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
OoI1Ii11I1Ii1i = base64 . decodestring ( 'aHR0cDovL2VjaG9jb2Rlci5jb20vcHJpdmF0ZS9hZGRvbnMvc3BvcnRpZS9tZW51cy9tYWluLnhtbA==' )
Ooo = xbmcgui . Dialog ( )
o0oOoO00o = xbmcgui . DialogProgress ( )
if 43 - 43: O0OOo . II1Iiii1111i
i1IIi11111i = xbmc . translatePath ( 'special://home/' )
o000o0o00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o , 'settings.xml' ) )
oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o , 'parental' ) )
IiII1I1i1i1ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o ) )
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o ) )
I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.f4mTester' ) )
O0OoOoo00o = xbmc . translatePath ( os . path . join ( oo , 'controls.txt' ) )
iiiI11 = xbmc . translatePath ( os . path . join ( IIIII , 'resources/disclaimer.txt' ) )
OOooO = xbmc . translatePath ( os . path . join ( IIIII , 'resources/information.txt' ) )
OOoO00o = xbmc . translatePath ( os . path . join ( IIIII , 'resources/repository.txt' ) )
II111iiii = xbmc . translatePath ( os . path . join ( IIIII , 'resources/reset.txt' ) )
IIoOoOo00oOo = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'agreed.txt' ) )
Ooo00O00O0O0O = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'history.xml' ) )
OooO0OO = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'favourites.xml' ) )
iiiIi = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'downloads.xml' ) )
IiIIIiI1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.xxxecho' ) )
if 86 - 86: i11I1IIiiIi + oOo + iiIiIiIi - o0oooO0OO0O / Oooo
O00o = xbmc . translatePath ( 'special://home/addons/' + OO0o + '/addon.xml' )
O00 = xbmc . translatePath ( 'special://home/addons/repository.xxxecho/addon.xml' )
i11I1 = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9wbHVnaW4udmlkZW8ueHh4LW8tZHVzL3BsdWdpbi52aWRlby54eHgtby1kdXMt' )
Ii11Ii11I = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9yZXBvc2l0b3J5Lnh4eGVjaG8vcmVwb3NpdG9yeS54eHhlY2hvLQ==' )
if 43 - 43: Ii1I11I11i1 - ii11i1iIII - Ii1I
def Oo0o0 ( ) :
 if 49 - 49: ooo0oOOOO0o % iii % oO00 - I1i1iI1i - O00oOoOoO0o0O
 iiIi = IiIIIiI1I1 + '|SPLIT|' + OOoO00o
 checker . check ( iiIi )
 if 98 - 98: O00oOoOoO0o0O % i11I1IIiiIi * iiIiIiIi * i11I1IIiiIi
 if not os . path . exists ( IIoOoOo00oOo ) :
  i1 = open ( iiiI11 , mode = 'r' ) ; IiIiiI = i1 . read ( ) ; i1 . close ( )
  common . TextBoxes ( "%s" % IiIiiI )
  I1I = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Do you agree to the terms and conditions of this addon?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if I1I == 1 :
   i1 = open ( OOooO , mode = 'r' ) ; IiIiiI = i1 . read ( ) ; i1 . close ( )
   common . TextBoxes ( "%s" % IiIiiI )
   Ooo . ok ( Oo0Ooo , "[COLOR pink]We can see this is the first time you have used XXX-O-DUS. The next prompt is important as it will allow you to enable the history section of the addon and it will also allow you to select the location you would like to be used to download videos.[/COLOR]" )
   plugintools . open_settings_dialog ( )
   open ( IIoOoOo00oOo , 'w' )
  else :
   sys . exit ( 0 )
   if 80 - 80: i11I1IIiiIi - II1Iiii1111i
 if not os . path . exists ( oo ) :
  I1I = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , "[COLOR white]Would you like to enable the parental controls now?[/COLOR]" , "" , yeslabel = '[COLOR orangered]NO[/COLOR]' , nolabel = '[COLOR lime]YES[/COLOR]' )
  if I1I == 0 :
   OOO00 ( )
  else :
   os . makedirs ( oo )
   if 21 - 21: O0oo0OO0 - O0oo0OO0
 elif os . path . exists ( O0OoOoo00o ) :
  iIii11I = common . _get_keyboard ( heading = "Please Enter Your Password" )
  if ( not iIii11I ) :
   Ooo . ok ( Oo0Ooo , "Sorry, no password was entered." )
   sys . exit ( 0 )
  OOO0OOO00oo = iIii11I
  if 31 - 31: I1i1iI1i - Oooo . iii % i11I1IIiiIi - iii1I1I
  iii11 = open ( O0OoOoo00o , "r" )
  O0oo0OO0oOOOo = re . compile ( r'<password>(.+?)</password>' )
  for i1i1i11IIi in iii11 :
   file = O0oo0OO0oOOOo . findall ( i1i1i11IIi )
   for II1III in file :
    iI1iI1I1i1I = base64 . b64decode ( II1III )
    if not iI1iI1I1i1I == OOO0OOO00oo :
     if not II1III == OOO0OOO00oo :
      Ooo . ok ( Oo0Ooo , "Sorry, the password you entered was incorrect." )
      sys . exit ( 0 )
      if 24 - 24: iiIiIiIi
 o0Oo0O0Oo00oO = plugintools . get_setting ( "download_location" )
 I11i1I1I = xbmc . translatePath ( o0Oo0O0Oo00oO )
 if not os . path . exists ( I11i1I1I ) :
  os . makedirs ( I11i1I1I )
  if 83 - 83: iiIiIiIi / oO00
 if not os . path . isfile ( Ooo00O00O0O0O ) :
  i1 = open ( Ooo00O00O0O0O , 'w' )
  i1 . write ( '#START OF FILE#' )
  i1 . close ( )
 if not os . path . isfile ( OooO0OO ) :
  i1 = open ( OooO0OO , 'w' )
  i1 . write ( '#START OF FILE#' )
  i1 . close ( )
 if not os . path . isfile ( iiiIi ) :
  i1 = open ( iiiIi , 'w' )
  i1 . write ( '#START OF FILE#' )
  i1 . close ( )
  if 49 - 49: oOo
 IIii1Ii1 = open ( O00o ) . read ( )
 I1II11IiII = IIii1Ii1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 OOO0OOo = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( I1II11IiII ) )
 for I1I111 in OOO0OOo :
  i11iiI111I = float ( I1I111 )
 IIii1Ii1 = open ( O00 ) . read ( )
 I1II11IiII = IIii1Ii1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 OOO0OOo = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( I1II11IiII ) )
 for I1I111 in OOO0OOo :
  II11i1iIiII1 = float ( I1I111 )
  if 17 - 17: ooo0oOOOO0o
 common . addDir ( "[COLOR white]SEARCH XXX-O-DUS[/COLOR]" , "url" , 1 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]VIDEOS[/COLOR]" , "url" , 2 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]LIVE[/COLOR]" , "url" , 3 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]PHOTOS[/COLOR]" , "url" , 4 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]STORIES[/COLOR]" , "url" , 5 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]ALL WESBITES[/COLOR]" , "url" , 6 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR darkgray]#################################[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your History[/COLOR]" , OoI1Ii11I1Ii1i , 101 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Favourites[/COLOR]" , OoI1Ii11I1Ii1i , 102 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Downloads[/COLOR]" , OoI1Ii11I1Ii1i , 105 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Your Settings[/COLOR]" , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
 if 62 - 62: O00oOoOoO0o0O * i11I1IIiiIi
 if not os . path . exists ( O0OoOoo00o ) :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR orangered]OFF[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 else :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR lime]ON[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]#####################################[/COLOR]" , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR pink]Twitter Support: [/COLOR][COLOR white]@EchoCoder[/COLOR]" , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Disclaimer[/COLOR]" , iiiI11 , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Addon Information[/COLOR]" , OOooO , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR orangered]RESET XXX-O-DUS[/COLOR]" , 'url' , 997 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Addon Version:[/COLOR] [COLOR white]" + str ( i11iiI111I ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Repository Version:[/COLOR] [COLOR white]" + str ( II11i1iIiII1 ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 if 26 - 26: Ii1I . iii
 oOOOOo0 = common . GET_KODI_VERSION ( )
 if 20 - 20: Oo0ooO0oo0oO + iiIiIiIi - oO00
 if oOOOOo0 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif oOOOOo0 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 30 - 30: I1i1iI1i - Oooo - i11iIiiIii % i11I1IIiiIi - I1i1iI1i * ii11i1iIII
def oO00O0O0O ( ) :
 if 31 - 31: Ii1I11I11i1 - I1i1iI1i . Ii1I11I11i1
 i1I11i1I = ''
 Oo0o00 = xbmc . Keyboard ( i1I11i1I , 'Enter Search Term' )
 Oo0o00 . doModal ( )
 if Oo0o00 . isConfirmed ( ) :
  O0O0oOO00O00o = Oo0o00 . getText ( )
  iI1ii11iIi1i = O0O0oOO00O00o
  i1I11i1I = O0O0oOO00O00o . replace ( ' ' , '+' )
  if len ( i1I11i1I ) > 1 :
   try :
    o0oOoO00o . create ( Oo0Ooo , '[COLOR white]Searching: [/COLOR] [COLOR orangered]YouPorn[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]1 of 7[/COLOR]' )
    iiI111I1iIiI = "http://www.youporn.com/search/?query=" + i1I11i1I . lower ( )
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 15 )
    try :
     youporn . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    iiI111I1iIiI = "http://www.xnxx.com/?k=" + i1I11i1I . lower ( )
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 30 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]XNXX[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]2 of 7[/COLOR]' )
    try :
     xnxx . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    iiI111I1iIiI = "https://xhamster.com/search.php?from=&new=&q=" + i1I11i1I . lower ( ) + "&qcat=video"
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 45 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Xhamster[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]3 of 7[/COLOR]' )
    try :
     xhamster . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    iiI111I1iIiI = "http://www.pornhd.com/search?search=" + i1I11i1I . lower ( )
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 60 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornHD[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]4 of 7[/COLOR]' )
    try :
     pornhd . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    iiI111I1iIiI = "http://www.porn.com/videos/search?q=" + i1I11i1I . lower ( )
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 75 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn.com[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]5 of 7[/COLOR]' )
    try :
     porncom . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    iiI111I1iIiI = "http://www.redtube.com/?search=" + i1I11i1I . lower ( )
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 90 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]RedTube[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]6 of 7[/COLOR]' )
    try :
     redtube . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    iiI111I1iIiI = "http://pornfun.com/search/?q=" + i1I11i1I . lower ( )
    iiI111I1iIiI = 'split|' + iiI111I1iIiI
    o0oOoO00o . update ( 95 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornFun[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1ii11iIi1i . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]7 of 7[/COLOR]' )
    try :
     pornfun . GET_CONTENT ( iiI111I1iIiI )
    except : pass
    o0oOoO00o . close ( )
   except :
    Ooo . ok ( Oo0Ooo , '[COLOR pink]Sorry, there was an error searching for ' + i1I11i1I . lower ( ) + ' please try again later.[/COLOR]' )
    quit ( )
  else : quit ( )
  if 41 - 41: O0OOo . oO00 + iii1I1I * oOo % O0OOo * O0OOo
 oOOOOo0 = common . GET_KODI_VERSION ( )
 if 19 - 19: Ii1I
 if oOOOOo0 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 elif oOOOOo0 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 46 - 46: iiIiIiIi - ii11i1iIII . O00oOoOoO0o0O / iiIiIiIi
def Ii1i ( ) :
 if 15 - 15: ooo0oOOOO0o . O00oOoOoO0o0O . O0oo0OO0 / i11iIiiIii - ii11i1iIII . Oo0ooO0oo0oO
 i1O0OoO0o = 0
 if not os . path . exists ( O0OoOoo00o ) :
  i1O0OoO0o = 1
  common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
 else :
  iii11 = open ( O0OoOoo00o , "r" )
  O0oo0OO0oOOOo = re . compile ( r'<password>(.+?)</password>' )
  for i1i1i11IIi in iii11 :
   file = O0oo0OO0oOOOo . findall ( i1i1i11IIi )
   for II1III in file :
    iI1iI1I1i1I = base64 . b64decode ( II1III )
    i1O0OoO0o = 1
    common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR lime]ON[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR white]Current Password - [/COLOR][COLOR orangered]" + str ( iI1iI1I1i1I ) + "[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR lime]Change Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR orangered]Disable Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
    if 79 - 79: i11I1IIiiIi - iii1I1I * II1Iiii1111i + i11I1IIiiIi % iii1I1I * iii1I1I
 if i1O0OoO0o == 0 :
  common . addLink ( "[COLOR rose]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
  if 61 - 61: I1i1iI1i
def O0OOO ( ) :
 if 10 - 10: Oooo * Ii1I11I11i1 % i11I1IIiiIi / II / i11I1IIiiIi
 iIIi1i1 = plugintools . get_setting ( "history_setting" )
 if 10 - 10: Ii1I11I11i1
 if iIIi1i1 == "true" :
  common . addLink ( '[COLOR deeppink]Clear History[/COLOR]' , OoI1Ii11I1Ii1i , 104 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR orangered]Disable History[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '###########################################' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
  if 82 - 82: iiIiIiIi - O00oOoOoO0o0O / Oooo + ii11i1iIII
  i1 = open ( Ooo00O00O0O0O , mode = 'r' ) ; IiIiiI = i1 . read ( ) ; i1 . close ( )
  IiIiiI = IiIiiI . replace ( '\n' , '' )
  OOO0OOo = re . compile ( '<item>(.+?)</item>' ) . findall ( IiIiiI )
  for I1I111 in OOO0OOo :
   OOOOoOoo0O0O0 = re . compile ( '<date>(.+?)</date>' ) . findall ( I1I111 ) [ 0 ]
   time = re . compile ( '<time>(.+?)</time>' ) . findall ( I1I111 ) [ 0 ]
   OOOo00oo0oO = re . compile ( '<name>(.+?)</name>' ) . findall ( I1I111 ) [ 0 ]
   iiI111I1iIiI = re . compile ( '<link>(.+?)</link>' ) . findall ( I1I111 ) [ 0 ]
   IIiIi1iI = re . compile ( '<site>(.+?)</site>' ) . findall ( I1I111 ) [ 0 ]
   i1IiiiI1iI = re . compile ( '<icon>(.+?)</icon>' ) . findall ( I1I111 ) [ 0 ]
   iiI111I1iIiI = OOOo00oo0oO + '|SPLIT|' + iiI111I1iIiI + '|SPLIT|' + IIiIi1iI + '|SPLIT|' + i1IiiiI1iI + '|SPLIT|' + iiI111I1iIiI
   if 49 - 49: ii11i1iIII / II1Iiii1111i . I1i1iI1i
   common . addLink ( '[COLOR pink]' + OOOOoOoo0O0O0 + ' | ' + '[/COLOR][COLOR deeppink]' + time + '[/COLOR] - [COLOR orangered]' + IIiIi1iI + '[/COLOR][COLOR pink] - ' + OOOo00oo0oO + '[/COLOR]' , iiI111I1iIiI , 800 , i1IiiiI1iI , O0O0OO0O0O0 )
 else :
  common . addLink ( '[COLOR orangered]Enable History Monitoring[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '############################################' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR pink]History monitoring is currently disabled.[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  if 68 - 68: i11iIiiIii % iiIiIiIi + i11iIiiIii
def iiiII1I ( ) :
 if 84 - 84: ooo0oOOOO0o . i11iIiiIii . ooo0oOOOO0o * iiIiIiIi - Ii1I11I11i1
 common . addLink ( '[COLOR deeppink]Your Favourites[/COLOR]' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 if 42 - 42: i11iIiiIii
 i1 = open ( OooO0OO , mode = 'r' ) ; IiIiiI = i1 . read ( ) ; i1 . close ( )
 IiIiiI = IiIiiI . replace ( '\n' , '' )
 OOO0OOo = re . compile ( '<item>(.+?)</item>' ) . findall ( IiIiiI )
 for I1I111 in OOO0OOo :
  OOOo00oo0oO = re . compile ( '<name>(.+?)</name>' ) . findall ( I1I111 ) [ 0 ]
  iiI111I1iIiI = re . compile ( '<link>(.+?)</link>' ) . findall ( I1I111 ) [ 0 ]
  IIiIi1iI = re . compile ( '<site>(.+?)</site>' ) . findall ( I1I111 ) [ 0 ]
  i1IiiiI1iI = re . compile ( '<icon>(.+?)</icon>' ) . findall ( I1I111 ) [ 0 ]
  iiI111I1iIiI = OOOo00oo0oO + '|SPLIT|' + iiI111I1iIiI + '|SPLIT|' + IIiIi1iI + '|SPLIT|' + i1IiiiI1iI + '|SPLIT|' + iiI111I1iIiI
  common . addLink ( '[COLOR orangered]' + IIiIi1iI + '[/COLOR][COLOR pink] - ' + OOOo00oo0oO + '[/COLOR]' , iiI111I1iIiI , 103 , i1IiiiI1iI , O0O0OO0O0O0 )
  if 33 - 33: Ii1I - iii1I1I * Oo0ooO0oo0oO * oOo - O0OOo
def iiIiI ( name , url , iconimage ) :
 if 91 - 91: Ii1I % Oo0ooO0oo0oO % O00oOoOoO0o0O
 IIi1I11I1II = url
 IIii1Ii1 , I1II11IiII , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 if 81 - 81: i11I1IIiiIi / iii1I1I . ooo0oOOOO0o . II
 i1I11i1I = '\n<item>\n<name>' + IIii1Ii1 + '</name>\n<link>' + I1II11IiII + '</link>\n<site>' + OooOoooOo + '</site>\n<icon>' + ii11IIII11I + '</icon>\n</item>\n'
 if 72 - 72: Oo0ooO0oo0oO / II1Iiii1111i + O0oo0OO0 - O0OOo
 I1I = Ooo . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Remove from Favourites[/B][/COLOR]' ] )
 if 29 - 29: iiIiIiIi + o0oooO0OO0O % iii1I1I
 if I1I == 0 :
  I1I11 ( name , IIi1I11I1II , iconimage )
 else :
  II1o0oO00000 = open ( OooO0OO ) . read ( )
  i1 = II1o0oO00000 . replace ( i1I11i1I , '\n' )
  OOOOoo0Oo = open ( OooO0OO , mode = 'w' )
  OOOOoo0Oo . write ( str ( i1 ) )
  OOOOoo0Oo . close ( )
  xbmc . executebuiltin ( "Container.Refresh" )
  quit ( )
  if 14 - 14: Ii1I
def I1iI1iIi111i ( name , url , iconimage ) :
 if 44 - 44: Oo0ooO0oo0oO % I1i1iI1i + Ii1I11I11i1
 IIi1I11I1II = url
 IIii1Ii1 , I1II11IiII , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 if 45 - 45: Ii1I / Ii1I + iii + oO00
 I1I = Ooo . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Delete Download[/B][/COLOR]' ] )
 if 47 - 47: oOo + oO00
 if I1I == 0 :
  I1I11 ( name , IIi1I11I1II , iconimage )
 else :
  os . remove ( url )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 82 - 82: I1i1iI1i . ooo0oOOOO0o - O00oOoOoO0o0O - ooo0oOOOO0o * I1i1iI1i
def ooO0oOOooOo0 ( ) :
 if 38 - 38: iii
 if os . path . isfile ( Ooo00O00O0O0O ) :
  I1I = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Would you like to clear all stored history?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[B][COLOR orangered]NO[/COLOR][/B]' )
  if I1I == 1 :
   os . remove ( Ooo00O00O0O0O )
   i1 = open ( Ooo00O00O0O0O , 'w' )
   i1 . write ( '#START OF FILE#' )
   i1 . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 84 - 84: O00oOoOoO0o0O % Ii1I / O00oOoOoO0o0O % Ii1I11I11i1
def ii ( ) :
 if 84 - 84: oOo % I1i1iI1i . i11iIiiIii / II1Iiii1111i
 o0Oo0O0Oo00oO = plugintools . get_setting ( "download_location" )
 o0OIiII = xbmc . translatePath ( o0Oo0O0Oo00oO )
 common . addLink ( '[COLOR deeppink]Download Location: [/COLOR]' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( o0OIiII , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '[COLOR orangered]Change Download Location[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 if 25 - 25: iii1I1I - iii1I1I * oOo
 OOOO0oo0 = [ '.mp4' ]
 if 35 - 35: ii11i1iIII - II % oOo . O0oo0OO0 % ii11i1iIII
 for file in os . listdir ( o0OIiII ) :
  for I1i1Iiiii in OOOO0oo0 :
   if file . endswith ( I1i1Iiiii ) :
    i1IiiiI1iI = iiiii
    i1 = open ( iiiIi , mode = 'r' ) ; IiIiiI = i1 . read ( ) ; i1 . close ( )
    IiIiiI = IiIiiI . replace ( '\n' , '' )
    OOO0OOo = re . compile ( '<item>(.+?)</item>' ) . findall ( IiIiiI )
    for I1I111 in OOO0OOo :
     OOOo00oo0oO = re . compile ( '<name>(.+?)</name>' ) . findall ( I1I111 ) [ 0 ]
     OOo0oO00ooO00 = re . compile ( '<icon>(.+?)</icon>' ) . findall ( I1I111 ) [ 0 ]
     if file in OOOo00oo0oO :
      i1IiiiI1iI = OOo0oO00ooO00
    iiI111I1iIiI = xbmc . translatePath ( os . path . join ( o0OIiII , file ) )
    if "http" in i1IiiiI1iI :
     oOO0O00oO0Ooo = file + '|SPLIT|' + iiI111I1iIiI + '|SPLIT|Downloaded|SPLIT|' + i1IiiiI1iI + '|SPLIT|' + iiI111I1iIiI
    else :
     oOO0O00oO0Ooo = file + '|SPLIT|' + iiI111I1iIiI + '|SPLIT|Downloaded|SPLIT|None|SPLIT|' + iiI111I1iIiI
    common . addLink ( '[COLOR pink]' + file + '[/COLOR]' , oOO0O00oO0Ooo , 107 , i1IiiiI1iI , O0O0OO0O0O0 )
    if 67 - 67: II1Iiii1111i - Oooo
def iI1i11iII111 ( ) :
 if 15 - 15: i11iIiiIii % ii11i1iIII . O0OOo + iiIiIiIi
 o0Oo0O0Oo00oO = plugintools . get_setting ( "download_location" )
 OO0OOOOoo0OOO = Ooo . browse ( 3 , Oo0Ooo , 'files' , '' , False , False , i1IIi11111i )
 II1o0oO00000 = open ( o000o0o00o0Oo ) . read ( )
 i1 = II1o0oO00000 . replace ( o0Oo0O0Oo00oO , OO0OOOOoo0OOO )
 OOOOoo0Oo = open ( o000o0o00o0Oo , mode = 'w' )
 OOOOoo0Oo . write ( str ( i1 ) )
 OOOOoo0Oo . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 27 - 27: oO00 + I1i1iI1i
def o0Oo00 ( name , url , iconimage ) :
 if 32 - 32: oOo . ooo0oOOOO0o * Ii1I11I11i1
 IIii1Ii1 , I1II11IiII , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 name = IIii1Ii1
 OOooo0oOO0O = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 o00O0 = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 i1I11i1I = '\n<item>\n<date>' + OOooo0oOO0O + '</date>\n<time>' + o00O0 + '</time>\n<name>' + IIii1Ii1 + '</name>\n<link>' + I1II11IiII + '</link>\n<site>' + OooOoooOo + '</site>\n<icon>' + ii11IIII11I + '</icon>\n</item>\n'
 IIii1Ii1 = open ( Ooo00O00O0O0O ) . read ( )
 I1II11IiII = IIii1Ii1 . replace ( '#START OF FILE#' , '#START OF FILE#' + i1I11i1I )
 i1 = open ( Ooo00O00O0O0O , mode = 'w' )
 i1 . write ( str ( I1II11IiII ) )
 i1 . close ( )
 if 83 - 83: oO00
 if iconimage == "None" :
  iconimage = iiiii
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 13 - 13: O0oo0OO0
def I1I11 ( name , url , iconimage ) :
 if 33 - 33: iii + Ii1I * o0oooO0OO0O / O00oOoOoO0o0O - II
 IIii1Ii1 , I1II11IiII , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 name = IIii1Ii1
 OOooo0oOO0O = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 o00O0 = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 i1I11i1I = '\n<item>\n<date>' + OOooo0oOO0O + '</date>\n<time>' + o00O0 + '</time>\n<name>' + IIii1Ii1 + '</name>\n<link>' + I1II11IiII + '</link>\n<site>' + OooOoooOo + '</site>\n<icon>' + ii11IIII11I + '</icon>\n</item>\n'
 IIii1Ii1 = open ( Ooo00O00O0O0O ) . read ( )
 I1II11IiII = IIii1Ii1 . replace ( '#START OF FILE#' , '#START OF FILE#' + i1I11i1I )
 i1 = open ( Ooo00O00O0O0O , mode = 'w' )
 i1 . write ( str ( I1II11IiII ) )
 i1 . close ( )
 if 54 - 54: iii / Oooo . o0oooO0OO0O % Ii1I
 if iconimage == "None" :
  iconimage = iiiii
  if 57 - 57: i11iIiiIii . iiIiIiIi - ii11i1iIII - o0oooO0OO0O + i11I1IIiiIi
 if "highwebmedia" in url :
  Ooo . ok ( Oo0Ooo , '[COLOR pink]Chaturbate links are taken at the time of broadcasting. If this broadcast has ended the link will no longer play. [/COLOR]' )
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 63 - 63: i11I1IIiiIi * Ii1I
def OOO00 ( ) :
 if 69 - 69: iii1I1I . II1Iiii1111i
 iIii11I = common . _get_keyboard ( heading = "Please Set Password" )
 if ( not iIii11I ) :
  Ooo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 OOO0OOO00oo = iIii11I
 if 49 - 49: II - Ii1I11I11i1
 iIii11I = common . _get_keyboard ( heading = "Please Confirm Your Password" )
 if ( not iIii11I ) :
  Ooo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 OoOOoOooooOOo = iIii11I
 if 87 - 87: II
 if not os . path . exists ( O0OoOoo00o ) :
  if not os . path . exists ( oo ) :
   os . makedirs ( oo )
  open ( O0OoOoo00o , 'w' )
  if 58 - 58: i11I1IIiiIi % oOo
  if OOO0OOO00oo == OoOOoOooooOOo :
   i1OOoO = base64 . b64encode ( OOO0OOO00oo )
   i1 = open ( O0OoOoo00o , 'w' )
   i1 . write ( '<password>' + str ( i1OOoO ) + '</password>' )
   i1 . close ( )
   Ooo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   Ooo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
 else :
  os . remove ( O0OoOoo00o )
  if 89 - 89: oOo + II1Iiii1111i * Ii1I11I11i1 * ii11i1iIII
  if OOO0OOO00oo == OoOOoOooooOOo :
   i1OOoO = base64 . b64encode ( OOO0OOO00oo )
   i1 = open ( O0OoOoo00o , 'w' )
   i1 . write ( '<password>' + str ( i1OOoO ) + '</password>' )
   i1 . close ( )
   Ooo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   Ooo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
   if 37 - 37: O0oo0OO0 - iii1I1I - oOo
def o0o0O0O00oOOo ( ) :
 if 14 - 14: i11I1IIiiIi + o0oooO0OO0O
 try :
  os . remove ( O0OoOoo00o )
  Ooo . ok ( Oo0Ooo , 'Parental controls have been disabled.' )
  xbmc . executebuiltin ( "Container.Refresh" )
 except :
  Ooo . ok ( Oo0Ooo , 'There was an error disabling the parental controls.' )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 52 - 52: O0oo0OO0 - oO00
def o0O0o0 ( ) :
 if 37 - 37: iiIiIiIi * Ii1I11I11i1 % i11iIiiIii % oO00 + ii11i1iIII
 OOoOO0o0o0 = 0
 if 11 - 11: II
 try :
  common . open_url ( "http://www.google.com" )
 except :
  Ooo . ok ( Oo0Ooo , '[COLOR orangered]Error: It appears you do not currently have an active internet connection. This will cause false positives in the test. Please try again with an active internet connection.[/COLOR]' )
  return
  if 16 - 16: ii11i1iIII + ooo0oOOOO0o * iii1I1I % Oo0ooO0oo0oO . II
 o0oOoO00o . create ( Oo0Ooo , "Checking for repository updates" , '' , 'Please Wait...' )
 o0oOoO00o . update ( 0 )
 IIii1Ii1 = open ( O00 ) . read ( )
 I1II11IiII = IIii1Ii1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 OOO0OOo = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( I1II11IiII ) )
 for I1I111 in OOO0OOo :
  o0oOoO00o . update ( 25 )
  Oo0OO = float ( I1I111 ) + 0.01
  iiI111I1iIiI = Ii11Ii11I + str ( Oo0OO ) + '.zip'
  try :
   O0OooOo0o = common . open_url ( iiI111I1iIiI )
   if "Not Found" not in O0OooOo0o :
    i1O0OoO0o = 1
    o0oOoO00o . update ( 75 )
    iiI11ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( iiI11ii1I1 ) :
     os . makedirs ( iiI11ii1I1 )
    Ooo0OOoOoO0 = os . path . join ( iiI11ii1I1 , 'repoupdate.zip' )
    try : os . remove ( Ooo0OOoOoO0 )
    except : pass
    o0oOoO00o . update ( 100 )
    o0oOoO00o . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( iiI111I1iIiI , Ooo0OOoOoO0 , o0oOoO00o )
    oOo0OOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    o0oOoO00o . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( Ooo0OOoOoO0 , oOo0OOoO0 , o0oOoO00o )
    try : os . remove ( Ooo0OOoOoO0 )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    OOoOO0o0o0 = 1
    Ooo . ok ( Oo0Ooo , "ECHO XXX repository was updated to " + str ( Oo0OO ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 11 - 11: iiIiIiIi . II1Iiii1111i * ooo0oOOOO0o * O0oo0OO0 + oO00
 o0oOoO00o . update ( 75 , "Checking for addon updates" )
 IIii1Ii1 = open ( O00o ) . read ( )
 I1II11IiII = IIii1Ii1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 OOO0OOo = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( I1II11IiII ) )
 for I1I111 in OOO0OOo :
  Oo0OO = float ( I1I111 ) + 0.01
  iiI111I1iIiI = i11I1 + str ( Oo0OO ) + '.zip'
  try :
   O0OooOo0o = common . open_url ( iiI111I1iIiI )
   if "Not Found" not in O0OooOo0o :
    i1O0OoO0o = 1
    o0oOoO00o . update ( 75 )
    iiI11ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( iiI11ii1I1 ) :
     os . makedirs ( iiI11ii1I1 )
    Ooo0OOoOoO0 = os . path . join ( iiI11ii1I1 , 'xxx_o_dus_update.zip' )
    try : os . remove ( Ooo0OOoOoO0 )
    except : pass
    o0oOoO00o . update ( 100 )
    o0oOoO00o . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( iiI111I1iIiI , Ooo0OOoOoO0 , o0oOoO00o )
    oOo0OOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    o0oOoO00o . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( Ooo0OOoOoO0 , oOo0OOoO0 , o0oOoO00o )
    try : os . remove ( Ooo0OOoOoO0 )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    o0oOoO00o . update ( 100 )
    o0oOoO00o . close
    OOoOO0o0o0 = 1
    Ooo . ok ( Oo0Ooo , "XXX-O-DUS was updated to " + str ( Oo0OO ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 33 - 33: iii1I1I * oOo - iii % iii
 if o0oOoO00o . iscanceled ( ) :
  o0oOoO00o . close ( )
  if 18 - 18: iii / O0OOo * iii + iii * i11iIiiIii * iiIiIiIi
 return OOoOO0o0o0
 if 11 - 11: oO00 / i11I1IIiiIi - ooo0oOOOO0o * O0oo0OO0 + O0oo0OO0 . i11I1IIiiIi
def i1I1i111Ii ( url ) :
 if 67 - 67: II . Oo0ooO0oo0oO
 i1 = open ( url , mode = 'r' ) ; IiIiiI = i1 . read ( ) ; i1 . close ( )
 common . TextBoxes ( "%s" % IiIiiI )
 if 27 - 27: oO00 % II
 if url == II111iiii :
  return
  if 73 - 73: Oooo
def ooO ( ) :
 if 51 - 51: II % iii . o0oooO0OO0O / O00oOoOoO0o0O / Ii1I11I11i1 . o0oooO0OO0O
 try :
  i1I1i111Ii ( II111iiii )
  if 42 - 42: oOo + Oo0ooO0oo0oO - ii11i1iIII / ooo0oOOOO0o
  I1I = xbmcgui . Dialog ( ) . yesno ( "[COLOR orangered][B]RESET XXX-O-DUS?[/B][/COLOR]" , '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]' , '' , yeslabel = '[COLOR green]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if I1I == 1 :
   o0Oo0O0Oo00oO = plugintools . get_setting ( "download_location" )
   o0OIiII = xbmc . translatePath ( o0Oo0O0Oo00oO )
   if 9 - 9: iii1I1I % iii1I1I - oOo
   OOOO0oo0 = [ '.mp4' ]
   if 51 - 51: II . O00oOoOoO0o0O - iiIiIiIi / iii1I1I
   for file in os . listdir ( o0OIiII ) :
    for I1i1Iiiii in OOOO0oo0 :
     if file . endswith ( I1i1Iiiii ) :
      try :
       iiI11ii1I1 = xbmc . translatePath ( os . path . join ( o0OIiII , file ) )
       os . remove ( iiI11ii1I1 )
      except :
       Ooo . ok ( Oo0Ooo , "[COLOR white]There was an error deleting " + file + "[/COLOR]" )
       pass
   try :
    shutil . rmtree ( IiII1I1i1i1ii )
   except :
    Ooo . ok ( Oo0Ooo , "[COLOR white]There was an error deleting deleting the data directory.[/COLOR]" )
    pass
   Ooo . ok ( Oo0Ooo , "[COLOR white]XXX-O-DUS has been reset to the factory state.[/COLOR]" , "[COLOR white]Press OK to continue.[/COLOR]" )
   xbmc . executebuiltin ( "Container.Refresh" )
 except :
  Ooo . ok ( Oo0Ooo , "[COLOR white]Sorry, something went wrong.[/COLOR]" , "[COLOR white]Please report this issue to @EchoCoder on Twitter.[/COLOR]" )
  quit ( )
  if 52 - 52: oOo + iii1I1I + Ii1I + O0OOo % Ii1I
def OO ( ) :
 Ii1iI111II1I1 = [ ]
 oOOOOoOO0o = sys . argv [ 2 ]
 if len ( oOOOOoOO0o ) >= 2 :
  i1II1 = sys . argv [ 2 ]
  i11i1 = i1II1 . replace ( '?' , '' )
  if ( i1II1 [ len ( i1II1 ) - 1 ] == '/' ) :
   i1II1 = i1II1 [ 0 : len ( i1II1 ) - 2 ]
  IiiiiI1i1Iii = i11i1 . split ( '&' )
  Ii1iI111II1I1 = { }
  for oo00oO0o in range ( len ( IiiiiI1i1Iii ) ) :
   iiii111II = { }
   iiii111II = IiiiiI1i1Iii [ oo00oO0o ] . split ( '=' )
   if ( len ( iiii111II ) ) == 2 :
    Ii1iI111II1I1 [ iiii111II [ 0 ] ] = iiii111II [ 1 ]
    if 50 - 50: Oooo * II % O00oOoOoO0o0O + ii11i1iIII + Ii1I + II
 return Ii1iI111II1I1
 if 71 - 71: iiIiIiIi * iiIiIiIi * Oo0ooO0oo0oO . o0oooO0OO0O / iii
i1II1 = OO ( ) ; ooo0O0o00O = None ; iiI111I1iIiI = None ; I1i11 = None ; i1IiiiI1iI = None ; IiIi1I1 = None
try : ooo0O0o00O = urllib . unquote_plus ( i1II1 [ "name" ] )
except : pass
try : iiI111I1iIiI = urllib . unquote_plus ( i1II1 [ "url" ] )
except : pass
try : I1i11 = int ( i1II1 [ "mode" ] )
except : pass
try : i1IiiiI1iI = urllib . unquote_plus ( i1II1 [ "iconimage" ] )
except : pass
try : IiIi1I1 = urllib . quote_plus ( i1II1 [ "fanartimage" ] )
except : pass
if 39 - 39: I1i1iI1i + i11I1IIiiIi - oO00 . i11I1IIiiIi
if I1i11 == None or iiI111I1iIiI == None or len ( iiI111I1iIiI ) < 1 : Oo0o0 ( )
elif I1i11 == 1 : menus . SEARCH ( )
elif I1i11 == 2 : menus . VIDEOS ( )
elif I1i11 == 3 : menus . LIVE ( )
elif I1i11 == 4 : menus . PICTURES ( )
elif I1i11 == 5 : menus . STORIES ( )
elif I1i11 == 6 : menus . ALL ( )
elif I1i11 == 10 : xhamster . MAIN_MENU ( )
elif I1i11 == 11 : xhamster . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 12 : xhamster . SEARCH ( )
elif I1i11 == 13 : xhamster . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 20 : chaturbate . MAIN_MENU ( )
elif I1i11 == 21 : chaturbate . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 22 : chaturbate . SEARCH ( )
elif I1i11 == 23 : chaturbate . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 30 : xnxx . MAIN_MENU ( )
elif I1i11 == 31 : xnxx . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 32 : xnxx . SEARCH ( )
elif I1i11 == 33 : xnxx . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 34 : xnxx . PICTURE_MENU ( )
elif I1i11 == 35 : xnxx . PICTURE_CONTENT ( iiI111I1iIiI )
elif I1i11 == 36 : xnxx . SCRAPE_GALLERY ( iiI111I1iIiI )
elif I1i11 == 37 : xnxx . DISPLAY_PICTURE ( iiI111I1iIiI )
elif I1i11 == 38 : xnxx . STORY_MENU ( )
elif I1i11 == 39 : xnxx . LIST_STORIES ( iiI111I1iIiI )
elif I1i11 == 40 : xnxx . DISPLAY_STORY ( iiI111I1iIiI )
elif I1i11 == 41 : redtube . MAIN_MENU ( )
elif I1i11 == 42 : redtube . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 43 : redtube . SEARCH ( )
elif I1i11 == 44 : redtube . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 50 : pornhd . MAIN_MENU ( )
elif I1i11 == 51 : pornhd . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 52 : pornhd . SEARCH ( )
elif I1i11 == 53 : pornhd . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 60 : porncom . MAIN_MENU ( )
elif I1i11 == 61 : porncom . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 62 : porncom . SEARCH ( )
elif I1i11 == 63 : porncom . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 70 : youporn . MAIN_MENU ( )
elif I1i11 == 71 : youporn . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 72 : youporn . SEARCH ( )
elif I1i11 == 73 : youporn . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 80 : pornfun . MAIN_MENU ( )
elif I1i11 == 81 : pornfun . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 82 : pornfun . SEARCH ( )
elif I1i11 == 83 : pornfun . PLAY_URL ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 90 : motherless . MAIN_MENU ( )
elif I1i11 == 91 : motherless . GET_CONTENT ( iiI111I1iIiI )
elif I1i11 == 92 : motherless . DISPLAY_PICTURE ( iiI111I1iIiI )
elif I1i11 == 100 : oO00O0O0O ( ) ;
elif I1i11 == 101 : O0OOO ( )
elif I1i11 == 102 : iiiII1I ( )
elif I1i11 == 103 : iiIiI ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 104 : ooO0oOOooOo0 ( )
elif I1i11 == 105 : ii ( )
elif I1i11 == 106 : plugintools . open_settings_dialog ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
elif I1i11 == 107 : I1iI1iIi111i ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 800 : I1I11 ( ooo0O0o00O , iiI111I1iIiI , i1IiiiI1iI )
elif I1i11 == 900 : Ii1i ( )
elif I1i11 == 901 : OOO00 ( )
elif I1i11 == 902 : o0o0O0O00oOOo ( )
elif I1i11 == 997 : ooO ( )
elif I1i11 == 998 : i1I1i111Ii ( iiI111I1iIiI )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
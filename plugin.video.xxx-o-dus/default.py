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
from resources . lib . scrapers import spankbang
from resources . lib . scrapers import porn00
from resources . lib . scrapers import virtualpornstars
from resources . lib . scrapers import watchxxxfree
from resources . lib . scrapers import perfectgirls
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
IiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/spankbang/icon.png' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/spankbang/fanart.jpg' ) )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/watchxxxfree/icon.png' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'resources/art/watchxxxfree/fanart.jpg' ) )
if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
iiI1iIiI = base64 . decodestring ( 'aHR0cDovL2VjaG9jb2Rlci5jb20vcHJpdmF0ZS9hZGRvbnMvc3BvcnRpZS9tZW51cy9tYWluLnhtbA==' )
OOo = xbmcgui . Dialog ( )
Ii1IIii11 = xbmcgui . DialogProgress ( )
if 55 - 55: i1111 - i1IIi11111i / I11i1i11i1I % oo / OOO0O / oo0ooO0oOOOOo
oO000OoOoo00o = xbmc . translatePath ( 'special://home/' )
iiiI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o , 'settings.xml' ) )
OOooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o , 'parental' ) )
OOoO00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o ) )
II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o ) )
II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.f4mTester' ) )
oOoOo00oOo = xbmc . translatePath ( os . path . join ( OOooO , 'controls.txt' ) )
Ooo00O00O0O0O = xbmc . translatePath ( os . path . join ( II111iiii , 'resources/disclaimer.txt' ) )
OooO0OO = xbmc . translatePath ( os . path . join ( II111iiii , 'resources/information.txt' ) )
iiiIi = xbmc . translatePath ( os . path . join ( II111iiii , 'resources/repository.txt' ) )
IiIIIiI1I1 = xbmc . translatePath ( os . path . join ( II111iiii , 'resources/reset.txt' ) )
OoO000 = xbmc . translatePath ( os . path . join ( OOoO00o , 'agreed.txt' ) )
IIiiIiI1 = xbmc . translatePath ( os . path . join ( OOoO00o , 'history.xml' ) )
iiIiIIi = xbmc . translatePath ( os . path . join ( OOoO00o , 'favourites.xml' ) )
ooOoo0O = xbmc . translatePath ( os . path . join ( OOoO00o , 'downloads.xml' ) )
OooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.xxxecho' ) )
if 35 - 35: Ooooo0Oo00oO0 % Ooo . oo0Oo00Oo0 % oOOO00o
O0O00o0OOO0 = xbmc . translatePath ( 'special://home/addons/' + OO0o + '/addon.xml' )
Ii1iIIIi1ii = xbmc . translatePath ( 'special://home/addons/repository.xxxecho/addon.xml' )
o0oo0o0O00OO = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9wbHVnaW4udmlkZW8ueHh4LW8tZHVzL3BsdWdpbi52aWRlby54eHgtby1kdXMt' )
o0oO = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9yZXBvc2l0b3J5Lnh4eGVjaG8vcmVwb3NpdG9yeS54eHhlY2hvLQ==' )
if 48 - 48: ooooooO0oo + OooooooO + Oo0O0OOOoo / oOoOooOo0o0
def OOOO ( ) :
 if 87 - 87: O0ooOooooO / i1111 - oOOO00o / OOO0O % oOoOooOo0o0 % ooooooO0oo
 OOOO00ooo0Ooo = OooO0 + '|SPLIT|' + iiiIi
 checker . check ( OOOO00ooo0Ooo )
 if 69 - 69: oo0ooO0oOOOOo * oooO0oo0oOOOO + oo . i1111 / oooO0oo0oOOOO
 if not os . path . exists ( OoO000 ) :
  O000oo0O = open ( Ooo00O00O0O0O , mode = 'r' ) ; OOOOi11i1 = O000oo0O . read ( ) ; O000oo0O . close ( )
  common . TextBoxes ( "%s" % OOOOi11i1 )
  IIIii1II1II = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Do you agree to the terms and conditions of this addon?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if IIIii1II1II == 1 :
   O000oo0O = open ( OooO0OO , mode = 'r' ) ; OOOOi11i1 = O000oo0O . read ( ) ; O000oo0O . close ( )
   common . TextBoxes ( "%s" % OOOOi11i1 )
   OOo . ok ( Oo0Ooo , "[COLOR pink]We can see this is the first time you have used XXX-O-DUS. The next prompt is important as it will allow you to enable the history section of the addon and it will also allow you to select the location you would like to be used to download videos.[/COLOR]" )
   plugintools . open_settings_dialog ( )
   open ( OoO000 , 'w' )
  else :
   sys . exit ( 0 )
   if 42 - 42: ooooooO0oo + Ooo
 if not os . path . exists ( OOooO ) :
  IIIii1II1II = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , "[COLOR white]Would you like to enable the parental controls now?[/COLOR]" , "" , yeslabel = '[COLOR orangered]NO[/COLOR]' , nolabel = '[COLOR lime]YES[/COLOR]' )
  if IIIii1II1II == 0 :
   o0O0o0Oo ( )
  else :
   os . makedirs ( OOooO )
   if 16 - 16: oooO0oo0oOOOO - oOoOooOo0o0 * ooO0oo0oO0 + OooooooO
 elif os . path . exists ( oOoOo00oOo ) :
  Ii11iII1 = common . _get_keyboard ( heading = "Please Enter Your Password" )
  if ( not Ii11iII1 ) :
   OOo . ok ( Oo0Ooo , "Sorry, no password was entered." )
   sys . exit ( 0 )
  Oo0O0O0ooO0O = Ii11iII1
  if 15 - 15: Ooooo0Oo00oO0 + OOO0O - i111I / oo0Oo00Oo0
  oo000OO00Oo = open ( oOoOo00oOo , "r" )
  O0OOO0OOoO0O = re . compile ( r'<password>(.+?)</password>' )
  for O00Oo000ooO0 in oo000OO00Oo :
   file = O0OOO0OOoO0O . findall ( O00Oo000ooO0 )
   for OoO0O00 in file :
    IIiII = base64 . b64decode ( OoO0O00 )
    if not IIiII == Oo0O0O0ooO0O :
     if not OoO0O00 == Oo0O0O0ooO0O :
      OOo . ok ( Oo0Ooo , "Sorry, the password you entered was incorrect." )
      sys . exit ( 0 )
      if 80 - 80: Oo0O0OOOoo . Ooo
 IIi = plugintools . get_setting ( "download_location" )
 i11iIIIIIi1 = xbmc . translatePath ( IIi )
 if not os . path . exists ( i11iIIIIIi1 ) :
  os . makedirs ( i11iIIIIIi1 )
  if 20 - 20: II1Ii1iI1i + Ooooo0Oo00oO0 - O0ooOooooO
 if not os . path . isfile ( IIiiIiI1 ) :
  O000oo0O = open ( IIiiIiI1 , 'w' )
  O000oo0O . write ( '#START OF FILE#' )
  O000oo0O . close ( )
 if not os . path . isfile ( iiIiIIi ) :
  O000oo0O = open ( iiIiIIi , 'w' )
  O000oo0O . write ( '#START OF FILE#' )
  O000oo0O . close ( )
 if not os . path . isfile ( ooOoo0O ) :
  O000oo0O = open ( ooOoo0O , 'w' )
  O000oo0O . write ( '#START OF FILE#' )
  O000oo0O . close ( )
  if 30 - 30: i1111 - oo0Oo00Oo0 - i11iIiiIii % OOO0O - i1111 * ooooooO0oo
 oO00O0O0O = open ( O0O00o0OOO0 ) . read ( )
 i1ii1iiI = oO00O0O0O . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0o0O00Oo0o0 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( i1ii1iiI ) )
 for O00O0oOO00O00 in O0o0O00Oo0o0 :
  i1 = float ( O00O0oOO00O00 )
 oO00O0O0O = open ( Ii1iIIIi1ii ) . read ( )
 i1ii1iiI = oO00O0O0O . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0o0O00Oo0o0 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( i1ii1iiI ) )
 for O00O0oOO00O00 in O0o0O00Oo0o0 :
  Oo00 = float ( O00O0oOO00O00 )
  if 31 - 31: oOoOooOo0o0 . OOO0O / oooO0oo0oOOOO
 common . addDir ( "[COLOR white]SEARCH XXX-O-DUS[/COLOR]" , "url" , 1 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Live[/COLOR]" , "url" , 3 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Videos[/COLOR]" , "url" , 2 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Photos[/COLOR]" , "url" , 4 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Stories[/COLOR]" , "url" , 5 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]All Websites[/COLOR]" , "url" , 6 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR darkgray]#################################[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your History[/COLOR]" , iiI1iIiI , 101 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Favourites[/COLOR]" , iiI1iIiI , 102 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Downloads[/COLOR]" , iiI1iIiI , 105 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Your Settings[/COLOR]" , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
 if 89 - 89: OOO0O
 if not os . path . exists ( oOoOo00oOo ) :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR orangered]OFF[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 else :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR lime]ON[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]#####################################[/COLOR]" , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR pink]Twitter Support: [/COLOR][COLOR white]@EchoCoder[/COLOR]" , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Disclaimer[/COLOR]" , Ooo00O00O0O0O , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Addon Information[/COLOR]" , OooO0OO , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR orangered]RESET XXX-O-DUS[/COLOR]" , 'url' , 997 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Addon Version:[/COLOR] [COLOR white]" + str ( i1 ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Repository Version:[/COLOR] [COLOR white]" + str ( Oo00 ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 if 68 - 68: oo * i111I % oooO0oo0oOOOO + oo + O0ooOooooO
 i11i1I1 = common . GET_KODI_VERSION ( )
 if 36 - 36: ooO0oo0oO0 / OOO0O * oo0Oo00Oo0
 if i11i1I1 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif i11i1I1 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 65 - 65: ooooooO0oo . ooO0oo0oO0 / oooO0oo0oOOOO - ooooooO0oo
def iii1i1iiiiIi ( ) :
 if 2 - 2: i1IIi11111i / oooO0oo0oOOOO / oo0ooO0oOOOOo % OOO0O % ooooooO0oo
 o0o00OO0 = ''
 i1I1ii = xbmc . Keyboard ( o0o00OO0 , 'Enter Search Term' )
 i1I1ii . doModal ( )
 if i1I1ii . isConfirmed ( ) :
  oOOo0 = i1I1ii . getText ( )
  oo00O00oO = oOOo0
  o0o00OO0 = oOOo0 . replace ( ' ' , '+' )
  if len ( o0o00OO0 ) > 1 :
   try :
    Ii1IIii11 . create ( Oo0Ooo , '[COLOR white]Searching: [/COLOR] [COLOR orangered]YouPorn[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]1 of 11[/COLOR]' )
    iIiIIIi = "http://www.youporn.com/search/?query=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 15 )
    try :
     youporn . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://www.xnxx.com/?k=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 30 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]XNXX[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]2 of 11[/COLOR]' )
    try :
     xnxx . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "https://xhamster.com/search.php?from=&new=&q=" + o0o00OO0 . lower ( ) + "&qcat=video"
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 45 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Xhamster[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]3 of 11[/COLOR]' )
    try :
     xhamster . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://www.pornhd.com/search?search=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 60 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornHD[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]4 of 11[/COLOR]' )
    try :
     pornhd . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://www.porn.com/videos/search?q=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 75 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn.com[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]5 of 11[/COLOR]' )
    try :
     porncom . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://www.redtube.com/?search=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 90 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]RedTube[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]6 of 11[/COLOR]' )
    try :
     redtube . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://pornfun.com/search/?q=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 95 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornFun[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]7 of 11[/COLOR]' )
    try :
     pornfun . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://spankbang.com/s/" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 97 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Spankbang[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]8 of 11[/COLOR]' )
    try :
     spankbang . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://www.porn00.org/?s=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 99 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn00[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]9 of 11[/COLOR]' )
    try :
     porn00 . GET_CONTENT ( 'none' , iIiIIIi , 'none' )
    except : pass
    iIiIIIi = "http://virtualpornstars.com/?s=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Virtual Porn Stars[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]9 of 11[/COLOR]' )
    try :
     virtualpornstars . GET_CONTENT ( iIiIIIi )
    except : pass
    iIiIIIi = "http://watchxxxfree.com/?s=" + o0o00OO0 . lower ( )
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Watch XXX Free[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]10 of 11[/COLOR]' )
    try :
     watchxxxfree . GET_CONTENT ( iIiIIIi )
    except : pass
    o0o00OO0 = o0o00OO0 . replace ( '+' , '%20' )
    iIiIIIi = "http://www.perfectgirls.net/search/" + o0o00OO0 . lower ( ) + '/'
    iIiIIIi = 'split|' + iIiIIIi
    Ii1IIii11 . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Perfect Girls[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + oo00O00oO . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]11 of 11[/COLOR]' )
    try :
     perfectgirls . GET_CONTENT ( iIiIIIi )
    except : pass
    Ii1IIii11 . close ( )
   except :
    OOo . ok ( Oo0Ooo , '[COLOR pink]Sorry, there was an error searching for ' + o0o00OO0 . lower ( ) + ' please try again later.[/COLOR]' )
    quit ( )
  else : quit ( )
  if 93 - 93: OooooooO
 i11i1I1 = common . GET_KODI_VERSION ( )
 if 10 - 10: oOOO00o
 if i11i1I1 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 elif i11i1I1 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 82 - 82: Ooooo0Oo00oO0 - ooO0oo0oO0 / oo0Oo00Oo0 + ooooooO0oo
def OOOOoOoo0O0O0 ( ) :
 if 85 - 85: Ooo % i11iIiiIii - OooooooO * i111I / i1IIi11111i % i1IIi11111i
 IIiIi1iI = 0
 if not os . path . exists ( oOoOo00oOo ) :
  IIiIi1iI = 1
  common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
 else :
  oo000OO00Oo = open ( oOoOo00oOo , "r" )
  O0OOO0OOoO0O = re . compile ( r'<password>(.+?)</password>' )
  for O00Oo000ooO0 in oo000OO00Oo :
   file = O0OOO0OOoO0O . findall ( O00Oo000ooO0 )
   for OoO0O00 in file :
    IIiII = base64 . b64decode ( OoO0O00 )
    IIiIi1iI = 1
    common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR lime]ON[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR white]Current Password - [/COLOR][COLOR orangered]" + str ( IIiII ) + "[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR lime]Change Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR orangered]Disable Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
    if 35 - 35: ooooooO0oo % oooO0oo0oOOOO - oooO0oo0oOOOO
 if IIiIi1iI == 0 :
  common . addLink ( "[COLOR rose]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
  if 16 - 16: i1111 % OOO0O - i1111 + ooooooO0oo
def i1I1i ( ) :
 if 40 - 40: i1IIi11111i . ooO0oo0oO0 / i1IIi11111i / i11iIiiIii
 o0O00o = plugintools . get_setting ( "history_setting" )
 if 87 - 87: i11iIiiIii
 if o0O00o == "true" :
  common . addLink ( '[COLOR deeppink]Clear History[/COLOR]' , iiI1iIiI , 104 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR orangered]Disable History[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '###########################################' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
  if 93 - 93: Ooooo0Oo00oO0 - oo % i11iIiiIii . OooooooO / OooooooO - oOoOooOo0o0
  O000oo0O = open ( IIiiIiI1 , mode = 'r' ) ; OOOOi11i1 = O000oo0O . read ( ) ; O000oo0O . close ( )
  OOOOi11i1 = OOOOi11i1 . replace ( '\n' , '' )
  O0o0O00Oo0o0 = re . compile ( '<item>(.+?)</item>' ) . findall ( OOOOi11i1 )
  for O00O0oOO00O00 in O0o0O00Oo0o0 :
   IIII = re . compile ( '<date>(.+?)</date>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
   time = re . compile ( '<time>(.+?)</time>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
   iiIiI = re . compile ( '<name>(.+?)</name>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
   iIiIIIi = re . compile ( '<link>(.+?)</link>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
   o00oooO0Oo = re . compile ( '<site>(.+?)</site>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
   o0O0OOO0Ooo = re . compile ( '<icon>(.+?)</icon>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
   iIiIIIi = iiIiI + '|SPLIT|' + iIiIIIi + '|SPLIT|' + o00oooO0Oo + '|SPLIT|' + o0O0OOO0Ooo + '|SPLIT|' + iIiIIIi
   if 45 - 45: oooO0oo0oOOOO / oo0ooO0oOOOOo
   common . addLink ( '[COLOR pink]' + IIII + ' | ' + '[/COLOR][COLOR deeppink]' + time + '[/COLOR] - [COLOR orangered]' + o00oooO0Oo + '[/COLOR][COLOR pink] - ' + iiIiI + '[/COLOR]' , iIiIIIi , 800 , o0O0OOO0Ooo , O0O0OO0O0O0 )
 else :
  common . addLink ( '[COLOR orangered]Enable History Monitoring[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '############################################' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR pink]History monitoring is currently disabled.[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  if 32 - 32: OooooooO . Oo0O0OOOoo . Oo0O0OOOoo
def OO00O0O ( ) :
 if 33 - 33: oooO0oo0oOOOO . Oo0O0OOOoo . i1IIi11111i
 common . addLink ( '[COLOR deeppink]Your Favourites[/COLOR]' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 if 72 - 72: II1Ii1iI1i / oo + i111I - I11i1i11i1I
 O000oo0O = open ( iiIiIIi , mode = 'r' ) ; OOOOi11i1 = O000oo0O . read ( ) ; O000oo0O . close ( )
 OOOOi11i1 = OOOOi11i1 . replace ( '\n' , '' )
 O0o0O00Oo0o0 = re . compile ( '<item>(.+?)</item>' ) . findall ( OOOOi11i1 )
 for O00O0oOO00O00 in O0o0O00Oo0o0 :
  iiIiI = re . compile ( '<name>(.+?)</name>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
  iIiIIIi = re . compile ( '<link>(.+?)</link>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
  o00oooO0Oo = re . compile ( '<site>(.+?)</site>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
  o0O0OOO0Ooo = re . compile ( '<icon>(.+?)</icon>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
  iIiIIIi = iiIiI + '|SPLIT|' + iIiIIIi + '|SPLIT|' + o00oooO0Oo + '|SPLIT|' + o0O0OOO0Ooo + '|SPLIT|' + iIiIIIi
  common . addLink ( '[COLOR orangered]' + o00oooO0Oo + '[/COLOR][COLOR pink] - ' + iiIiI + '[/COLOR]' , iIiIIIi , 103 , o0O0OOO0Ooo , O0O0OO0O0O0 )
  if 29 - 29: Ooooo0Oo00oO0 + Ooo % oooO0oo0oOOOO
def I1I11 ( name , url , iconimage ) :
 if 34 - 34: i1IIi11111i . oo0Oo00Oo0 * Ooooo0Oo00oO0 + oOoOooOo0o0
 i11111IIIII = url
 oO00O0O0O , i1ii1iiI , iIiii1i111iI1 , i11 , url = url . split ( '|SPLIT|' )
 if 81 - 81: oo
 o0o00OO0 = '\n<item>\n<name>' + oO00O0O0O + '</name>\n<link>' + i1ii1iiI + '</link>\n<site>' + iIiii1i111iI1 + '</site>\n<icon>' + i11 + '</icon>\n</item>\n'
 if 42 - 42: oo / oOOO00o / oo0ooO0oOOOOo + OooooooO / OOO0O
 IIIii1II1II = OOo . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Remove from Favourites[/B][/COLOR]' ] )
 if 84 - 84: O0ooOooooO * i1111 + I11i1i11i1I
 if IIIii1II1II == 0 :
  O0ooO0Oo00o ( name , i11111IIIII , iconimage )
 else :
  ooO0oOOooOo0 = open ( iiIiIIi ) . read ( )
  O000oo0O = ooO0oOOooOo0 . replace ( o0o00OO0 , '\n' )
  i1I1ii11i1Iii = open ( iiIiIIi , mode = 'w' )
  i1I1ii11i1Iii . write ( str ( O000oo0O ) )
  i1I1ii11i1Iii . close ( )
  xbmc . executebuiltin ( "Container.Refresh" )
  quit ( )
  if 26 - 26: oOOO00o - ooO0oo0oO0 - i1IIi11111i / oo . OOO0O % ooO0oo0oO0
def OO ( name , url , iconimage ) :
 if 25 - 25: oo
 i11111IIIII = url
 oO00O0O0O , i1ii1iiI , iIiii1i111iI1 , i11 , url = url . split ( '|SPLIT|' )
 if 62 - 62: oo0Oo00Oo0 + oooO0oo0oOOOO
 IIIii1II1II = OOo . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Delete Download[/B][/COLOR]' ] )
 if 98 - 98: oo0ooO0oOOOOo
 if IIIii1II1II == 0 :
  O0ooO0Oo00o ( name , i11111IIIII , iconimage )
 else :
  os . remove ( url )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 51 - 51: I11i1i11i1I - Ooo + i1111 * ooooooO0oo . oOOO00o + Ooo
def OoO0o ( ) :
 if 78 - 78: Ooo % oooO0oo0oOOOO % ooooooO0oo
 if os . path . isfile ( IIiiIiI1 ) :
  IIIii1II1II = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Would you like to clear all stored history?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[B][COLOR orangered]NO[/COLOR][/B]' )
  if IIIii1II1II == 1 :
   os . remove ( IIiiIiI1 )
   O000oo0O = open ( IIiiIiI1 , 'w' )
   O000oo0O . write ( '#START OF FILE#' )
   O000oo0O . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 46 - 46: i111I . i11iIiiIii
def OOo0oO00ooO00 ( ) :
 if 90 - 90: OOO0O * oOoOooOo0o0 + oo0ooO0oOOOOo
 IIi = plugintools . get_setting ( "download_location" )
 OOOoOoO = xbmc . translatePath ( IIi )
 common . addLink ( '[COLOR deeppink]Download Location: [/COLOR]' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( OOOoOoO , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '[COLOR orangered]Change Download Location[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 if 43 - 43: i11iIiiIii + I11i1i11i1I * i1111 * oOoOooOo0o0 * oooO0oo0oOOOO
 o00oO0oo0OO = [ '.mp4' ]
 if 57 - 57: oOoOooOo0o0 % ooooooO0oo + oo0ooO0oOOOOo - I11i1i11i1I
 for file in os . listdir ( OOOoOoO ) :
  for o0OIiI1i in o00oO0oo0OO :
   if file . endswith ( o0OIiI1i ) :
    o0O0OOO0Ooo = iiiii
    O000oo0O = open ( ooOoo0O , mode = 'r' ) ; OOOOi11i1 = O000oo0O . read ( ) ; O000oo0O . close ( )
    OOOOi11i1 = OOOOi11i1 . replace ( '\n' , '' )
    O0o0O00Oo0o0 = re . compile ( '<item>(.+?)</item>' ) . findall ( OOOOi11i1 )
    for O00O0oOO00O00 in O0o0O00Oo0o0 :
     iiIiI = re . compile ( '<name>(.+?)</name>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
     o0Oo00 = re . compile ( '<icon>(.+?)</icon>' ) . findall ( O00O0oOO00O00 ) [ 0 ]
     if file in iiIiI :
      o0O0OOO0Ooo = o0Oo00
    iIiIIIi = xbmc . translatePath ( os . path . join ( OOOoOoO , file ) )
    if "http" in o0O0OOO0Ooo :
     iI = file + '|SPLIT|' + iIiIIIi + '|SPLIT|Downloaded|SPLIT|' + o0O0OOO0Ooo + '|SPLIT|' + iIiIIIi
    else :
     iI = file + '|SPLIT|' + iIiIIIi + '|SPLIT|Downloaded|SPLIT|None|SPLIT|' + iIiIIIi
    common . addLink ( '[COLOR pink]' + file + '[/COLOR]' , iI , 107 , o0O0OOO0Ooo , O0O0OO0O0O0 )
    if 90 - 90: oOoOooOo0o0 % ooooooO0oo - ooO0oo0oO0 - ooO0oo0oO0 / i11iIiiIii % Ooooo0Oo00oO0
def IIii11I1 ( ) :
 if 83 - 83: O0ooOooooO
 IIi = plugintools . get_setting ( "download_location" )
 oO00Oo0O0o = OOo . browse ( 3 , Oo0Ooo , 'files' , '' , False , False , oO000OoOoo00o )
 ooO0oOOooOo0 = open ( iiiI11 ) . read ( )
 O000oo0O = ooO0oOOooOo0 . replace ( IIi , oO00Oo0O0o )
 i1I1ii11i1Iii = open ( iiiI11 , mode = 'w' )
 i1I1ii11i1Iii . write ( str ( O000oo0O ) )
 i1I1ii11i1Iii . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 13 - 13: i111I
def I111iI ( name , url , iconimage ) :
 if 56 - 56: i1IIi11111i
 oO00O0O0O , i1ii1iiI , iIiii1i111iI1 , i11 , url = url . split ( '|SPLIT|' )
 name = oO00O0O0O
 O0oO = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 OO0ooOOO0OOO = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 o0o00OO0 = '\n<item>\n<date>' + O0oO + '</date>\n<time>' + OO0ooOOO0OOO + '</time>\n<name>' + oO00O0O0O + '</name>\n<link>' + i1ii1iiI + '</link>\n<site>' + iIiii1i111iI1 + '</site>\n<icon>' + i11 + '</icon>\n</item>\n'
 oO00O0O0O = open ( IIiiIiI1 ) . read ( )
 i1ii1iiI = oO00O0O0O . replace ( '#START OF FILE#' , '#START OF FILE#' + o0o00OO0 )
 O000oo0O = open ( IIiiIiI1 , mode = 'w' )
 O000oo0O . write ( str ( i1ii1iiI ) )
 O000oo0O . close ( )
 if 63 - 63: OOO0O * OooooooO
 if iconimage == "None" :
  iconimage = iiiii
 ooiIi1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , ooiIi1 , False )
 if 74 - 74: ooO0oo0oO0 * Ooooo0Oo00oO0 + OOO0O / II1Ii1iI1i / i1111 . I11i1i11i1I
def O0ooO0Oo00o ( name , url , iconimage ) :
 if 62 - 62: i111I * i1IIi11111i
 oO00O0O0O , i1ii1iiI , iIiii1i111iI1 , i11 , url = url . split ( '|SPLIT|' )
 name = oO00O0O0O
 O0oO = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 OO0ooOOO0OOO = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 o0o00OO0 = '\n<item>\n<date>' + O0oO + '</date>\n<time>' + OO0ooOOO0OOO + '</time>\n<name>' + oO00O0O0O + '</name>\n<link>' + i1ii1iiI + '</link>\n<site>' + iIiii1i111iI1 + '</site>\n<icon>' + i11 + '</icon>\n</item>\n'
 oO00O0O0O = open ( IIiiIiI1 ) . read ( )
 i1ii1iiI = oO00O0O0O . replace ( '#START OF FILE#' , '#START OF FILE#' + o0o00OO0 )
 O000oo0O = open ( IIiiIiI1 , mode = 'w' )
 O000oo0O . write ( str ( i1ii1iiI ) )
 O000oo0O . close ( )
 if 58 - 58: OOO0O % oo0ooO0oOOOOo
 if iconimage == "None" :
  iconimage = iiiii
  if 50 - 50: oOoOooOo0o0 . oo0ooO0oOOOOo
 if "highwebmedia" in url :
  OOo . ok ( Oo0Ooo , '[COLOR pink]Chaturbate links are taken at the time of broadcasting. If this broadcast has ended the link will no longer play. [/COLOR]' )
 ooiIi1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , ooiIi1 , False )
 if 97 - 97: oooO0oo0oOOOO + OOO0O
def OO0O000 ( name , url , iconimage ) :
 if 37 - 37: i111I - oooO0oo0oOOOO - oo0ooO0oOOOOo
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   if 77 - 77: oo0Oo00Oo0 * ooO0oo0oO0
 ooiIi1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , ooiIi1 , False )
 if 98 - 98: i1IIi11111i % ooooooO0oo * i111I
def o0O0o0Oo ( ) :
 if 51 - 51: ooO0oo0oO0 . OOO0O / Ooo + oo0ooO0oOOOOo
 Ii11iII1 = common . _get_keyboard ( heading = "Please Set Password" )
 if ( not Ii11iII1 ) :
  OOo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 Oo0O0O0ooO0O = Ii11iII1
 if 33 - 33: O0ooOooooO . i1111 % OooooooO + oo0ooO0oOOOOo
 Ii11iII1 = common . _get_keyboard ( heading = "Please Confirm Your Password" )
 if ( not Ii11iII1 ) :
  OOo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 oO00O000oO0 = Ii11iII1
 if 79 - 79: oOOO00o - i111I - Ooo - ooO0oo0oO0 * oo0Oo00Oo0
 if not os . path . exists ( oOoOo00oOo ) :
  if not os . path . exists ( OOooO ) :
   os . makedirs ( OOooO )
  open ( oOoOo00oOo , 'w' )
  if 4 - 4: i11iIiiIii . i111I / oo % oOoOooOo0o0 % oOOO00o * oooO0oo0oOOOO
  if Oo0O0O0ooO0O == oO00O000oO0 :
   iIIii = base64 . b64encode ( Oo0O0O0ooO0O )
   O000oo0O = open ( oOoOo00oOo , 'w' )
   O000oo0O . write ( '<password>' + str ( iIIii ) + '</password>' )
   O000oo0O . close ( )
   OOo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   OOo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
 else :
  os . remove ( oOoOo00oOo )
  if 92 - 92: ooooooO0oo + Ooo % oo0Oo00Oo0
  if Oo0O0O0ooO0O == oO00O000oO0 :
   iIIii = base64 . b64encode ( Oo0O0O0ooO0O )
   O000oo0O = open ( oOoOo00oOo , 'w' )
   O000oo0O . write ( '<password>' + str ( iIIii ) + '</password>' )
   O000oo0O . close ( )
   OOo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   OOo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
   if 62 - 62: Ooooo0Oo00oO0 / II1Ii1iI1i
def oo0oO ( ) :
 if 94 - 94: ooO0oo0oO0 / I11i1i11i1I % OooooooO * OooooooO * i1111
 try :
  os . remove ( oOoOo00oOo )
  OOo . ok ( Oo0Ooo , 'Parental controls have been disabled.' )
  xbmc . executebuiltin ( "Container.Refresh" )
 except :
  OOo . ok ( Oo0Ooo , 'There was an error disabling the parental controls.' )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 29 - 29: oo + OOO0O / oo0ooO0oOOOOo / oo0Oo00Oo0 * ooO0oo0oO0
def O0OO ( ) :
 if 6 - 6: ooO0oo0oO0 % i11iIiiIii % Ooooo0Oo00oO0
 o0Oo0oO0oOO00 = 0
 if 92 - 92: i111I * oOoOooOo0o0
 try :
  common . open_url ( "http://www.google.com" )
 except :
  OOo . ok ( Oo0Ooo , '[COLOR orangered]Error: It appears you do not currently have an active internet connection. This will cause false positives in the test. Please try again with an active internet connection.[/COLOR]' )
  return
  if 100 - 100: oOoOooOo0o0 + oOoOooOo0o0 * Oo0O0OOOoo
 Ii1IIii11 . create ( Oo0Ooo , "Checking for repository updates" , '' , 'Please Wait...' )
 Ii1IIii11 . update ( 0 )
 oO00O0O0O = open ( Ii1iIIIi1ii ) . read ( )
 i1ii1iiI = oO00O0O0O . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0o0O00Oo0o0 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( i1ii1iiI ) )
 for O00O0oOO00O00 in O0o0O00Oo0o0 :
  Ii1IIii11 . update ( 25 )
  I1i = float ( O00O0oOO00O00 ) + 0.01
  iIiIIIi = o0oO + str ( I1i ) + '.zip'
  try :
   O00Oooo = common . open_url ( iIiIIIi )
   if "Not Found" not in O00Oooo :
    IIiIi1iI = 1
    Ii1IIii11 . update ( 75 )
    i11I = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( i11I ) :
     os . makedirs ( i11I )
    o00Oo0oooooo = os . path . join ( i11I , 'repoupdate.zip' )
    try : os . remove ( o00Oo0oooooo )
    except : pass
    Ii1IIii11 . update ( 100 )
    Ii1IIii11 . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( iIiIIIi , o00Oo0oooooo , Ii1IIii11 )
    O0oO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    Ii1IIii11 . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( o00Oo0oooooo , O0oO0 , Ii1IIii11 )
    try : os . remove ( o00Oo0oooooo )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    o0Oo0oO0oOO00 = 1
    OOo . ok ( Oo0Ooo , "ECHO XXX repository was updated to " + str ( I1i ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 7 - 7: i1IIi11111i
 Ii1IIii11 . update ( 75 , "Checking for addon updates" )
 oO00O0O0O = open ( O0O00o0OOO0 ) . read ( )
 i1ii1iiI = oO00O0O0O . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0o0O00Oo0o0 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( i1ii1iiI ) )
 for O00O0oOO00O00 in O0o0O00Oo0o0 :
  I1i = float ( O00O0oOO00O00 ) + 0.01
  iIiIIIi = o0oo0o0O00OO + str ( I1i ) + '.zip'
  try :
   O00Oooo = common . open_url ( iIiIIIi )
   if "Not Found" not in O00Oooo :
    IIiIi1iI = 1
    Ii1IIii11 . update ( 75 )
    i11I = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( i11I ) :
     os . makedirs ( i11I )
    o00Oo0oooooo = os . path . join ( i11I , 'xxx_o_dus_update.zip' )
    try : os . remove ( o00Oo0oooooo )
    except : pass
    Ii1IIii11 . update ( 100 )
    Ii1IIii11 . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( iIiIIIi , o00Oo0oooooo , Ii1IIii11 )
    O0oO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    Ii1IIii11 . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( o00Oo0oooooo , O0oO0 , Ii1IIii11 )
    try : os . remove ( o00Oo0oooooo )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    Ii1IIii11 . update ( 100 )
    Ii1IIii11 . close
    o0Oo0oO0oOO00 = 1
    OOo . ok ( Oo0Ooo , "XXX-O-DUS was updated to " + str ( I1i ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 41 - 41: oOOO00o * ooO0oo0oO0 / i1111 * Ooo
 if Ii1IIii11 . iscanceled ( ) :
  Ii1IIii11 . close ( )
  if 22 - 22: i111I
 return o0Oo0oO0oOO00
 if 75 - 75: oo0ooO0oOOOOo + oo0ooO0oOOOOo + II1Ii1iI1i - II1Ii1iI1i
def OOooOOOooO ( url ) :
 if 12 - 12: oooO0oo0oOOOO - oo0ooO0oOOOOo
 O000oo0O = open ( url , mode = 'r' ) ; OOOOi11i1 = O000oo0O . read ( ) ; O000oo0O . close ( )
 common . TextBoxes ( "%s" % OOOOi11i1 )
 if 81 - 81: OOO0O - OOO0O . OooooooO
 if url == IiIIIiI1I1 :
  return
  if 73 - 73: oOOO00o % i11iIiiIii - i1IIi11111i
def Ii1iI111II1I1 ( ) :
 if 91 - 91: oo0Oo00Oo0 % oo0Oo00Oo0 - i1IIi11111i
 try :
  OOooOOOooO ( IiIIIiI1I1 )
  if 18 - 18: oOOO00o - i11iIiiIii / i1111 . oo0Oo00Oo0
  IIIii1II1II = xbmcgui . Dialog ( ) . yesno ( "[COLOR orangered][B]RESET XXX-O-DUS?[/B][/COLOR]" , '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]' , '' , yeslabel = '[COLOR green]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if IIIii1II1II == 1 :
   IIi = plugintools . get_setting ( "download_location" )
   OOOoOoO = xbmc . translatePath ( IIi )
   if 55 - 55: II1Ii1iI1i % i1111 + oOOO00o * ooO0oo0oO0
   o00oO0oo0OO = [ '.mp4' ]
   if 81 - 81: Oo0O0OOOoo % II1Ii1iI1i . ooO0oo0oO0
   for file in os . listdir ( OOOoOoO ) :
    for o0OIiI1i in o00oO0oo0OO :
     if file . endswith ( o0OIiI1i ) :
      try :
       i11I = xbmc . translatePath ( os . path . join ( OOOoOoO , file ) )
       os . remove ( i11I )
      except :
       OOo . ok ( Oo0Ooo , "[COLOR white]There was an error deleting " + file + "[/COLOR]" )
       pass
   try :
    shutil . rmtree ( OOoO00o )
   except :
    OOo . ok ( Oo0Ooo , "[COLOR white]There was an error deleting deleting the data directory.[/COLOR]" )
    pass
   OOo . ok ( Oo0Ooo , "[COLOR white]XXX-O-DUS has been reset to the factory state.[/COLOR]" , "[COLOR white]Press OK to continue.[/COLOR]" )
   xbmc . executebuiltin ( "Container.Refresh" )
 except :
  OOo . ok ( Oo0Ooo , "[COLOR white]Sorry, something went wrong.[/COLOR]" , "[COLOR white]Please report this issue to @EchoCoder on Twitter.[/COLOR]" )
  quit ( )
  if 4 - 4: i11iIiiIii % oo % II1Ii1iI1i / Oo0O0OOOoo
def I11iI ( ) :
 ooOoo = [ ]
 I1III1111iIi = sys . argv [ 2 ]
 if len ( I1III1111iIi ) >= 2 :
  I1i111I = sys . argv [ 2 ]
  OooOo0oo0O0o00O = I1i111I . replace ( '?' , '' )
  if ( I1i111I [ len ( I1i111I ) - 1 ] == '/' ) :
   I1i111I = I1i111I [ 0 : len ( I1i111I ) - 2 ]
  I1i11 = OooOo0oo0O0o00O . split ( '&' )
  ooOoo = { }
  for IiIi1I1 in range ( len ( I1i11 ) ) :
   IiIIi1 = { }
   IiIIi1 = I1i11 [ IiIi1I1 ] . split ( '=' )
   if ( len ( IiIIi1 ) ) == 2 :
    ooOoo [ IiIIi1 [ 0 ] ] = IiIIi1 [ 1 ]
    if 47 - 47: I11i1i11i1I * Ooooo0Oo00oO0 + ooO0oo0oO0 / oOoOooOo0o0 / oo - i111I
 return ooOoo
 if 33 - 33: OOO0O * oo0Oo00Oo0 - i1111
I1i111I = I11iI ( ) ; OOo0o0O0O = None ; iIiIIIi = None ; o0 = None ; o0O0OOO0Ooo = None ; OO0o0oOOO0O = None
try : OOo0o0O0O = urllib . unquote_plus ( I1i111I [ "name" ] )
except : pass
try : iIiIIIi = urllib . unquote_plus ( I1i111I [ "url" ] )
except : pass
try : o0 = int ( I1i111I [ "mode" ] )
except : pass
try : o0O0OOO0Ooo = urllib . unquote_plus ( I1i111I [ "iconimage" ] )
except : pass
try : OO0o0oOOO0O = urllib . quote_plus ( I1i111I [ "fanartimage" ] )
except : pass
if 49 - 49: Ooooo0Oo00oO0 . oo0ooO0oOOOOo . i1111
if o0 == None or iIiIIIi == None or len ( iIiIIIi ) < 1 : OOOO ( )
elif o0 == 1 : menus . SEARCH ( )
elif o0 == 2 : menus . VIDEOS ( )
elif o0 == 3 : menus . LIVE ( )
elif o0 == 4 : menus . PICTURES ( )
elif o0 == 5 : menus . STORIES ( )
elif o0 == 6 : menus . ALL ( )
elif o0 == 10 : xhamster . MAIN_MENU ( )
elif o0 == 11 : xhamster . GET_CONTENT ( iIiIIIi )
elif o0 == 12 : xhamster . SEARCH ( )
elif o0 == 13 : xhamster . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 20 : chaturbate . MAIN_MENU ( )
elif o0 == 21 : chaturbate . GET_CONTENT ( iIiIIIi )
elif o0 == 22 : chaturbate . SEARCH ( )
elif o0 == 23 : chaturbate . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 30 : xnxx . MAIN_MENU ( )
elif o0 == 31 : xnxx . GET_CONTENT ( iIiIIIi )
elif o0 == 32 : xnxx . SEARCH ( )
elif o0 == 33 : xnxx . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 34 : xnxx . PICTURE_MENU ( )
elif o0 == 35 : xnxx . PICTURE_CONTENT ( iIiIIIi )
elif o0 == 36 : xnxx . SCRAPE_GALLERY ( iIiIIIi )
elif o0 == 37 : xnxx . DISPLAY_PICTURE ( iIiIIIi )
elif o0 == 38 : xnxx . STORY_MENU ( )
elif o0 == 39 : xnxx . LIST_STORIES ( iIiIIIi )
elif o0 == 40 : xnxx . DISPLAY_STORY ( iIiIIIi )
elif o0 == 41 : redtube . MAIN_MENU ( )
elif o0 == 42 : redtube . GET_CONTENT ( iIiIIIi )
elif o0 == 43 : redtube . SEARCH ( )
elif o0 == 44 : redtube . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 50 : pornhd . MAIN_MENU ( )
elif o0 == 51 : pornhd . GET_CONTENT ( iIiIIIi )
elif o0 == 52 : pornhd . SEARCH ( )
elif o0 == 53 : pornhd . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 60 : porncom . MAIN_MENU ( )
elif o0 == 61 : porncom . GET_CONTENT ( iIiIIIi )
elif o0 == 62 : porncom . SEARCH ( )
elif o0 == 63 : porncom . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 70 : youporn . MAIN_MENU ( )
elif o0 == 71 : youporn . GET_CONTENT ( iIiIIIi )
elif o0 == 72 : youporn . SEARCH ( )
elif o0 == 73 : youporn . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 80 : pornfun . MAIN_MENU ( )
elif o0 == 81 : pornfun . GET_CONTENT ( iIiIIIi )
elif o0 == 82 : pornfun . SEARCH ( )
elif o0 == 83 : pornfun . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 90 : motherless . MAIN_MENU ( )
elif o0 == 91 : motherless . GET_CONTENT ( iIiIIIi )
elif o0 == 92 : motherless . DISPLAY_PICTURE ( iIiIIIi )
elif o0 == 300 : watchxxxfree . MAIN_MENU ( )
elif o0 == 301 : watchxxxfree . GET_CONTENT ( iIiIIIi )
elif o0 == 302 : watchxxxfree . SEARCH ( )
elif o0 == 303 : watchxxxfree . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 310 : perfectgirls . MAIN_MENU ( )
elif o0 == 311 : perfectgirls . GET_CONTENT ( iIiIIIi )
elif o0 == 312 : perfectgirls . SEARCH ( )
elif o0 == 313 : perfectgirls . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 100 : iii1i1iiiiIi ( ) ;
elif o0 == 101 : i1I1i ( )
elif o0 == 102 : OO00O0O ( )
elif o0 == 103 : I1I11 ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 104 : OoO0o ( )
elif o0 == 105 : OOo0oO00ooO00 ( )
elif o0 == 106 : plugintools . open_settings_dialog ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
elif o0 == 107 : OO ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 200 : spankbang . MAIN_MENU ( )
elif o0 == 201 : spankbang . SUB_MENU ( iIiIIIi )
elif o0 == 202 : spankbang . GET_CONTENT ( iIiIIIi )
elif o0 == 203 : spankbang . SEARCH ( )
elif o0 == 204 : spankbang . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 210 : porn00 . MAIN_MENU ( )
elif o0 == 211 : porn00 . GET_CONTENT ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 212 : porn00 . SEARCH ( )
elif o0 == 213 : porn00 . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 220 : virtualpornstars . MAIN_MENU ( )
elif o0 == 221 : virtualpornstars . GET_CONTENT ( iIiIIIi )
elif o0 == 222 : virtualpornstars . SEARCH ( )
elif o0 == 223 : virtualpornstars . PLAY_URL ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 800 : O0ooO0Oo00o ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 900 : OOOOoOoo0O0O0 ( )
elif o0 == 901 : o0O0o0Oo ( )
elif o0 == 902 : oo0oO ( )
elif o0 == 995 : common . GET_M3U_LIST ( iIiIIIi )
elif o0 == 996 : OO0O000 ( OOo0o0O0O , iIiIIIi , o0O0OOO0Ooo )
elif o0 == 997 : Ii1iI111II1I1 ( )
elif o0 == 998 : OOooOOOooO ( iIiIIIi )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , shutil
import base64 , time , datetime
from resources . lib . modules import plugintools
from resources . lib . modules import menus
from resources . lib . modules import common
from resources . lib . modules import checker
from resources . lib . modules import cache
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
cache . check ( )
if 61 - 61: o00oOO0 / II1Ii1iI1i * oo0Oo00Oo0 / i111I . oooO0oo0oOOOO
def iii11I111 ( ) :
 if 63 - 63: oo * Ooo - OooooooO * oooO0oo0oOOOO
 iIii111IIi = OooO0 + '|SPLIT|' + iiiIi
 checker . check ( iIii111IIi )
 if 4 - 4: i1111 / o00oOO0 . OooooooO
 if not os . path . exists ( OoO000 ) :
  O0oo0OO0oOOOo = open ( Ooo00O00O0O0O , mode = 'r' ) ; i1i1i11IIi = O0oo0OO0oOOOo . read ( ) ; O0oo0OO0oOOOo . close ( )
  common . TextBoxes ( "%s" % i1i1i11IIi )
  II1III = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Do you agree to the terms and conditions of this addon?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if II1III == 1 :
   O0oo0OO0oOOOo = open ( OooO0OO , mode = 'r' ) ; i1i1i11IIi = O0oo0OO0oOOOo . read ( ) ; O0oo0OO0oOOOo . close ( )
   common . TextBoxes ( "%s" % i1i1i11IIi )
   OOo . ok ( Oo0Ooo , "[COLOR pink]We can see this is the first time you have used XXX-O-DUS. The next prompt is important as it will allow you to enable the history section of the addon and it will also allow you to select the location you would like to be used to download videos.[/COLOR]" )
   plugintools . open_settings_dialog ( )
   open ( OoO000 , 'w' )
  else :
   sys . exit ( 0 )
   if 19 - 19: Ooo % II1Ii1iI1i % oo0ooO0oOOOOo
 if not os . path . exists ( OOooO ) :
  II1III = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , "[COLOR white]Would you like to enable the parental controls now?[/COLOR]" , "" , yeslabel = '[COLOR orangered]NO[/COLOR]' , nolabel = '[COLOR lime]YES[/COLOR]' )
  if II1III == 0 :
   oo0OooOOo0 ( )
  else :
   os . makedirs ( OOooO )
   if 92 - 92: OooooooO . oOOO00o + oo0ooO0oOOOOo
 elif os . path . exists ( oOoOo00oOo ) :
  IiII1I11i1I1I = common . _get_keyboard ( heading = "Please Enter Your Password" )
  if ( not IiII1I11i1I1I ) :
   OOo . ok ( Oo0Ooo , "Sorry, no password was entered." )
   sys . exit ( 0 )
  oO0Oo = IiII1I11i1I1I
  if 54 - 54: oo0ooO0oOOOOo - i1IIi11111i + i111I
  O0o0 = open ( oOoOo00oOo , "r" )
  OO00Oo = re . compile ( r'<password>(.+?)</password>' )
  for O0OOO0OOoO0O in O0o0 :
   file = OO00Oo . findall ( O0OOO0OOoO0O )
   for O00Oo000ooO0 in file :
    OoO0O00 = base64 . b64decode ( O00Oo000ooO0 )
    if not OoO0O00 == oO0Oo :
     if not O00Oo000ooO0 == oO0Oo :
      OOo . ok ( Oo0Ooo , "Sorry, the password you entered was incorrect." )
      sys . exit ( 0 )
      if 5 - 5: I11i1i11i1I / oo0ooO0oOOOOo . ooooooO0oo - oooO0oo0oOOOO / Oo0O0OOOoo
 ooOooo000oOO = plugintools . get_setting ( "download_location" )
 Oo0oOOo = xbmc . translatePath ( ooOooo000oOO )
 if not os . path . exists ( Oo0oOOo ) :
  os . makedirs ( Oo0oOOo )
  if 58 - 58: i1111 * oo0Oo00Oo0 * Ooooo0Oo00oO0 / oo0Oo00Oo0
 if not os . path . isfile ( IIiiIiI1 ) :
  O0oo0OO0oOOOo = open ( IIiiIiI1 , 'w' )
  O0oo0OO0oOOOo . write ( '#START OF FILE#' )
  O0oo0OO0oOOOo . close ( )
 if not os . path . isfile ( iiIiIIi ) :
  O0oo0OO0oOOOo = open ( iiIiIIi , 'w' )
  O0oo0OO0oOOOo . write ( '#START OF FILE#' )
  O0oo0OO0oOOOo . close ( )
 if not os . path . isfile ( ooOoo0O ) :
  O0oo0OO0oOOOo = open ( ooOoo0O , 'w' )
  O0oo0OO0oOOOo . write ( '#START OF FILE#' )
  O0oo0OO0oOOOo . close ( )
  if 75 - 75: Ooo
 I1III = open ( O0O00o0OOO0 ) . read ( )
 OO0O0OoOO0 = I1III . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 iiiI1I11i1 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO0O0OoOO0 ) )
 for IIi1i11111 in iiiI1I11i1 :
  ooOO00O00oo = float ( IIi1i11111 )
 I1III = open ( Ii1iIIIi1ii ) . read ( )
 OO0O0OoOO0 = I1III . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 iiiI1I11i1 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO0O0OoOO0 ) )
 for IIi1i11111 in iiiI1I11i1 :
  I1ii11iI = float ( IIi1i11111 )
  if 14 - 14: OOO0O / Oo0O0OOOoo . OOO0O . oOOO00o % oo * oOOO00o
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
 if 16 - 16: OOO0O . o00oOO0 + i11iIiiIii
 if not os . path . exists ( oOoOo00oOo ) :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR orangered]OFF[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 else :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR lime]ON[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]#####################################[/COLOR]" , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR pink]Twitter Support: [/COLOR][COLOR white]@EchoCoder[/COLOR]" , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Disclaimer[/COLOR]" , Ooo00O00O0O0O , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Addon Information[/COLOR]" , OooO0OO , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR orangered]RESET XXX-O-DUS[/COLOR]" , 'url' , 997 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Addon Version:[/COLOR] [COLOR white]" + str ( ooOO00O00oo ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Repository Version:[/COLOR] [COLOR white]" + str ( I1ii11iI ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 if 38 - 38: Oo0O0OOOoo * oo0Oo00Oo0 . oo0ooO0oOOOOo
 ooo0OOO0 = common . GET_KODI_VERSION ( )
 if 25 - 25: Ooooo0Oo00oO0
 if ooo0OOO0 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif ooo0OOO0 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 7 - 7: II1Ii1iI1i / i1IIi11111i * oOoOooOo0o0 . Oo0O0OOOoo . ooO0oo0oO0
def iIii ( ) :
 if 79 - 79: i111I / oooO0oo0oOOOO
 OO0OoO0o00 = ''
 ooOO0O0ooOooO = xbmc . Keyboard ( OO0OoO0o00 , 'Enter Search Term' )
 ooOO0O0ooOooO . doModal ( )
 if ooOO0O0ooOooO . isConfirmed ( ) :
  oOOOo00O00oOo = ooOO0O0ooOooO . getText ( )
  iiIIIi = oOOOo00O00oOo
  OO0OoO0o00 = oOOOo00O00oOo . replace ( ' ' , '+' )
  if len ( OO0OoO0o00 ) > 1 :
   try :
    Ii1IIii11 . create ( Oo0Ooo , '[COLOR white]Searching: [/COLOR] [COLOR orangered]YouPorn[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]1 of 11[/COLOR]' )
    ooo00OOOooO = "http://www.youporn.com/search/?query=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 15 )
    try :
     youporn . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://www.xnxx.com/?k=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 30 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]XNXX[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]2 of 11[/COLOR]' )
    try :
     xnxx . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "https://xhamster.com/search.php?from=&new=&q=" + OO0OoO0o00 . lower ( ) + "&qcat=video"
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 45 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Xhamster[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]3 of 11[/COLOR]' )
    try :
     xhamster . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://www.pornhd.com/search?search=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 60 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornHD[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]4 of 11[/COLOR]' )
    try :
     pornhd . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://www.porn.com/videos/search?q=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 75 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn.com[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]5 of 11[/COLOR]' )
    try :
     porncom . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://www.redtube.com/?search=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 90 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]RedTube[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]6 of 11[/COLOR]' )
    try :
     redtube . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://pornfun.com/search/?q=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 95 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornFun[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]7 of 11[/COLOR]' )
    try :
     pornfun . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://spankbang.com/s/" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 97 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Spankbang[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]8 of 11[/COLOR]' )
    try :
     spankbang . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://www.porn00.org/?s=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 99 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn00[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]9 of 11[/COLOR]' )
    try :
     porn00 . GET_CONTENT ( 'none' , ooo00OOOooO , 'none' )
    except : pass
    ooo00OOOooO = "http://virtualpornstars.com/?s=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Virtual Porn Stars[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]9 of 11[/COLOR]' )
    try :
     virtualpornstars . GET_CONTENT ( ooo00OOOooO )
    except : pass
    ooo00OOOooO = "http://watchxxxfree.com/?s=" + OO0OoO0o00 . lower ( )
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Watch XXX Free[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]10 of 11[/COLOR]' )
    try :
     watchxxxfree . GET_CONTENT ( ooo00OOOooO )
    except : pass
    OO0OoO0o00 = OO0OoO0o00 . replace ( '+' , '%20' )
    ooo00OOOooO = "http://www.perfectgirls.net/search/" + OO0OoO0o00 . lower ( ) + '/'
    ooo00OOOooO = 'split|' + ooo00OOOooO
    Ii1IIii11 . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Perfect Girls[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIIIi . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]11 of 11[/COLOR]' )
    try :
     perfectgirls . GET_CONTENT ( ooo00OOOooO )
    except : pass
    Ii1IIii11 . close ( )
   except :
    OOo . ok ( Oo0Ooo , '[COLOR pink]Sorry, there was an error searching for ' + OO0OoO0o00 . lower ( ) + ' please try again later.[/COLOR]' )
    quit ( )
  else : quit ( )
  if 67 - 67: oOOO00o * Ooo * Ooooo0Oo00oO0 + oo0Oo00Oo0 / II1Ii1iI1i
 ooo0OOO0 = common . GET_KODI_VERSION ( )
 if 11 - 11: ooooooO0oo + OooooooO - o00oOO0 * Ooo % i11iIiiIii - oOoOooOo0o0
 if ooo0OOO0 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 elif ooo0OOO0 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 83 - 83: oOOO00o / i1IIi11111i
def iIIiIi1iIII1 ( ) :
 if 78 - 78: oooO0oo0oOOOO . Ooo . i1111 % oo0Oo00Oo0
 i1iIi = 0
 if not os . path . exists ( oOoOo00oOo ) :
  i1iIi = 1
  common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
 else :
  O0o0 = open ( oOoOo00oOo , "r" )
  OO00Oo = re . compile ( r'<password>(.+?)</password>' )
  for O0OOO0OOoO0O in O0o0 :
   file = OO00Oo . findall ( O0OOO0OOoO0O )
   for O00Oo000ooO0 in file :
    OoO0O00 = base64 . b64decode ( O00Oo000ooO0 )
    i1iIi = 1
    common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR lime]ON[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR white]Current Password - [/COLOR][COLOR orangered]" + str ( OoO0O00 ) + "[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR lime]Change Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR orangered]Disable Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
    if 68 - 68: i11iIiiIii % Ooooo0Oo00oO0 + i11iIiiIii
 if i1iIi == 0 :
  common . addLink ( "[COLOR rose]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
  if 31 - 31: i1111 . i1IIi11111i
def II1I ( ) :
 if 84 - 84: Oo0O0OOOoo . i11iIiiIii . Oo0O0OOOoo * Ooooo0Oo00oO0 - oOOO00o
 ii = plugintools . get_setting ( "history_setting" )
 if 81 - 81: oOoOooOo0o0 % OooooooO . Ooooo0Oo00oO0 / oo0ooO0oOOOOo
 if ii == "true" :
  common . addLink ( '[COLOR deeppink]Clear History[/COLOR]' , iiI1iIiI , 104 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR orangered]Disable History[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '###########################################' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
  if 40 - 40: i1IIi11111i + i111I
  O0oo0OO0oOOOo = open ( IIiiIiI1 , mode = 'r' ) ; i1i1i11IIi = O0oo0OO0oOOOo . read ( ) ; O0oo0OO0oOOOo . close ( )
  i1i1i11IIi = i1i1i11IIi . replace ( '\n' , '' )
  iiiI1I11i1 = re . compile ( '<item>(.+?)</item>' ) . findall ( i1i1i11IIi )
  for IIi1i11111 in iiiI1I11i1 :
   o0O000oo = re . compile ( '<date>(.+?)</date>' ) . findall ( IIi1i11111 ) [ 0 ]
   time = re . compile ( '<time>(.+?)</time>' ) . findall ( IIi1i11111 ) [ 0 ]
   IIi1I11I1II = re . compile ( '<name>(.+?)</name>' ) . findall ( IIi1i11111 ) [ 0 ]
   ooo00OOOooO = re . compile ( '<link>(.+?)</link>' ) . findall ( IIi1i11111 ) [ 0 ]
   OooOoooOo = re . compile ( '<site>(.+?)</site>' ) . findall ( IIi1i11111 ) [ 0 ]
   ii11IIII11I = re . compile ( '<icon>(.+?)</icon>' ) . findall ( IIi1i11111 ) [ 0 ]
   ooo00OOOooO = IIi1I11I1II + '|SPLIT|' + ooo00OOOooO + '|SPLIT|' + OooOoooOo + '|SPLIT|' + ii11IIII11I + '|SPLIT|' + ooo00OOOooO
   if 81 - 81: OOO0O / oooO0oo0oOOOO . Oo0O0OOOoo . i1IIi11111i
   common . addLink ( '[COLOR pink]' + o0O000oo + ' | ' + '[/COLOR][COLOR deeppink]' + time + '[/COLOR] - [COLOR orangered]' + OooOoooOo + '[/COLOR][COLOR pink] - ' + IIi1I11I1II + '[/COLOR]' , ooo00OOOooO , 800 , ii11IIII11I , O0O0OO0O0O0 )
 else :
  common . addLink ( '[COLOR orangered]Enable History Monitoring[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '############################################' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR pink]History monitoring is currently disabled.[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
  if 72 - 72: II1Ii1iI1i / oo + i111I - I11i1i11i1I
def iI1Iii ( ) :
 if 68 - 68: oo0Oo00Oo0 % oOoOooOo0o0
 common . addLink ( '[COLOR deeppink]Your Favourites[/COLOR]' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 if 88 - 88: ooO0oo0oO0 - o00oOO0 + oo0Oo00Oo0
 O0oo0OO0oOOOo = open ( iiIiIIi , mode = 'r' ) ; i1i1i11IIi = O0oo0OO0oOOOo . read ( ) ; O0oo0OO0oOOOo . close ( )
 i1i1i11IIi = i1i1i11IIi . replace ( '\n' , '' )
 iiiI1I11i1 = re . compile ( '<item>(.+?)</item>' ) . findall ( i1i1i11IIi )
 for IIi1i11111 in iiiI1I11i1 :
  IIi1I11I1II = re . compile ( '<name>(.+?)</name>' ) . findall ( IIi1i11111 ) [ 0 ]
  ooo00OOOooO = re . compile ( '<link>(.+?)</link>' ) . findall ( IIi1i11111 ) [ 0 ]
  OooOoooOo = re . compile ( '<site>(.+?)</site>' ) . findall ( IIi1i11111 ) [ 0 ]
  ii11IIII11I = re . compile ( '<icon>(.+?)</icon>' ) . findall ( IIi1i11111 ) [ 0 ]
  ooo00OOOooO = IIi1I11I1II + '|SPLIT|' + ooo00OOOooO + '|SPLIT|' + OooOoooOo + '|SPLIT|' + ii11IIII11I + '|SPLIT|' + ooo00OOOooO
  common . addLink ( '[COLOR orangered]' + OooOoooOo + '[/COLOR][COLOR pink] - ' + IIi1I11I1II + '[/COLOR]' , ooo00OOOooO , 103 , ii11IIII11I , O0O0OO0O0O0 )
  if 40 - 40: i1IIi11111i * ooooooO0oo + oo0Oo00Oo0 % OooooooO
def OOOOOoo0 ( name , url , iconimage ) :
 if 49 - 49: oooO0oo0oOOOO . OooooooO
 I1iI1iIi111i = url
 I1III , OO0O0OoOO0 , iiIi1IIi1I , o0OoOO000ooO0 , url = url . split ( '|SPLIT|' )
 if 56 - 56: OooooooO
 OO0OoO0o00 = '\n<item>\n<name>' + I1III + '</name>\n<link>' + OO0O0OoOO0 + '</link>\n<site>' + iiIi1IIi1I + '</site>\n<icon>' + o0OoOO000ooO0 + '</icon>\n</item>\n'
 if 86 - 86: i1111 % oOoOooOo0o0
 II1III = OOo . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Remove from Favourites[/B][/COLOR]' ] )
 if 15 - 15: II1Ii1iI1i * i1IIi11111i + i11iIiiIii
 if II1III == 0 :
  I1Ii ( name , I1iI1iIi111i , iconimage )
 else :
  O0oo00o0O = open ( iiIiIIi ) . read ( )
  O0oo0OO0oOOOo = O0oo00o0O . replace ( OO0OoO0o00 , '\n' )
  i1I1I = open ( iiIiIIi , mode = 'w' )
  i1I1I . write ( str ( O0oo0OO0oOOOo ) )
  i1I1I . close ( )
  xbmc . executebuiltin ( "Container.Refresh" )
  quit ( )
  if 12 - 12: i11iIiiIii / oo
def o0OIiII ( name , url , iconimage ) :
 if 25 - 25: oooO0oo0oOOOO - oooO0oo0oOOOO * oo0ooO0oOOOOo
 I1iI1iIi111i = url
 I1III , OO0O0OoOO0 , iiIi1IIi1I , o0OoOO000ooO0 , url = url . split ( '|SPLIT|' )
 if 51 - 51: I11i1i11i1I - Ooo + i1111 * ooooooO0oo . oOOO00o + Ooo
 II1III = OOo . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Delete Download[/B][/COLOR]' ] )
 if 78 - 78: i11iIiiIii / OooooooO - ooooooO0oo / oo0Oo00Oo0 + Ooo
 if II1III == 0 :
  I1Ii ( name , I1iI1iIi111i , iconimage )
 else :
  os . remove ( url )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 82 - 82: ooooooO0oo
def iiI1Ii1iI1 ( ) :
 if 87 - 87: I11i1i11i1I . Oo0O0OOOoo
 if os . path . isfile ( IIiiIiI1 ) :
  II1III = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Would you like to clear all stored history?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[B][COLOR orangered]NO[/COLOR][/B]' )
  if II1III == 1 :
   os . remove ( IIiiIiI1 )
   O0oo0OO0oOOOo = open ( IIiiIiI1 , 'w' )
   O0oo0OO0oOOOo . write ( '#START OF FILE#' )
   O0oo0OO0oOOOo . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 75 - 75: o00oOO0 + OOO0O + oo0ooO0oOOOOo * oOOO00o % Ooo . OooooooO
def oO ( ) :
 if 31 - 31: oo0Oo00Oo0 + i11iIiiIii + I11i1i11i1I * o00oOO0
 ooOooo000oOO = plugintools . get_setting ( "download_location" )
 IiII111iI1ii1 = xbmc . translatePath ( ooOooo000oOO )
 common . addLink ( '[COLOR deeppink]Download Location: [/COLOR]' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( IiII111iI1ii1 , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '[COLOR orangered]Change Download Location[/COLOR]' , iiI1iIiI , 106 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , iiI1iIiI , 999 , iiiii , O0O0OO0O0O0 )
 if 37 - 37: Ooo - oOoOooOo0o0 % I11i1i11i1I
 OOOoo0OO = [ '.mp4' ]
 if 57 - 57: oo / o00oOO0
 for file in os . listdir ( IiII111iI1ii1 ) :
  for Ii1I1Ii in OOOoo0OO :
   if file . endswith ( Ii1I1Ii ) :
    ii11IIII11I = iiiii
    O0oo0OO0oOOOo = open ( ooOoo0O , mode = 'r' ) ; i1i1i11IIi = O0oo0OO0oOOOo . read ( ) ; O0oo0OO0oOOOo . close ( )
    i1i1i11IIi = i1i1i11IIi . replace ( '\n' , '' )
    iiiI1I11i1 = re . compile ( '<item>(.+?)</item>' ) . findall ( i1i1i11IIi )
    for IIi1i11111 in iiiI1I11i1 :
     IIi1I11I1II = re . compile ( '<name>(.+?)</name>' ) . findall ( IIi1i11111 ) [ 0 ]
     OOoO0 = re . compile ( '<icon>(.+?)</icon>' ) . findall ( IIi1i11111 ) [ 0 ]
     if file in IIi1I11I1II :
      ii11IIII11I = OOoO0
    ooo00OOOooO = xbmc . translatePath ( os . path . join ( IiII111iI1ii1 , file ) )
    if "http" in ii11IIII11I :
     OO0Oooo0oOO0O = file + '|SPLIT|' + ooo00OOOooO + '|SPLIT|Downloaded|SPLIT|' + ii11IIII11I + '|SPLIT|' + ooo00OOOooO
    else :
     OO0Oooo0oOO0O = file + '|SPLIT|' + ooo00OOOooO + '|SPLIT|Downloaded|SPLIT|None|SPLIT|' + ooo00OOOooO
    common . addLink ( '[COLOR pink]' + file + '[/COLOR]' , OO0Oooo0oOO0O , 107 , ii11IIII11I , O0O0OO0O0O0 )
    if 62 - 62: i1IIi11111i
def O00o0OO0 ( ) :
 if 35 - 35: Ooo % o00oOO0 / oOoOooOo0o0 + ooO0oo0oO0 . i111I . i1IIi11111i
 ooOooo000oOO = plugintools . get_setting ( "download_location" )
 o00oOOooOOo0o = OOo . browse ( 3 , Oo0Ooo , 'files' , '' , False , False , oO000OoOoo00o )
 O0oo00o0O = open ( iiiI11 ) . read ( )
 O0oo0OO0oOOOo = O0oo00o0O . replace ( ooOooo000oOO , o00oOOooOOo0o )
 i1I1I = open ( iiiI11 , mode = 'w' )
 i1I1I . write ( str ( O0oo0OO0oOOOo ) )
 i1I1I . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 66 - 66: OooooooO - OooooooO - i11iIiiIii . Ooooo0Oo00oO0 - oo0Oo00Oo0
def oOOo0O00o ( name , url , iconimage ) :
 if 8 - 8: oo
 I1III , OO0O0OoOO0 , iiIi1IIi1I , o0OoOO000ooO0 , url = url . split ( '|SPLIT|' )
 name = I1III
 ii1111iII = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 iiiiI = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 OO0OoO0o00 = '\n<item>\n<date>' + ii1111iII + '</date>\n<time>' + iiiiI + '</time>\n<name>' + I1III + '</name>\n<link>' + OO0O0OoOO0 + '</link>\n<site>' + iiIi1IIi1I + '</site>\n<icon>' + o0OoOO000ooO0 + '</icon>\n</item>\n'
 I1III = open ( IIiiIiI1 ) . read ( )
 OO0O0OoOO0 = I1III . replace ( '#START OF FILE#' , '#START OF FILE#' + OO0OoO0o00 )
 O0oo0OO0oOOOo = open ( IIiiIiI1 , mode = 'w' )
 O0oo0OO0oOOOo . write ( str ( OO0O0OoOO0 ) )
 O0oo0OO0oOOOo . close ( )
 if 62 - 62: i111I * i1IIi11111i
 if iconimage == "None" :
  iconimage = iiiii
 oOOOoo0O0oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oOOOoo0O0oO , False )
 if 6 - 6: oo0Oo00Oo0 * oo0ooO0oOOOOo + OooooooO
def I1Ii ( name , url , iconimage ) :
 if 44 - 44: ooooooO0oo % oo + i111I - oooO0oo0oOOOO - ooooooO0oo - i1111
 I1III , OO0O0OoOO0 , iiIi1IIi1I , o0OoOO000ooO0 , url = url . split ( '|SPLIT|' )
 name = I1III
 ii1111iII = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 iiiiI = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 OO0OoO0o00 = '\n<item>\n<date>' + ii1111iII + '</date>\n<time>' + iiiiI + '</time>\n<name>' + I1III + '</name>\n<link>' + OO0O0OoOO0 + '</link>\n<site>' + iiIi1IIi1I + '</site>\n<icon>' + o0OoOO000ooO0 + '</icon>\n</item>\n'
 I1III = open ( IIiiIiI1 ) . read ( )
 OO0O0OoOO0 = I1III . replace ( '#START OF FILE#' , '#START OF FILE#' + OO0OoO0o00 )
 O0oo0OO0oOOOo = open ( IIiiIiI1 , mode = 'w' )
 O0oo0OO0oOOOo . write ( str ( OO0O0OoOO0 ) )
 O0oo0OO0oOOOo . close ( )
 if 99 - 99: o00oOO0 . ooooooO0oo + oOoOooOo0o0 + i111I % oo0ooO0oOOOOo
 if iconimage == "None" :
  iconimage = iiiii
  if 51 - 51: ooO0oo0oO0
 if "highwebmedia" in url :
  OOo . ok ( Oo0Ooo , '[COLOR pink]Chaturbate links are taken at the time of broadcasting. If this broadcast has ended the link will no longer play. [/COLOR]' )
 oOOOoo0O0oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oOOOoo0O0oO , False )
 if 34 - 34: Ooo + i1IIi11111i - Ooo
def IiI1I1i1I1 ( name , url , iconimage ) :
 if 98 - 98: oOOO00o % i11iIiiIii % o00oOO0 + ooooooO0oo
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   if 78 - 78: Ooooo0Oo00oO0 % Ooo / OooooooO - ooO0oo0oO0
 oOOOoo0O0oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oOOOoo0O0oO , False )
 if 69 - 69: oOoOooOo0o0
def oo0OooOOo0 ( ) :
 if 11 - 11: i1IIi11111i
 IiII1I11i1I1I = common . _get_keyboard ( heading = "Please Set Password" )
 if ( not IiII1I11i1I1I ) :
  OOo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 oO0Oo = IiII1I11i1I1I
 if 16 - 16: ooooooO0oo + Oo0O0OOOoo * oooO0oo0oOOOO % II1Ii1iI1i . i1IIi11111i
 IiII1I11i1I1I = common . _get_keyboard ( heading = "Please Confirm Your Password" )
 if ( not IiII1I11i1I1I ) :
  OOo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 Oo0OO = IiII1I11i1I1I
 if 78 - 78: oo0Oo00Oo0 - i111I - Ooooo0Oo00oO0 / o00oOO0 / i1111
 if not os . path . exists ( oOoOo00oOo ) :
  if not os . path . exists ( OOooO ) :
   os . makedirs ( OOooO )
  open ( oOoOo00oOo , 'w' )
  if 29 - 29: i1IIi11111i % i1IIi11111i
  if oO0Oo == Oo0OO :
   Oo0O0 = base64 . b64encode ( oO0Oo )
   O0oo0OO0oOOOo = open ( oOoOo00oOo , 'w' )
   O0oo0OO0oOOOo . write ( '<password>' + str ( Oo0O0 ) + '</password>' )
   O0oo0OO0oOOOo . close ( )
   OOo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   OOo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
 else :
  os . remove ( oOoOo00oOo )
  if 82 - 82: i1111 % oOOO00o / oo + OOO0O / oo0ooO0oOOOOo / oOoOooOo0o0
  if oO0Oo == Oo0OO :
   Oo0O0 = base64 . b64encode ( oO0Oo )
   O0oo0OO0oOOOo = open ( oOoOo00oOo , 'w' )
   O0oo0OO0oOOOo . write ( '<password>' + str ( Oo0O0 ) + '</password>' )
   O0oo0OO0oOOOo . close ( )
   OOo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   OOo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
   if 70 - 70: Ooo
def oOOoO0o0oO ( ) :
 if 93 - 93: Oo0O0OOOoo * i111I + o00oOO0
 try :
  os . remove ( oOoOo00oOo )
  OOo . ok ( Oo0Ooo , 'Parental controls have been disabled.' )
  xbmc . executebuiltin ( "Container.Refresh" )
 except :
  OOo . ok ( Oo0Ooo , 'There was an error disabling the parental controls.' )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 33 - 33: oooO0oo0oOOOO * oo0ooO0oOOOOo - oOoOooOo0o0 % oOoOooOo0o0
def I11I ( ) :
 if 50 - 50: oOoOooOo0o0 * i11iIiiIii * ooO0oo0oO0 - i1111 * oo0ooO0oOOOOo * OOO0O
 OoooOoo = 0
 if 74 - 74: ooooooO0oo - Oo0O0OOOoo / OooooooO * oooO0oo0oOOOO - oo0Oo00Oo0
 try :
  common . open_url ( "http://www.google.com" )
 except :
  OOo . ok ( Oo0Ooo , '[COLOR orangered]Error: It appears you do not currently have an active internet connection. This will cause false positives in the test. Please try again with an active internet connection.[/COLOR]' )
  return
  if 19 - 19: i1IIi11111i
 Ii1IIii11 . create ( Oo0Ooo , "Checking for repository updates" , '' , 'Please Wait...' )
 Ii1IIii11 . update ( 0 )
 I1III = open ( Ii1iIIIi1ii ) . read ( )
 OO0O0OoOO0 = I1III . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 iiiI1I11i1 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO0O0OoOO0 ) )
 for IIi1i11111 in iiiI1I11i1 :
  Ii1IIii11 . update ( 25 )
  i11i = float ( IIi1i11111 ) + 0.01
  ooo00OOOooO = o0oO + str ( i11i ) + '.zip'
  try :
   o0oooOO00 = common . open_url ( ooo00OOOooO )
   if "Not Found" not in o0oooOO00 :
    i1iIi = 1
    Ii1IIii11 . update ( 75 )
    iiIiii1IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( iiIiii1IIIII ) :
     os . makedirs ( iiIiii1IIIII )
    o00o = os . path . join ( iiIiii1IIIII , 'repoupdate.zip' )
    try : os . remove ( o00o )
    except : pass
    Ii1IIii11 . update ( 100 )
    Ii1IIii11 . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( ooo00OOOooO , o00o , Ii1IIii11 )
    IIIIiiIiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    Ii1IIii11 . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( o00o , IIIIiiIiiI , Ii1IIii11 )
    try : os . remove ( o00o )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    OoooOoo = 1
    OOo . ok ( Oo0Ooo , "ECHO XXX repository was updated to " + str ( i11i ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 10 - 10: OOO0O % OOO0O - OOO0O . OooooooO
 Ii1IIii11 . update ( 75 , "Checking for addon updates" )
 I1III = open ( O0O00o0OOO0 ) . read ( )
 OO0O0OoOO0 = I1III . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 iiiI1I11i1 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO0O0OoOO0 ) )
 for IIi1i11111 in iiiI1I11i1 :
  i11i = float ( IIi1i11111 ) + 0.01
  ooo00OOOooO = o0oo0o0O00OO + str ( i11i ) + '.zip'
  try :
   o0oooOO00 = common . open_url ( ooo00OOOooO )
   if "Not Found" not in o0oooOO00 :
    i1iIi = 1
    Ii1IIii11 . update ( 75 )
    iiIiii1IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( iiIiii1IIIII ) :
     os . makedirs ( iiIiii1IIIII )
    o00o = os . path . join ( iiIiii1IIIII , 'xxx_o_dus_update.zip' )
    try : os . remove ( o00o )
    except : pass
    Ii1IIii11 . update ( 100 )
    Ii1IIii11 . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( ooo00OOOooO , o00o , Ii1IIii11 )
    IIIIiiIiiI = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    Ii1IIii11 . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( o00o , IIIIiiIiiI , Ii1IIii11 )
    try : os . remove ( o00o )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    Ii1IIii11 . update ( 100 )
    Ii1IIii11 . close
    OoooOoo = 1
    OOo . ok ( Oo0Ooo , "XXX-O-DUS was updated to " + str ( i11i ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 73 - 73: oOOO00o % i11iIiiIii - i1IIi11111i
 if Ii1IIii11 . iscanceled ( ) :
  Ii1IIii11 . close ( )
  if 7 - 7: oooO0oo0oOOOO * i11iIiiIii * ooooooO0oo + o00oOO0 % oo - o00oOO0
 return OoooOoo
 if 39 - 39: I11i1i11i1I * oo0Oo00Oo0 % oo0Oo00Oo0 - i111I + oo0ooO0oOOOOo - oOOO00o
def iiO0oOo00o ( url ) :
 if 81 - 81: Oo0O0OOOoo % II1Ii1iI1i . ooO0oo0oO0
 O0oo0OO0oOOOo = open ( url , mode = 'r' ) ; i1i1i11IIi = O0oo0OO0oOOOo . read ( ) ; O0oo0OO0oOOOo . close ( )
 common . TextBoxes ( "%s" % i1i1i11IIi )
 if 4 - 4: i11iIiiIii % oo % II1Ii1iI1i / Oo0O0OOOoo
 if url == IiIIIiI1I1 :
  return
  if 6 - 6: OooooooO / i1IIi11111i % oo0Oo00Oo0 - i1IIi11111i
def iiii111II ( ) :
 if 50 - 50: oo0Oo00Oo0 * i1IIi11111i % ooO0oo0oO0 + ooooooO0oo + OooooooO + i1IIi11111i
 try :
  iiO0oOo00o ( IiIIIiI1I1 )
  if 71 - 71: Ooooo0Oo00oO0 * Ooooo0Oo00oO0 * II1Ii1iI1i . Ooo / oOoOooOo0o0
  II1III = xbmcgui . Dialog ( ) . yesno ( "[COLOR orangered][B]RESET XXX-O-DUS?[/B][/COLOR]" , '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]' , '' , yeslabel = '[COLOR green]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if II1III == 1 :
   ooOooo000oOO = plugintools . get_setting ( "download_location" )
   IiII111iI1ii1 = xbmc . translatePath ( ooOooo000oOO )
   if 85 - 85: oOOO00o
   OOOoo0OO = [ '.mp4' ]
   if 20 - 20: Ooo % Oo0O0OOOoo
   for file in os . listdir ( IiII111iI1ii1 ) :
    for Ii1I1Ii in OOOoo0OO :
     if file . endswith ( Ii1I1Ii ) :
      try :
       iiIiii1IIIII = xbmc . translatePath ( os . path . join ( IiII111iI1ii1 , file ) )
       os . remove ( iiIiii1IIIII )
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
  if 19 - 19: Ooooo0Oo00oO0 % Oo0O0OOOoo + o00oOO0 / oOoOooOo0o0 . o00oOO0
def IiIi1I1 ( ) :
 IiIIi1 = [ ]
 IIIIiii1IIii = sys . argv [ 2 ]
 if len ( IIIIiii1IIii ) >= 2 :
  II1i11I = sys . argv [ 2 ]
  ii1I1IIii11 = II1i11I . replace ( '?' , '' )
  if ( II1i11I [ len ( II1i11I ) - 1 ] == '/' ) :
   II1i11I = II1i11I [ 0 : len ( II1i11I ) - 2 ]
  O0o0oO = ii1I1IIii11 . split ( '&' )
  IiIIi1 = { }
  for IIIIiIiIi1 in range ( len ( O0o0oO ) ) :
   I11iiiiI1i = { }
   I11iiiiI1i = O0o0oO [ IIIIiIiIi1 ] . split ( '=' )
   if ( len ( I11iiiiI1i ) ) == 2 :
    IiIIi1 [ I11iiiiI1i [ 0 ] ] = I11iiiiI1i [ 1 ]
    if 40 - 40: Ooooo0Oo00oO0 + II1Ii1iI1i * oo0Oo00Oo0
 return IiIIi1
 if 85 - 85: ooooooO0oo * I11i1i11i1I . oooO0oo0oOOOO - i11iIiiIii
II1i11I = IiIi1I1 ( ) ; i1I1iIi = None ; ooo00OOOooO = None ; IIii11Ii1i1I = None ; ii11IIII11I = None ; Oooo0O = None
try : i1I1iIi = urllib . unquote_plus ( II1i11I [ "name" ] )
except : pass
try : ooo00OOOooO = urllib . unquote_plus ( II1i11I [ "url" ] )
except : pass
try : IIii11Ii1i1I = int ( II1i11I [ "mode" ] )
except : pass
try : ii11IIII11I = urllib . unquote_plus ( II1i11I [ "iconimage" ] )
except : pass
try : Oooo0O = urllib . quote_plus ( II1i11I [ "fanartimage" ] )
except : pass
if 90 - 90: ooO0oo0oO0 % o00oOO0
if IIii11Ii1i1I == None or ooo00OOOooO == None or len ( ooo00OOOooO ) < 1 : iii11I111 ( )
elif IIii11Ii1i1I == 1 : menus . SEARCH ( )
elif IIii11Ii1i1I == 2 : menus . VIDEOS ( )
elif IIii11Ii1i1I == 3 : menus . LIVE ( )
elif IIii11Ii1i1I == 4 : menus . PICTURES ( )
elif IIii11Ii1i1I == 5 : menus . STORIES ( )
elif IIii11Ii1i1I == 6 : menus . ALL ( )
elif IIii11Ii1i1I == 10 : xhamster . MAIN_MENU ( )
elif IIii11Ii1i1I == 11 : xhamster . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 12 : xhamster . SEARCH ( )
elif IIii11Ii1i1I == 13 : xhamster . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 20 : chaturbate . MAIN_MENU ( )
elif IIii11Ii1i1I == 21 : chaturbate . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 22 : chaturbate . SEARCH ( )
elif IIii11Ii1i1I == 23 : chaturbate . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 30 : xnxx . MAIN_MENU ( )
elif IIii11Ii1i1I == 31 : xnxx . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 32 : xnxx . SEARCH ( )
elif IIii11Ii1i1I == 33 : xnxx . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 34 : xnxx . PICTURE_MENU ( )
elif IIii11Ii1i1I == 35 : xnxx . PICTURE_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 36 : xnxx . SCRAPE_GALLERY ( ooo00OOOooO )
elif IIii11Ii1i1I == 37 : xnxx . DISPLAY_PICTURE ( ooo00OOOooO )
elif IIii11Ii1i1I == 38 : xnxx . STORY_MENU ( )
elif IIii11Ii1i1I == 39 : xnxx . LIST_STORIES ( ooo00OOOooO )
elif IIii11Ii1i1I == 40 : xnxx . DISPLAY_STORY ( ooo00OOOooO )
elif IIii11Ii1i1I == 41 : redtube . MAIN_MENU ( )
elif IIii11Ii1i1I == 42 : redtube . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 43 : redtube . SEARCH ( )
elif IIii11Ii1i1I == 44 : redtube . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 50 : pornhd . MAIN_MENU ( )
elif IIii11Ii1i1I == 51 : pornhd . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 52 : pornhd . SEARCH ( )
elif IIii11Ii1i1I == 53 : pornhd . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 60 : porncom . MAIN_MENU ( )
elif IIii11Ii1i1I == 61 : porncom . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 62 : porncom . SEARCH ( )
elif IIii11Ii1i1I == 63 : porncom . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 70 : youporn . MAIN_MENU ( )
elif IIii11Ii1i1I == 71 : youporn . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 72 : youporn . SEARCH ( )
elif IIii11Ii1i1I == 73 : youporn . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 80 : pornfun . MAIN_MENU ( )
elif IIii11Ii1i1I == 81 : pornfun . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 82 : pornfun . SEARCH ( )
elif IIii11Ii1i1I == 83 : pornfun . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 90 : motherless . MAIN_MENU ( )
elif IIii11Ii1i1I == 91 : motherless . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 92 : motherless . DISPLAY_PICTURE ( ooo00OOOooO )
elif IIii11Ii1i1I == 300 : watchxxxfree . MAIN_MENU ( )
elif IIii11Ii1i1I == 301 : watchxxxfree . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 302 : watchxxxfree . SEARCH ( )
elif IIii11Ii1i1I == 303 : watchxxxfree . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 310 : perfectgirls . MAIN_MENU ( )
elif IIii11Ii1i1I == 311 : perfectgirls . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 312 : perfectgirls . SEARCH ( )
elif IIii11Ii1i1I == 313 : perfectgirls . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 100 : iIii ( ) ;
elif IIii11Ii1i1I == 101 : II1I ( )
elif IIii11Ii1i1I == 102 : iI1Iii ( )
elif IIii11Ii1i1I == 103 : OOOOOoo0 ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 104 : iiI1Ii1iI1 ( )
elif IIii11Ii1i1I == 105 : oO ( )
elif IIii11Ii1i1I == 106 : plugintools . open_settings_dialog ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
elif IIii11Ii1i1I == 107 : o0OIiII ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 200 : spankbang . MAIN_MENU ( )
elif IIii11Ii1i1I == 201 : spankbang . SUB_MENU ( ooo00OOOooO )
elif IIii11Ii1i1I == 202 : spankbang . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 203 : spankbang . SEARCH ( )
elif IIii11Ii1i1I == 204 : spankbang . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 210 : porn00 . MAIN_MENU ( )
elif IIii11Ii1i1I == 211 : porn00 . GET_CONTENT ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 212 : porn00 . SEARCH ( )
elif IIii11Ii1i1I == 213 : porn00 . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 220 : virtualpornstars . MAIN_MENU ( )
elif IIii11Ii1i1I == 221 : virtualpornstars . GET_CONTENT ( ooo00OOOooO )
elif IIii11Ii1i1I == 222 : virtualpornstars . SEARCH ( )
elif IIii11Ii1i1I == 223 : virtualpornstars . PLAY_URL ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 800 : I1Ii ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 900 : iIIiIi1iIII1 ( )
elif IIii11Ii1i1I == 901 : oo0OooOOo0 ( )
elif IIii11Ii1i1I == 902 : oOOoO0o0oO ( )
elif IIii11Ii1i1I == 995 : common . GET_M3U_LIST ( ooo00OOOooO )
elif IIii11Ii1i1I == 996 : IiI1I1i1I1 ( i1I1iIi , ooo00OOOooO , ii11IIII11I )
elif IIii11Ii1i1I == 997 : iiii111II ( )
elif IIii11Ii1i1I == 998 : iiO0oOo00o ( ooo00OOOooO )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
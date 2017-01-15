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
if 41 - 41: I1II1
Ooo0OO0oOO = base64 . decodestring ( 'aHR0cDovL2VjaG9jb2Rlci5jb20vcHJpdmF0ZS9hZGRvbnMvc3BvcnRpZS9tZW51cy9tYWluLnhtbA==' )
oooO0oo0oOOOO = xbmcgui . Dialog ( )
O0oO = xbmcgui . DialogProgress ( )
if 68 - 68: o00ooo0 / Oo00O0
ooO0oooOoO0 = xbmc . translatePath ( 'special://home/' )
II11i = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o , 'settings.xml' ) )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o , 'parental' ) )
oOOoo00O0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o ) )
i1111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o ) )
i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.f4mTester' ) )
I11 = xbmc . translatePath ( os . path . join ( i1 , 'controls.txt' ) )
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( i1111 , 'resources/disclaimer.txt' ) )
oOo0oooo00o = xbmc . translatePath ( os . path . join ( i1111 , 'resources/information.txt' ) )
oO0o0o0ooO0oO = xbmc . translatePath ( os . path . join ( i1111 , 'resources/repository.txt' ) )
oo0o0O00 = xbmc . translatePath ( os . path . join ( i1111 , 'resources/reset.txt' ) )
oO = xbmc . translatePath ( os . path . join ( oOOoo00O0O , 'agreed.txt' ) )
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( oOOoo00O0O , 'history.xml' ) )
oooOOOOO = xbmc . translatePath ( os . path . join ( oOOoo00O0O , 'favourites.xml' ) )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( oOOoo00O0O , 'downloads.xml' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.xxxecho' ) )
if 50 - 50: IiIi1Iii1I1 - O00O0O0O0
ooO0O = xbmc . translatePath ( 'special://home/addons/' + OO0o + '/addon.xml' )
oo = xbmc . translatePath ( 'special://home/addons/repository.xxxecho/addon.xml' )
iii11iII = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9wbHVnaW4udmlkZW8ueHh4LW8tZHVzL3BsdWdpbi52aWRlby54eHgtby1kdXMt' )
i1I111I = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9yZXBvc2l0b3J5Lnh4eGVjaG8vcmVwb3NpdG9yeS54eHhlY2hvLQ==' )
if 1 - 1: O0OOooO % IiIiIi . II
def iI ( ) :
 if 22 - 22: IiiiI1II1I1 % ooIi11iI1i
 Ooo = i1iIIi1 + '|SPLIT|' + oO0o0o0ooO0oO
 checker . check ( Ooo )
 if 68 - 68: oOo00Oo00O + I11i1I + o0o0OOO0o0 % IIII % o0O0 . o0
 if not os . path . exists ( oO ) :
  I11II1i = open ( Oo0o0000o0o0 , mode = 'r' ) ; IIIII = I11II1i . read ( ) ; I11II1i . close ( )
  common . TextBoxes ( "%s" % IIIII )
  ooooooO0oo = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Do you agree to the terms and conditions of this addon?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if ooooooO0oo == 1 :
   I11II1i = open ( oOo0oooo00o , mode = 'r' ) ; IIIII = I11II1i . read ( ) ; I11II1i . close ( )
   common . TextBoxes ( "%s" % IIIII )
   oooO0oo0oOOOO . ok ( Oo0Ooo , "[COLOR pink]We can see this is the first time you have used XXX-O-DUS. The next prompt is important as it will allow you to enable the history section of the addon and it will also allow you to select the location you would like to be used to download videos.[/COLOR]" )
   plugintools . open_settings_dialog ( )
   open ( oO , 'w' )
  else :
   sys . exit ( 0 )
   if 49 - 49: ooo * I1I1i / IIIii1I1 * I1II1 + I11i1I
 if not os . path . exists ( i1 ) :
  ooooooO0oo = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , "[COLOR white]Would you like to enable the parental controls now?[/COLOR]" , "" , yeslabel = '[COLOR orangered]NO[/COLOR]' , nolabel = '[COLOR lime]YES[/COLOR]' )
  if ooooooO0oo == 0 :
   ii1i1I1i ( )
  else :
   os . makedirs ( i1 )
   if 53 - 53: ooo + O0OOooO * I11i1I
 elif os . path . exists ( I11 ) :
  OooOooooOOoo0 = common . _get_keyboard ( heading = "Please Enter Your Password" )
  if ( not OooOooooOOoo0 ) :
   oooO0oo0oOOOO . ok ( Oo0Ooo , "Sorry, no password was entered." )
   sys . exit ( 0 )
  o00OO0OOO0 = OooOooooOOoo0
  if 83 - 83: Oo00O0
  Iii111II = open ( I11 , "r" )
  iiii11I = re . compile ( r'<password>(.+?)</password>' )
  for Ooo0OO0oOOii11i1 in Iii111II :
   file = iiii11I . findall ( Ooo0OO0oOOii11i1 )
   for IIIii1II1II in file :
    i1I1iI = base64 . b64decode ( IIIii1II1II )
    if not i1I1iI == o00OO0OOO0 :
     if not IIIii1II1II == o00OO0OOO0 :
      oooO0oo0oOOOO . ok ( Oo0Ooo , "Sorry, the password you entered was incorrect." )
      sys . exit ( 0 )
      if 93 - 93: o00ooo0 % I11i1I * IiIi1Iii1I1
 Ii11Ii1I = plugintools . get_setting ( "download_location" )
 O00oO = xbmc . translatePath ( Ii11Ii1I )
 if not os . path . exists ( O00oO ) :
  os . makedirs ( O00oO )
  if 39 - 39: ooo - O00O0O0O0 * II % ooIi11iI1i * O00O0O0O0 % O00O0O0O0
 if not os . path . isfile ( i1iiIIiiI111 ) :
  I11II1i = open ( i1iiIIiiI111 , 'w' )
  I11II1i . write ( '#START OF FILE#' )
  I11II1i . close ( )
 if not os . path . isfile ( oooOOOOO ) :
  I11II1i = open ( oooOOOOO , 'w' )
  I11II1i . write ( '#START OF FILE#' )
  I11II1i . close ( )
 if not os . path . isfile ( i1iiIII111ii ) :
  I11II1i = open ( i1iiIII111ii , 'w' )
  I11II1i . write ( '#START OF FILE#' )
  I11II1i . close ( )
  if 59 - 59: o00ooo0 + O0OOooO - ooIi11iI1i - O0OOooO + o0o0OOO0o0 / oOo00Oo00O
 I1 = open ( ooO0O ) . read ( )
 OO00Oo = I1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0OOO0OOoO0O = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO00Oo ) )
 for O00Oo000ooO0 in O0OOO0OOoO0O :
  OoO0O00 = float ( O00Oo000ooO0 )
 I1 = open ( oo ) . read ( )
 OO00Oo = I1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0OOO0OOoO0O = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO00Oo ) )
 for O00Oo000ooO0 in O0OOO0OOoO0O :
  IIiII = float ( O00Oo000ooO0 )
  if 80 - 80: ooo . I11i1I
 common . addDir ( "[COLOR white]SEARCH XXX-O-DUS[/COLOR]" , "url" , 1 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Live[/COLOR]" , "url" , 3 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Videos[/COLOR]" , "url" , 2 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Photos[/COLOR]" , "url" , 4 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]Stories[/COLOR]" , "url" , 5 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR white]All Websites[/COLOR]" , "url" , 6 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR darkgray]#################################[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your History[/COLOR]" , Ooo0OO0oOO , 101 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Favourites[/COLOR]" , Ooo0OO0oOO , 102 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Downloads[/COLOR]" , Ooo0OO0oOO , 105 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Your Settings[/COLOR]" , Ooo0OO0oOO , 106 , iiiii , O0O0OO0O0O0 )
 if 25 - 25: IiiiI1II1I1 . O00O0O0O0 / o0 . o0o0OOO0o0 * II . O0OOooO
 if not os . path . exists ( I11 ) :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR orangered]OFF[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 else :
  common . addDir ( "[COLOR orangered]PARENTAL CONTROLS - [COLOR lime]ON[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]#####################################[/COLOR]" , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR pink]Twitter Support: [/COLOR][COLOR white]@EchoCoder[/COLOR]" , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Disclaimer[/COLOR]" , Oo0o0000o0o0 , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Addon Information[/COLOR]" , oOo0oooo00o , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR orangered]RESET XXX-O-DUS[/COLOR]" , 'url' , 997 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Addon Version:[/COLOR] [COLOR white]" + str ( OoO0O00 ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Repository Version:[/COLOR] [COLOR white]" + str ( IIiII ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 if 59 - 59: O00O0O0O0 + Oo00O0 * IiiiI1II1I1 + IiIi1Iii1I1
 Oo0OoO00oOO0o = common . GET_KODI_VERSION ( )
 if 80 - 80: I11i1I + o0o0OOO0o0 - o0o0OOO0o0 % o0
 if Oo0OoO00oOO0o == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif Oo0OoO00oOO0o == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 63 - 63: O0OOooO - oOo00Oo00O + I1II1 % IIII / o00ooo0 / ooIi11iI1i
def O0o0O00Oo0o0 ( ) :
 if 87 - 87: IIIii1I1 * IiIiIi % i11iIiiIii % IiiiI1II1I1 - o0o0OOO0o0
 O0ooo0O0oo0 = ''
 oo0oOo = xbmc . Keyboard ( O0ooo0O0oo0 , 'Enter Search Term' )
 oo0oOo . doModal ( )
 if oo0oOo . isConfirmed ( ) :
  o000O0o = oo0oOo . getText ( )
  iI1iII1 = o000O0o
  O0ooo0O0oo0 = o000O0o . replace ( ' ' , '+' )
  if len ( O0ooo0O0oo0 ) > 1 :
   try :
    O0oO . create ( Oo0Ooo , '[COLOR white]Searching: [/COLOR] [COLOR orangered]YouPorn[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]1 of 9[/COLOR]' )
    oO0OOoo0OO = "http://www.youporn.com/search/?query=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 15 )
    try :
     youporn . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://www.xnxx.com/?k=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 30 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]XNXX[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]2 of 9[/COLOR]' )
    try :
     xnxx . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "https://xhamster.com/search.php?from=&new=&q=" + O0ooo0O0oo0 . lower ( ) + "&qcat=video"
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 45 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Xhamster[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]3 of 9[/COLOR]' )
    try :
     xhamster . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://www.pornhd.com/search?search=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 60 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornHD[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]4 of 9[/COLOR]' )
    try :
     pornhd . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://www.porn.com/videos/search?q=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 75 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn.com[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]5 of 9[/COLOR]' )
    try :
     porncom . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://www.redtube.com/?search=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 90 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]RedTube[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]6 of 9[/COLOR]' )
    try :
     redtube . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://pornfun.com/search/?q=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 95 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]PornFun[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]7 of 9[/COLOR]' )
    try :
     pornfun . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://spankbang.com/s/" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 97 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Spankbang[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]8 of 9[/COLOR]' )
    try :
     spankbang . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    oO0OOoo0OO = "http://www.porn00.org/?s=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 99 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Porn00[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]9 of 9[/COLOR]' )
    try :
     porn00 . GET_CONTENT ( 'none' , oO0OOoo0OO , 'none' )
    except : pass
    O0oO . close ( )
    oO0OOoo0OO = "http://virtualpornstars.com/?s=" + O0ooo0O0oo0 . lower ( )
    oO0OOoo0OO = 'split|' + oO0OOoo0OO
    O0oO . update ( 100 , '[COLOR white]Searching: [/COLOR] [COLOR orangered]Virtual Porn Stars[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iI1iII1 . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]9 of 9[/COLOR]' )
    try :
     virtualpornstars . GET_CONTENT ( oO0OOoo0OO )
    except : pass
    O0oO . close ( )
   except :
    oooO0oo0oOOOO . ok ( Oo0Ooo , '[COLOR pink]Sorry, there was an error searching for ' + O0ooo0O0oo0 . lower ( ) + ' please try again later.[/COLOR]' )
    quit ( )
  else : quit ( )
  if 65 - 65: o0O0 . o00ooo0 / I1II1 - o0O0
 Oo0OoO00oOO0o = common . GET_KODI_VERSION ( )
 if 21 - 21: O0OOooO * o00ooo0
 if Oo0OoO00oOO0o == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 elif Oo0OoO00oOO0o == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 91 - 91: ooo
def iiIii ( ) :
 if 79 - 79: Oo00O0 / I1II1
 OO0OoO0o00 = 0
 if not os . path . exists ( I11 ) :
  OO0OoO0o00 = 1
  common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
 else :
  Iii111II = open ( I11 , "r" )
  iiii11I = re . compile ( r'<password>(.+?)</password>' )
  for Ooo0OO0oOOii11i1 in Iii111II :
   file = iiii11I . findall ( Ooo0OO0oOOii11i1 )
   for IIIii1II1II in file :
    i1I1iI = base64 . b64decode ( IIIii1II1II )
    OO0OoO0o00 = 1
    common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR lime]ON[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR white]Current Password - [/COLOR][COLOR orangered]" + str ( i1I1iI ) + "[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR lime]Change Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR orangered]Disable Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
    if 53 - 53: I1II1 * II + o0o0OOO0o0
 if OO0OoO0o00 == 0 :
  common . addLink ( "[COLOR rose]PARENTAL CONTROLS - [/COLOR][COLOR orangered]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
  if 50 - 50: I1II1 . I1II1 - I11i1I / O0OOooO - ooIi11iI1i * IiiiI1II1I1
def o0O00oOoOO ( ) :
 if 42 - 42: II
 o0o = plugintools . get_setting ( "history_setting" )
 if 84 - 84: I1II1
 if o0o == "true" :
  common . addLink ( '[COLOR deeppink]Clear History[/COLOR]' , Ooo0OO0oOO , 104 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR orangered]Disable History[/COLOR]' , Ooo0OO0oOO , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '###########################################' , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
  if 74 - 74: oOo00Oo00O - O0OOooO - IiIiIi . o0O0 - ooo
  I11II1i = open ( i1iiIIiiI111 , mode = 'r' ) ; IIIII = I11II1i . read ( ) ; I11II1i . close ( )
  IIIII = IIIII . replace ( '\n' , '' )
  O0OOO0OOoO0O = re . compile ( '<item>(.+?)</item>' ) . findall ( IIIII )
  for O00Oo000ooO0 in O0OOO0OOoO0O :
   OOOoOoo0O = re . compile ( '<date>(.+?)</date>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
   time = re . compile ( '<time>(.+?)</time>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
   O000OOo00oo = re . compile ( '<name>(.+?)</name>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
   oO0OOoo0OO = re . compile ( '<link>(.+?)</link>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
   oo0OOo = re . compile ( '<site>(.+?)</site>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
   ooOOO00Ooo = re . compile ( '<icon>(.+?)</icon>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
   oO0OOoo0OO = O000OOo00oo + '|SPLIT|' + oO0OOoo0OO + '|SPLIT|' + oo0OOo + '|SPLIT|' + ooOOO00Ooo + '|SPLIT|' + oO0OOoo0OO
   if 16 - 16: O00O0O0O0 % IiiiI1II1I1 - O00O0O0O0 + o0O0
   common . addLink ( '[COLOR pink]' + OOOoOoo0O + ' | ' + '[/COLOR][COLOR deeppink]' + time + '[/COLOR] - [COLOR orangered]' + oo0OOo + '[/COLOR][COLOR pink] - ' + O000OOo00oo + '[/COLOR]' , oO0OOoo0OO , 800 , ooOOO00Ooo , O0O0OO0O0O0 )
 else :
  common . addLink ( '[COLOR orangered]Enable History Monitoring[/COLOR]' , Ooo0OO0oOO , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '############################################' , Ooo0OO0oOO , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR pink]History monitoring is currently disabled.[/COLOR]' , Ooo0OO0oOO , 106 , iiiii , O0O0OO0O0O0 )
  if 12 - 12: o0o0OOO0o0 / o0o0OOO0o0 + i11iIiiIii
def Ii ( ) :
 if 22 - 22: O00O0O0O0
 common . addLink ( '[COLOR deeppink]Your Favourites[/COLOR]' , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 if 33 - 33: IIII
 I11II1i = open ( oooOOOOO , mode = 'r' ) ; IIIII = I11II1i . read ( ) ; I11II1i . close ( )
 IIIII = IIIII . replace ( '\n' , '' )
 O0OOO0OOoO0O = re . compile ( '<item>(.+?)</item>' ) . findall ( IIIII )
 for O00Oo000ooO0 in O0OOO0OOoO0O :
  O000OOo00oo = re . compile ( '<name>(.+?)</name>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
  oO0OOoo0OO = re . compile ( '<link>(.+?)</link>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
  oo0OOo = re . compile ( '<site>(.+?)</site>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
  ooOOO00Ooo = re . compile ( '<icon>(.+?)</icon>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
  oO0OOoo0OO = O000OOo00oo + '|SPLIT|' + oO0OOoo0OO + '|SPLIT|' + oo0OOo + '|SPLIT|' + ooOOO00Ooo + '|SPLIT|' + oO0OOoo0OO
  common . addLink ( '[COLOR orangered]' + oo0OOo + '[/COLOR][COLOR pink] - ' + O000OOo00oo + '[/COLOR]' , oO0OOoo0OO , 103 , ooOOO00Ooo , O0O0OO0O0O0 )
  if 18 - 18: ooIi11iI1i % o0 * I1II1
def o0O0Oooo0O ( name , url , iconimage ) :
 if 84 - 84: o0 . oOo00Oo00O / IiIiIi - O0OOooO / Oo00O0 / ooIi11iI1i
 II111iiiI1Ii = url
 I1 , OO00Oo , o0O0OOO0Ooo , iiIiI , url = url . split ( '|SPLIT|' )
 if 6 - 6: ooo . I11i1I * IiiiI1II1I1 - o0O0 - ooo
 O0ooo0O0oo0 = '\n<item>\n<name>' + I1 + '</name>\n<link>' + OO00Oo + '</link>\n<site>' + o0O0OOO0Ooo + '</site>\n<icon>' + iiIiI + '</icon>\n</item>\n'
 if 45 - 45: O0OOooO - Oo00O0 + o00ooo0 . O0OOooO * IIII
 ooooooO0oo = oooO0oo0oOOOO . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Remove from Favourites[/B][/COLOR]' ] )
 if 51 - 51: II / II
 if ooooooO0oo == 0 :
  ooOOO0 ( name , II111iiiI1Ii , iconimage )
 else :
  o0oO0OOoO00OO0o = open ( oooOOOOO ) . read ( )
  I11II1i = o0oO0OOoO00OO0o . replace ( O0ooo0O0oo0 , '\n' )
  I1111IIIIIi = open ( oooOOOOO , mode = 'w' )
  I1111IIIIIi . write ( str ( I11II1i ) )
  I1111IIIIIi . close ( )
  xbmc . executebuiltin ( "Container.Refresh" )
  quit ( )
  if 22 - 22: IiIi1Iii1I1 + I1II1 . o00ooo0 * o0 % i11iIiiIii * O0OOooO
def oo000o ( name , url , iconimage ) :
 if 44 - 44: IiIi1Iii1I1 % O00O0O0O0 + IIII
 II111iiiI1Ii = url
 I1 , OO00Oo , o0O0OOO0Ooo , iiIiI , url = url . split ( '|SPLIT|' )
 if 45 - 45: o0 / o0 + I1I1i + IIIii1I1
 ooooooO0oo = oooO0oo0oOOOO . select ( "[COLOR orangered][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Delete Download[/B][/COLOR]' ] )
 if 47 - 47: ooIi11iI1i + IIIii1I1
 if ooooooO0oo == 0 :
  ooOOO0 ( name , II111iiiI1Ii , iconimage )
 else :
  os . remove ( url )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 82 - 82: O00O0O0O0 . ooo - o00ooo0 - ooo * O00O0O0O0
def ooO0oOOooOo0 ( ) :
 if 38 - 38: I1I1i
 if os . path . isfile ( i1iiIIiiI111 ) :
  ooooooO0oo = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Would you like to clear all stored history?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[B][COLOR orangered]NO[/COLOR][/B]' )
  if ooooooO0oo == 1 :
   os . remove ( i1iiIIiiI111 )
   I11II1i = open ( i1iiIIiiI111 , 'w' )
   I11II1i . write ( '#START OF FILE#' )
   I11II1i . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 84 - 84: o00ooo0 % o0 / o00ooo0 % IIII
def ii ( ) :
 if 84 - 84: ooIi11iI1i % O00O0O0O0 . i11iIiiIii / II
 Ii11Ii1I = plugintools . get_setting ( "download_location" )
 o0OIiII = xbmc . translatePath ( Ii11Ii1I )
 common . addLink ( '[COLOR deeppink]Download Location: [/COLOR]' , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( o0OIiII , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '[COLOR orangered]Change Download Location[/COLOR]' , Ooo0OO0oOO , 106 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , Ooo0OO0oOO , 999 , iiiii , O0O0OO0O0O0 )
 if 25 - 25: I1II1 - I1II1 * ooIi11iI1i
 OOOO0oo0 = [ '.mp4' ]
 if 35 - 35: o0O0 - O0OOooO % ooIi11iI1i . Oo00O0 % o0O0
 for file in os . listdir ( o0OIiII ) :
  for I1i1Iiiii in OOOO0oo0 :
   if file . endswith ( I1i1Iiiii ) :
    ooOOO00Ooo = iiiii
    I11II1i = open ( i1iiIII111ii , mode = 'r' ) ; IIIII = I11II1i . read ( ) ; I11II1i . close ( )
    IIIII = IIIII . replace ( '\n' , '' )
    O0OOO0OOoO0O = re . compile ( '<item>(.+?)</item>' ) . findall ( IIIII )
    for O00Oo000ooO0 in O0OOO0OOoO0O :
     O000OOo00oo = re . compile ( '<name>(.+?)</name>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
     OOo0oO00ooO00 = re . compile ( '<icon>(.+?)</icon>' ) . findall ( O00Oo000ooO0 ) [ 0 ]
     if file in O000OOo00oo :
      ooOOO00Ooo = OOo0oO00ooO00
    oO0OOoo0OO = xbmc . translatePath ( os . path . join ( o0OIiII , file ) )
    if "http" in ooOOO00Ooo :
     oOO0O00oO0Ooo = file + '|SPLIT|' + oO0OOoo0OO + '|SPLIT|Downloaded|SPLIT|' + ooOOO00Ooo + '|SPLIT|' + oO0OOoo0OO
    else :
     oOO0O00oO0Ooo = file + '|SPLIT|' + oO0OOoo0OO + '|SPLIT|Downloaded|SPLIT|None|SPLIT|' + oO0OOoo0OO
    common . addLink ( '[COLOR pink]' + file + '[/COLOR]' , oOO0O00oO0Ooo , 107 , ooOOO00Ooo , O0O0OO0O0O0 )
    if 67 - 67: II - o0o0OOO0o0
def iI1i11iII111 ( ) :
 if 15 - 15: i11iIiiIii % o0O0 . IiIiIi + oOo00Oo00O
 Ii11Ii1I = plugintools . get_setting ( "download_location" )
 OO0OOOOoo0OOO = oooO0oo0oOOOO . browse ( 3 , Oo0Ooo , 'files' , '' , False , False , ooO0oooOoO0 )
 o0oO0OOoO00OO0o = open ( II11i ) . read ( )
 I11II1i = o0oO0OOoO00OO0o . replace ( Ii11Ii1I , OO0OOOOoo0OOO )
 I1111IIIIIi = open ( II11i , mode = 'w' )
 I1111IIIIIi . write ( str ( I11II1i ) )
 I1111IIIIIi . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 27 - 27: IIIii1I1 + O00O0O0O0
def o0Oo00 ( name , url , iconimage ) :
 if 32 - 32: ooIi11iI1i . ooo * IIII
 I1 , OO00Oo , o0O0OOO0Ooo , iiIiI , url = url . split ( '|SPLIT|' )
 name = I1
 OOooo0oOO0O = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 o00O0 = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 O0ooo0O0oo0 = '\n<item>\n<date>' + OOooo0oOO0O + '</date>\n<time>' + o00O0 + '</time>\n<name>' + I1 + '</name>\n<link>' + OO00Oo + '</link>\n<site>' + o0O0OOO0Ooo + '</site>\n<icon>' + iiIiI + '</icon>\n</item>\n'
 I1 = open ( i1iiIIiiI111 ) . read ( )
 OO00Oo = I1 . replace ( '#START OF FILE#' , '#START OF FILE#' + O0ooo0O0oo0 )
 I11II1i = open ( i1iiIIiiI111 , mode = 'w' )
 I11II1i . write ( str ( OO00Oo ) )
 I11II1i . close ( )
 if 83 - 83: IIIii1I1
 if iconimage == "None" :
  iconimage = iiiii
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 13 - 13: Oo00O0
def ooOOO0 ( name , url , iconimage ) :
 if 33 - 33: I1I1i + o0 * I11i1I / o00ooo0 - O0OOooO
 I1 , OO00Oo , o0O0OOO0Ooo , iiIiI , url = url . split ( '|SPLIT|' )
 name = I1
 OOooo0oOO0O = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 o00O0 = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 O0ooo0O0oo0 = '\n<item>\n<date>' + OOooo0oOO0O + '</date>\n<time>' + o00O0 + '</time>\n<name>' + I1 + '</name>\n<link>' + OO00Oo + '</link>\n<site>' + o0O0OOO0Ooo + '</site>\n<icon>' + iiIiI + '</icon>\n</item>\n'
 I1 = open ( i1iiIIiiI111 ) . read ( )
 OO00Oo = I1 . replace ( '#START OF FILE#' , '#START OF FILE#' + O0ooo0O0oo0 )
 I11II1i = open ( i1iiIIiiI111 , mode = 'w' )
 I11II1i . write ( str ( OO00Oo ) )
 I11II1i . close ( )
 if 54 - 54: I1I1i / o0o0OOO0o0 . I11i1I % o0
 if iconimage == "None" :
  iconimage = iiiii
  if 57 - 57: i11iIiiIii . oOo00Oo00O - o0O0 - I11i1I + IiiiI1II1I1
 if "highwebmedia" in url :
  oooO0oo0oOOOO . ok ( Oo0Ooo , '[COLOR pink]Chaturbate links are taken at the time of broadcasting. If this broadcast has ended the link will no longer play. [/COLOR]' )
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 63 - 63: IiiiI1II1I1 * o0
def ooiIi1 ( name , url , iconimage ) :
 if 74 - 74: o00ooo0 * oOo00Oo00O + IiiiI1II1I1 / IiIi1Iii1I1 / O00O0O0O0 . IiIiIi
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   if 62 - 62: Oo00O0 * O0OOooO
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 58 - 58: IiiiI1II1I1 % ooIi11iI1i
def ii1i1I1i ( ) :
 if 50 - 50: I1I1i . ooIi11iI1i
 OooOooooOOoo0 = common . _get_keyboard ( heading = "Please Set Password" )
 if ( not OooOooooOOoo0 ) :
  oooO0oo0oOOOO . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 o00OO0OOO0 = OooOooooOOoo0
 if 97 - 97: I1II1 + IiiiI1II1I1
 OooOooooOOoo0 = common . _get_keyboard ( heading = "Please Confirm Your Password" )
 if ( not OooOooooOOoo0 ) :
  oooO0oo0oOOOO . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 OO0O000 = OooOooooOOoo0
 if 37 - 37: Oo00O0 - I1II1 - ooIi11iI1i
 if not os . path . exists ( I11 ) :
  if not os . path . exists ( i1 ) :
   os . makedirs ( i1 )
  open ( I11 , 'w' )
  if 77 - 77: o0o0OOO0o0 * o00ooo0
  if o00OO0OOO0 == OO0O000 :
   oO00oOOoooO = base64 . b64encode ( o00OO0OOO0 )
   I11II1i = open ( I11 , 'w' )
   I11II1i . write ( '<password>' + str ( oO00oOOoooO ) + '</password>' )
   I11II1i . close ( )
   oooO0oo0oOOOO . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   oooO0oo0oOOOO . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
 else :
  os . remove ( I11 )
  if 46 - 46: O0OOooO - Oo00O0 - IIII * O00O0O0O0
  if o00OO0OOO0 == OO0O000 :
   oO00oOOoooO = base64 . b64encode ( o00OO0OOO0 )
   I11II1i = open ( I11 , 'w' )
   I11II1i . write ( '<password>' + str ( oO00oOOoooO ) + '</password>' )
   I11II1i . close ( )
   oooO0oo0oOOOO . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   oooO0oo0oOOOO . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
   if 34 - 34: IIII - o0 / o0o0OOO0o0 + oOo00Oo00O * o0O0
def OO ( ) :
 if 97 - 97: oOo00Oo00O % oOo00Oo00O % I11i1I / o0 - o00ooo0
 try :
  os . remove ( I11 )
  oooO0oo0oOOOO . ok ( Oo0Ooo , 'Parental controls have been disabled.' )
  xbmc . executebuiltin ( "Container.Refresh" )
 except :
  oooO0oo0oOOOO . ok ( Oo0Ooo , 'There was an error disabling the parental controls.' )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 69 - 69: I1I1i
def ii1I1 ( ) :
 if 93 - 93: I1II1 % IiIi1Iii1I1 . o0o0OOO0o0 / O0OOooO - I1I1i / O0OOooO
 II1IiiIi1i = 0
 if 29 - 29: O0OOooO % O0OOooO
 try :
  common . open_url ( "http://www.google.com" )
 except :
  oooO0oo0oOOOO . ok ( Oo0Ooo , '[COLOR orangered]Error: It appears you do not currently have an active internet connection. This will cause false positives in the test. Please try again with an active internet connection.[/COLOR]' )
  return
  if 94 - 94: o00ooo0 / IiIiIi % o0 * o0 * O00O0O0O0
 O0oO . create ( Oo0Ooo , "Checking for repository updates" , '' , 'Please Wait...' )
 O0oO . update ( 0 )
 I1 = open ( oo ) . read ( )
 OO00Oo = I1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0OOO0OOoO0O = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO00Oo ) )
 for O00Oo000ooO0 in O0OOO0OOoO0O :
  O0oO . update ( 25 )
  IIiIiI = float ( O00Oo000ooO0 ) + 0.01
  oO0OOoo0OO = i1I111I + str ( IIiIiI ) + '.zip'
  try :
   OOO = common . open_url ( oO0OOoo0OO )
   if "Not Found" not in OOO :
    OO0OoO0o00 = 1
    O0oO . update ( 75 )
    IIiI1i1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( IIiI1i1i ) :
     os . makedirs ( IIiI1i1i )
    O00Oo0 = os . path . join ( IIiI1i1i , 'repoupdate.zip' )
    try : os . remove ( O00Oo0 )
    except : pass
    O0oO . update ( 100 )
    O0oO . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( oO0OOoo0OO , O00Oo0 , O0oO )
    IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    O0oO . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( O00Oo0 , IiII111i1i11 , O0oO )
    try : os . remove ( O00Oo0 )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    II1IiiIi1i = 1
    oooO0oo0oOOOO . ok ( Oo0Ooo , "ECHO XXX repository was updated to " + str ( IIiIiI ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 40 - 40: IIIii1I1 * ooo * i11iIiiIii
 O0oO . update ( 75 , "Checking for addon updates" )
 I1 = open ( ooO0O ) . read ( )
 OO00Oo = I1 . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 O0OOO0OOoO0O = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( OO00Oo ) )
 for O00Oo000ooO0 in O0OOO0OOoO0O :
  IIiIiI = float ( O00Oo000ooO0 ) + 0.01
  oO0OOoo0OO = iii11iII + str ( IIiIiI ) + '.zip'
  try :
   OOO = common . open_url ( oO0OOoo0OO )
   if "Not Found" not in OOO :
    OO0OoO0o00 = 1
    O0oO . update ( 75 )
    IIiI1i1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( IIiI1i1i ) :
     os . makedirs ( IIiI1i1i )
    O00Oo0 = os . path . join ( IIiI1i1i , 'xxx_o_dus_update.zip' )
    try : os . remove ( O00Oo0 )
    except : pass
    O0oO . update ( 100 )
    O0oO . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( oO0OOoo0OO , O00Oo0 , O0oO )
    IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    O0oO . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( O00Oo0 , IiII111i1i11 , O0oO )
    try : os . remove ( O00Oo0 )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    O0oO . update ( 100 )
    O0oO . close
    II1IiiIi1i = 1
    oooO0oo0oOOOO . ok ( Oo0Ooo , "XXX-O-DUS was updated to " + str ( IIiIiI ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 57 - 57: IIIii1I1
 if O0oO . iscanceled ( ) :
  O0oO . close ( )
  if 29 - 29: IiiiI1II1I1 - ooo * Oo00O0 + Oo00O0 . O00O0O0O0 + Oo00O0
 return II1IiiIi1i
 if 74 - 74: o0O0 - ooo / o0 * I1II1 - o0o0OOO0o0
def iiii1 ( url ) :
 if 96 - 96: i11iIiiIii % o0o0OOO0o0
 I11II1i = open ( url , mode = 'r' ) ; IIIII = I11II1i . read ( ) ; I11II1i . close ( )
 common . TextBoxes ( "%s" % IIIII )
 if 70 - 70: o00ooo0
 if url == oo0o0O00 :
  return
  if 31 - 31: ooo - O0OOooO % o00ooo0
def oooo0OOOO ( ) :
 if 54 - 54: IiIi1Iii1I1 / ooo % II . IIII
 try :
  iiii1 ( oo0o0O00 )
  if 8 - 8: ooIi11iI1i . oOo00Oo00O - O0OOooO . ooIi11iI1i
  ooooooO0oo = xbmcgui . Dialog ( ) . yesno ( "[COLOR orangered][B]RESET XXX-O-DUS?[/B][/COLOR]" , '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]' , '' , yeslabel = '[COLOR green]YES[/COLOR]' , nolabel = '[COLOR orangered]NO[/COLOR]' )
  if ooooooO0oo == 1 :
   Ii11Ii1I = plugintools . get_setting ( "download_location" )
   o0OIiII = xbmc . translatePath ( Ii11Ii1I )
   if 12 - 12: I1II1 - ooIi11iI1i
   OOOO0oo0 = [ '.mp4' ]
   if 81 - 81: IiiiI1II1I1 - IiiiI1II1I1 . o0
   for file in os . listdir ( o0OIiII ) :
    for I1i1Iiiii in OOOO0oo0 :
     if file . endswith ( I1i1Iiiii ) :
      try :
       IIiI1i1i = xbmc . translatePath ( os . path . join ( o0OIiII , file ) )
       os . remove ( IIiI1i1i )
      except :
       oooO0oo0oOOOO . ok ( Oo0Ooo , "[COLOR white]There was an error deleting " + file + "[/COLOR]" )
       pass
   try :
    shutil . rmtree ( oOOoo00O0O )
   except :
    oooO0oo0oOOOO . ok ( Oo0Ooo , "[COLOR white]There was an error deleting deleting the data directory.[/COLOR]" )
    pass
   oooO0oo0oOOOO . ok ( Oo0Ooo , "[COLOR white]XXX-O-DUS has been reset to the factory state.[/COLOR]" , "[COLOR white]Press OK to continue.[/COLOR]" )
   xbmc . executebuiltin ( "Container.Refresh" )
 except :
  oooO0oo0oOOOO . ok ( Oo0Ooo , "[COLOR white]Sorry, something went wrong.[/COLOR]" , "[COLOR white]Please report this issue to @EchoCoder on Twitter.[/COLOR]" )
  quit ( )
  if 73 - 73: IIII % i11iIiiIii - O0OOooO
def Ii1iI111II1I1 ( ) :
 oOOOOoOO0o = [ ]
 i1II1 = sys . argv [ 2 ]
 if len ( i1II1 ) >= 2 :
  i11i1 = sys . argv [ 2 ]
  IiiiiI1i1Iii = i11i1 . replace ( '?' , '' )
  if ( i11i1 [ len ( i11i1 ) - 1 ] == '/' ) :
   i11i1 = i11i1 [ 0 : len ( i11i1 ) - 2 ]
  oo00oO0o = IiiiiI1i1Iii . split ( '&' )
  oOOOOoOO0o = { }
  for iiii111II in range ( len ( oo00oO0o ) ) :
   I11iIiI1I1i11 = { }
   I11iIiI1I1i11 = oo00oO0o [ iiii111II ] . split ( '=' )
   if ( len ( I11iIiI1I1i11 ) ) == 2 :
    oOOOOoOO0o [ I11iIiI1I1i11 [ 0 ] ] = I11iIiI1I1i11 [ 1 ]
    if 92 - 92: oOo00Oo00O * IiIi1Iii1I1 . I11i1I / I1I1i
 return oOOOOoOO0o
 if 85 - 85: IIII
i11i1 = Ii1iI111II1I1 ( ) ; iI1i11II1i = None ; oO0OOoo0OO = None ; o0o0OoOo0O0OO = None ; ooOOO00Ooo = None ; iIi1I11I = None
try : iI1i11II1i = urllib . unquote_plus ( i11i1 [ "name" ] )
except : pass
try : oO0OOoo0OO = urllib . unquote_plus ( i11i1 [ "url" ] )
except : pass
try : o0o0OoOo0O0OO = int ( i11i1 [ "mode" ] )
except : pass
try : ooOOO00Ooo = urllib . unquote_plus ( i11i1 [ "iconimage" ] )
except : pass
try : iIi1I11I = urllib . quote_plus ( i11i1 [ "fanartimage" ] )
except : pass
if 42 - 42: o00ooo0 / I1I1i / II - Oo00O0
if o0o0OoOo0O0OO == None or oO0OOoo0OO == None or len ( oO0OOoo0OO ) < 1 : iI ( )
elif o0o0OoOo0O0OO == 1 : menus . SEARCH ( )
elif o0o0OoOo0O0OO == 2 : menus . VIDEOS ( )
elif o0o0OoOo0O0OO == 3 : menus . LIVE ( )
elif o0o0OoOo0O0OO == 4 : menus . PICTURES ( )
elif o0o0OoOo0O0OO == 5 : menus . STORIES ( )
elif o0o0OoOo0O0OO == 6 : menus . ALL ( )
elif o0o0OoOo0O0OO == 10 : xhamster . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 11 : xhamster . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 12 : xhamster . SEARCH ( )
elif o0o0OoOo0O0OO == 13 : xhamster . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 20 : chaturbate . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 21 : chaturbate . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 22 : chaturbate . SEARCH ( )
elif o0o0OoOo0O0OO == 23 : chaturbate . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 30 : xnxx . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 31 : xnxx . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 32 : xnxx . SEARCH ( )
elif o0o0OoOo0O0OO == 33 : xnxx . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 34 : xnxx . PICTURE_MENU ( )
elif o0o0OoOo0O0OO == 35 : xnxx . PICTURE_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 36 : xnxx . SCRAPE_GALLERY ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 37 : xnxx . DISPLAY_PICTURE ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 38 : xnxx . STORY_MENU ( )
elif o0o0OoOo0O0OO == 39 : xnxx . LIST_STORIES ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 40 : xnxx . DISPLAY_STORY ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 41 : redtube . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 42 : redtube . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 43 : redtube . SEARCH ( )
elif o0o0OoOo0O0OO == 44 : redtube . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 50 : pornhd . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 51 : pornhd . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 52 : pornhd . SEARCH ( )
elif o0o0OoOo0O0OO == 53 : pornhd . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 60 : porncom . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 61 : porncom . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 62 : porncom . SEARCH ( )
elif o0o0OoOo0O0OO == 63 : porncom . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 70 : youporn . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 71 : youporn . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 72 : youporn . SEARCH ( )
elif o0o0OoOo0O0OO == 73 : youporn . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 80 : pornfun . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 81 : pornfun . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 82 : pornfun . SEARCH ( )
elif o0o0OoOo0O0OO == 83 : pornfun . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 90 : motherless . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 91 : motherless . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 92 : motherless . DISPLAY_PICTURE ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 100 : O0o0O00Oo0o0 ( ) ;
elif o0o0OoOo0O0OO == 101 : o0O00oOoOO ( )
elif o0o0OoOo0O0OO == 102 : Ii ( )
elif o0o0OoOo0O0OO == 103 : o0O0Oooo0O ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 104 : ooO0oOOooOo0 ( )
elif o0o0OoOo0O0OO == 105 : ii ( )
elif o0o0OoOo0O0OO == 106 : plugintools . open_settings_dialog ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
elif o0o0OoOo0O0OO == 107 : oo000o ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 200 : spankbang . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 201 : spankbang . SUB_MENU ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 202 : spankbang . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 203 : spankbang . SEARCH ( )
elif o0o0OoOo0O0OO == 204 : spankbang . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 210 : porn00 . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 211 : porn00 . GET_CONTENT ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 212 : porn00 . SEARCH ( )
elif o0o0OoOo0O0OO == 213 : porn00 . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 220 : virtualpornstars . MAIN_MENU ( )
elif o0o0OoOo0O0OO == 221 : virtualpornstars . GET_CONTENT ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 222 : virtualpornstars . SEARCH ( )
elif o0o0OoOo0O0OO == 223 : virtualpornstars . PLAY_URL ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 800 : ooOOO0 ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 900 : iiIii ( )
elif o0o0OoOo0O0OO == 901 : ii1i1I1i ( )
elif o0o0OoOo0O0OO == 902 : OO ( )
elif o0o0OoOo0O0OO == 995 : common . GET_M3U_LIST ( oO0OOoo0OO )
elif o0o0OoOo0O0OO == 996 : ooiIi1 ( iI1i11II1i , oO0OOoo0OO , ooOOO00Ooo )
elif o0o0OoOo0O0OO == 997 : oooo0OOOO ( )
elif o0o0OoOo0O0OO == 998 : iiii1 ( oO0OOoo0OO )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
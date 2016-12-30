import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , shutil
import base64 , time , datetime
from resources . lib . modules import plugintools
from resources . lib . modules import common
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
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xxx-o-dus'
Oo0Ooo = '[COLOR red]XXX-O-DUS[/COLOR]'
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
OOoO00o = xbmc . translatePath ( os . path . join ( IIIII , 'resources/reset.txt' ) )
II111iiii = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'agreed.txt' ) )
IIoOoOo00oOo = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'history.xml' ) )
Ooo00O00O0O0O = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'favourites.xml' ) )
OooO0OO = xbmc . translatePath ( os . path . join ( IiII1I1i1i1ii , 'downloads.xml' ) )
if 28 - 28: iIii1
oOOoO0 = xbmc . translatePath ( 'special://home/addons/' + OO0o + '/addon.xml' )
O0OoO000O0OO = xbmc . translatePath ( 'special://home/addons/repository.xxxecho/addon.xml' )
iiI1IiI = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9wbHVnaW4udmlkZW8ueHh4LW8tZHVzL3BsdWdpbi52aWRlby54eHgtby1kdXMt' )
IIooOoOoo0O = base64 . b64decode ( b'aHR0cHM6Ly9naXRodWIuY29tL2VjaG9jb2RlcmtvZGkvcmVwb3NpdG9yeS54eHhlY2hvL3Jhdy9tYXN0ZXIvemlwcy9yZXBvc2l0b3J5Lnh4eGVjaG8vcmVwb3NpdG9yeS54eHhlY2hvLQ==' )
if 76 - 76: i1II1I11 / i1I / OO0oOoo / oo0Oo00Oo0 % oOOO00o
O0O00o0OOO0 = plugintools . get_setting ( "update_setting" )
if 27 - 27: IIII % o0O0 . ii1I11II1ii1i % I1i1iii - IiiI11Iiiii / O0oo0OO0
def I1I1i ( ) :
 if 87 - 87: i1I * II1Iiii1111i + O0oo0OO0
 if not os . path . exists ( II111iiii ) :
  I1IiIii = open ( iiiI11 , mode = 'r' ) ; oo0O0oOOO00oO = I1IiIii . read ( ) ; I1IiIii . close ( )
  common . TextBoxes ( "%s" % oo0O0oOOO00oO )
  OooOooooOOoo0 = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Do you agree to the terms and conditions of this addon?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[COLOR red]NO[/COLOR]' )
  if OooOooooOOoo0 == 1 :
   I1IiIii = open ( OOooO , mode = 'r' ) ; oo0O0oOOO00oO = I1IiIii . read ( ) ; I1IiIii . close ( )
   common . TextBoxes ( "%s" % oo0O0oOOO00oO )
   Ooo . ok ( Oo0Ooo , "[COLOR pink]We can see this is the first time you have used XXX-O-DUS. The next prompt is important as it will allow you to enable the history section of the addon and it will also allow you to select the location you would like to be used to download videos.[/COLOR]" )
   plugintools . open_settings_dialog ( )
   open ( II111iiii , 'w' )
  else :
   sys . exit ( 0 )
   if 71 - 71: I1i1iii % OO0oOoo % oo0Oo00Oo0
 if not os . path . exists ( oo ) :
  OooOooooOOoo0 = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , "[COLOR white]Would you like to enable the parental controls now?[/COLOR]" , "" , yeslabel = '[COLOR red]NO[/COLOR]' , nolabel = '[COLOR lime]YES[/COLOR]' )
  if OooOooooOOoo0 == 0 :
   oO00ooo0 ( )
  else :
   os . makedirs ( oo )
   if 57 - 57: oo0Oo00Oo0 . oo0Oo00Oo0
 elif os . path . exists ( O0OoOoo00o ) :
  OooOooo = common . _get_keyboard ( heading = "Please Enter Your Password" )
  if ( not OooOooo ) :
   Ooo . ok ( Oo0Ooo , "Sorry, no password was entered." )
   sys . exit ( 0 )
  O000oo0O = OooOooo
  if 66 - 66: i1I / iIii1 - II . oo0Oo00Oo0 / II * oo0Oo00Oo0
  IIIii1II1II = open ( O0OoOoo00o , "r" )
  i1I1iI = re . compile ( r'<password>(.+?)</password>' )
  for oo0OooOOo0 in IIIii1II1II :
   file = i1I1iI . findall ( oo0OooOOo0 )
   for o0OO00oO in file :
    I11i1I1I = base64 . b64decode ( o0OO00oO )
    if not I11i1I1I == O000oo0O :
     if not o0OO00oO == O000oo0O :
      Ooo . ok ( Oo0Ooo , "Sorry, the password you entered was incorrect." )
      sys . exit ( 0 )
      if 83 - 83: i1I / IiiI11Iiiii
 iIIIIii1 = plugintools . get_setting ( "download_location" )
 oo000OO00Oo = xbmc . translatePath ( iIIIIii1 )
 if not os . path . exists ( oo000OO00Oo ) :
  os . makedirs ( oo000OO00Oo )
  if 51 - 51: ii1I11II1ii1i * i1II1I11 + oOOO00o + II1Iiii1111i
 if not os . path . isfile ( IIoOoOo00oOo ) :
  I1IiIii = open ( IIoOoOo00oOo , 'w' )
  I1IiIii . write ( '#START OF FILE#' )
  I1IiIii . close ( )
 if not os . path . isfile ( Ooo00O00O0O0O ) :
  I1IiIii = open ( Ooo00O00O0O0O , 'w' )
  I1IiIii . write ( '#START OF FILE#' )
  I1IiIii . close ( )
 if not os . path . isfile ( OooO0OO ) :
  I1IiIii = open ( OooO0OO , 'w' )
  I1IiIii . write ( '#START OF FILE#' )
  I1IiIii . close ( )
  if 66 - 66: iIii1
 if O0O00o0OOO0 == "true" :
  oO000Oo000 = i111IiI1I ( )
 else : oO000Oo000 = 0
 if 70 - 70: IIII . O0OOo / i1II1I11 . IIII - iii1I1I / ii1I11II1ii1i
 ooOooo000oOO = open ( oOOoO0 ) . read ( )
 Oo0oOOo = ooOooo000oOO . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 Oo0OoO00oOO0o = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( Oo0oOOo ) )
 for OOO00O in Oo0OoO00oOO0o :
  OOoOO0oo0ooO = float ( OOO00O )
 ooOooo000oOO = open ( O0OoO000O0OO ) . read ( )
 Oo0oOOo = ooOooo000oOO . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 Oo0OoO00oOO0o = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( Oo0oOOo ) )
 for OOO00O in Oo0OoO00oOO0o :
  O0o0O00Oo0o0 = float ( OOO00O )
  if 87 - 87: IiiI11Iiiii * O0OOo % i11iIiiIii % iIii1 - oo0Oo00Oo0
 common . addDir ( "[COLOR white]SEARCH ALL WESBITES[/COLOR]" , "url" , 100 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR pink]Xhamster.com[/COLOR]" , OoI1Ii11I1Ii1i , 10 , ooo0OO , II1 )
 common . addDir ( "[COLOR pink]Chaturbate.com[/COLOR]" , OoI1Ii11I1Ii1i , 20 , O00ooooo00 , I1IiiI )
 common . addDir ( "[COLOR pink]XNXX.com[/COLOR]" , OoI1Ii11I1Ii1i , 30 , IIi1IiiiI1Ii , I11i11Ii )
 common . addDir ( "[COLOR pink]RedTube.com[/COLOR]" , OoI1Ii11I1Ii1i , 41 , oO00oOo , OOOo0 )
 common . addDir ( "[COLOR pink]PornHD.com[/COLOR]" , OoI1Ii11I1Ii1i , 50 , Oooo000o , IiIi11iIIi1Ii )
 common . addDir ( "[COLOR pink]Porn.com[/COLOR]" , OoI1Ii11I1Ii1i , 60 , Oo0O , IiI )
 common . addDir ( "[COLOR pink]YouPorn.com[/COLOR]" , OoI1Ii11I1Ii1i , 70 , ooOo , Oo )
 common . addDir ( "[COLOR pink]PornFun.com[/COLOR]" , OoI1Ii11I1Ii1i , 80 , o0O , IiiIII111iI )
 common . addDir ( "[COLOR deeppink]Your History[/COLOR]" , OoI1Ii11I1Ii1i , 101 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Favourites[/COLOR]" , OoI1Ii11I1Ii1i , 102 , iiiii , O0O0OO0O0O0 )
 common . addDir ( "[COLOR deeppink]Your Downloads[/COLOR]" , OoI1Ii11I1Ii1i , 105 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Your Settings[/COLOR]" , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
 if 68 - 68: I1i1iii % Oo0ooO0oo0oO . ii1I11II1ii1i . i1I
 if not os . path . exists ( O0OoOoo00o ) :
  common . addDir ( "[COLOR red]PARENTAL CONTROLS - [COLOR red]OFF[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 else :
  common . addDir ( "[COLOR red]PARENTAL CONTROLS - [COLOR lime]ON[/COLOR][/COLOR]" , "url" , 900 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]#####################################[/COLOR]" , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR pink]Twitter Support: [/COLOR][COLOR white]@EchoCoder[/COLOR]" , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Disclaimer[/COLOR]" , iiiI11 , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR white]View Addon Information[/COLOR]" , OOooO , 998 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR red]RESET XXX-O-DUS[/COLOR]" , 'url' , 997 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Addon Version:[/COLOR] [COLOR white]" + str ( OOoOO0oo0ooO ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( "[COLOR deeppink]Repository Version:[/COLOR] [COLOR white]" + str ( O0o0O00Oo0o0 ) + "[/COLOR]" , 'url' , 999 , iiiii , O0O0OO0O0O0 )
 if 92 - 92: o0O0 . I1i1iii
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 31 - 31: I1i1iii . iIii1 / iii1I1I
 if oO000Oo000 == 1 :
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 89 - 89: iIii1
def OO0oOoOO0oOO0 ( ) :
 if 86 - 86: oo0Oo00Oo0
 OOoo0O = ''
 Oo0ooOo0o = xbmc . Keyboard ( OOoo0O , 'Enter Search Term' )
 Oo0ooOo0o . doModal ( )
 if Oo0ooOo0o . isConfirmed ( ) :
  Ii1i1 = Oo0ooOo0o . getText ( )
  iiIii = Ii1i1
  OOoo0O = Ii1i1 . replace ( ' ' , '+' )
  if len ( OOoo0O ) > 1 :
   try :
    o0oOoO00o . create ( Oo0Ooo , '[COLOR white]Searching: [/COLOR] [COLOR red]YouPorn[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]1 of 7[/COLOR]' )
    ooo0O = "http://www.youporn.com/search/?query=" + OOoo0O . lower ( )
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 15 )
    try :
     youporn . GET_CONTENT ( ooo0O )
    except : pass
    ooo0O = "http://www.xnxx.com/?k=" + OOoo0O . lower ( )
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 30 , '[COLOR white]Searching: [/COLOR] [COLOR red]XNXX[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]2 of 7[/COLOR]' )
    try :
     xnxx . GET_CONTENT ( ooo0O )
    except : pass
    ooo0O = "https://xhamster.com/search.php?from=&new=&q=" + OOoo0O . lower ( ) + "&qcat=video"
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 45 , '[COLOR white]Searching: [/COLOR] [COLOR red]Xhamster[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]3 of 7[/COLOR]' )
    try :
     xhamster . GET_CONTENT ( ooo0O )
    except : pass
    ooo0O = "http://www.pornhd.com/search?search=" + OOoo0O . lower ( )
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 60 , '[COLOR white]Searching: [/COLOR] [COLOR red]PornHD[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]4 of 7[/COLOR]' )
    try :
     pornhd . GET_CONTENT ( ooo0O )
    except : pass
    ooo0O = "http://www.porn.com/videos/search?q=" + OOoo0O . lower ( )
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 75 , '[COLOR white]Searching: [/COLOR] [COLOR red]Porn.com[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]5 of 7[/COLOR]' )
    try :
     porncom . GET_CONTENT ( ooo0O )
    except : pass
    ooo0O = "http://www.redtube.com/?search=" + OOoo0O . lower ( )
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 90 , '[COLOR white]Searching: [/COLOR] [COLOR red]RedTube[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]6 of 7[/COLOR]' )
    try :
     redtube . GET_CONTENT ( ooo0O )
    except : pass
    ooo0O = "http://pornfun.com/search/?q=" + OOoo0O . lower ( )
    ooo0O = 'split|' + ooo0O
    o0oOoO00o . update ( 95 , '[COLOR white]Searching: [/COLOR] [COLOR red]PornFun[/COLOR]' , '[COLOR white]Term: [/COLOR][COLOR deeppink]' + iiIii . lower ( ) + '[/COLOR]' , '[COLOR white]Source: [/COLOR][COLOR pink]7 of 7[/COLOR]' )
    try :
     pornfun . GET_CONTENT ( ooo0O )
    except : pass
    o0oOoO00o . close ( )
   except :
    Ooo . ok ( Oo0Ooo , '[COLOR pink]Sorry, there was an error searching for ' + OOoo0O . lower ( ) + ' please try again later.[/COLOR]' )
    quit ( )
  else : quit ( )
  if 75 - 75: i1II1I11 % i1II1I11 . I1i1iii
def III1iII1I1ii ( ) :
 if 61 - 61: I1i1iI1i
 O0OOO = 0
 if not os . path . exists ( O0OoOoo00o ) :
  O0OOO = 1
  common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR red]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
 else :
  IIIii1II1II = open ( O0OoOoo00o , "r" )
  i1I1iI = re . compile ( r'<password>(.+?)</password>' )
  for oo0OooOOo0 in IIIii1II1II :
   file = i1I1iI . findall ( oo0OooOOo0 )
   for o0OO00oO in file :
    I11i1I1I = base64 . b64decode ( o0OO00oO )
    O0OOO = 1
    common . addLink ( "[COLOR deeppink]PARENTAL CONTROLS - [/COLOR][COLOR lime]ON[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR white]Current Password - [/COLOR][COLOR orangered]" + str ( I11i1I1I ) + "[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR lime]Change Password[/COLOR]" , "url" , 901 , iiiii , O0O0OO0O0O0 )
    common . addLink ( "[COLOR red]Disable Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
    if 10 - 10: oo0Oo00Oo0 * oOOO00o % iIii1 / II / iIii1
 if O0OOO == 0 :
  common . addLink ( "[COLOR rose]PARENTAL CONTROLS - [/COLOR][COLOR red]OFF[/COLOR]" , "url" , 999 , iiiii , O0O0OO0O0O0 )
  common . addLink ( "[COLOR white]Setup Parental Password[/COLOR]" , "url" , 902 , iiiii , O0O0OO0O0O0 )
  if 42 - 42: II1Iiii1111i
def o0o ( ) :
 if 84 - 84: iii1I1I
 OOOooOO0 = plugintools . get_setting ( "history_setting" )
 if 87 - 87: OO0oOoo * i1I + oo0Oo00Oo0 / O00oOoOoO0o0O / o0O0
 if OOOooOO0 == "true" :
  common . addLink ( '[COLOR deeppink]Clear History[/COLOR]' , OoI1Ii11I1Ii1i , 104 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR red]Disable History[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '###########################################' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
  if 37 - 37: o0O0 - IiiI11Iiiii * OO0oOoo % i11iIiiIii - I1i1iii
  I1IiIii = open ( IIoOoOo00oOo , mode = 'r' ) ; oo0O0oOOO00oO = I1IiIii . read ( ) ; I1IiIii . close ( )
  oo0O0oOOO00oO = oo0O0oOOO00oO . replace ( '\n' , '' )
  Oo0OoO00oOO0o = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0O0oOOO00oO )
  for OOO00O in Oo0OoO00oOO0o :
   o0oO = re . compile ( '<date>(.+?)</date>' ) . findall ( OOO00O ) [ 0 ]
   time = re . compile ( '<time>(.+?)</time>' ) . findall ( OOO00O ) [ 0 ]
   IIiIi1iI = re . compile ( '<name>(.+?)</name>' ) . findall ( OOO00O ) [ 0 ]
   ooo0O = re . compile ( '<link>(.+?)</link>' ) . findall ( OOO00O ) [ 0 ]
   i1IiiiI1iI = re . compile ( '<site>(.+?)</site>' ) . findall ( OOO00O ) [ 0 ]
   i1iIi = re . compile ( '<icon>(.+?)</icon>' ) . findall ( OOO00O ) [ 0 ]
   ooo0O = IIiIi1iI + '|SPLIT|' + ooo0O + '|SPLIT|' + i1IiiiI1iI + '|SPLIT|' + i1iIi + '|SPLIT|' + ooo0O
   if 68 - 68: i11iIiiIii % i1I + i11iIiiIii
   common . addLink ( '[COLOR pink]' + o0oO + ' | ' + '[/COLOR][COLOR deeppink]' + time + '[/COLOR] - [COLOR red]' + i1IiiiI1iI + '[/COLOR][COLOR pink] - ' + IIiIi1iI + '[/COLOR]' , ooo0O , 800 , i1iIi , O0O0OO0O0O0 )
 else :
  common . addLink ( '[COLOR red]Enable History Monitoring[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '############################################' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  common . addLink ( '[COLOR pink]History monitoring is currently disabled.[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
  if 31 - 31: I1i1iI1i . II
def II1I ( ) :
 if 84 - 84: ii1I11II1ii1i . i11iIiiIii . ii1I11II1ii1i * i1I - oOOO00o
 common . addLink ( '[COLOR deeppink]Your Favourites[/COLOR]' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 if 42 - 42: i11iIiiIii
 I1IiIii = open ( Ooo00O00O0O0O , mode = 'r' ) ; oo0O0oOOO00oO = I1IiIii . read ( ) ; I1IiIii . close ( )
 oo0O0oOOO00oO = oo0O0oOOO00oO . replace ( '\n' , '' )
 Oo0OoO00oOO0o = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0O0oOOO00oO )
 for OOO00O in Oo0OoO00oOO0o :
  IIiIi1iI = re . compile ( '<name>(.+?)</name>' ) . findall ( OOO00O ) [ 0 ]
  ooo0O = re . compile ( '<link>(.+?)</link>' ) . findall ( OOO00O ) [ 0 ]
  i1IiiiI1iI = re . compile ( '<site>(.+?)</site>' ) . findall ( OOO00O ) [ 0 ]
  i1iIi = re . compile ( '<icon>(.+?)</icon>' ) . findall ( OOO00O ) [ 0 ]
  ooo0O = IIiIi1iI + '|SPLIT|' + ooo0O + '|SPLIT|' + i1IiiiI1iI + '|SPLIT|' + i1iIi + '|SPLIT|' + ooo0O
  common . addLink ( '[COLOR red]' + i1IiiiI1iI + '[/COLOR][COLOR pink] - ' + IIiIi1iI + '[/COLOR]' , ooo0O , 103 , i1iIi , O0O0OO0O0O0 )
  if 33 - 33: o0O0 - iii1I1I * Oo0ooO0oo0oO * i1II1I11 - O0OOo
def iiIiI ( name , url , iconimage ) :
 if 91 - 91: o0O0 % Oo0ooO0oo0oO % O00oOoOoO0o0O
 IIi1I11I1II = url
 ooOooo000oOO , Oo0oOOo , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 if 81 - 81: iIii1 / iii1I1I . ii1I11II1ii1i . II
 OOoo0O = '\n<item>\n<name>' + ooOooo000oOO + '</name>\n<link>' + Oo0oOOo + '</link>\n<site>' + OooOoooOo + '</site>\n<icon>' + ii11IIII11I + '</icon>\n</item>\n'
 if 72 - 72: Oo0ooO0oo0oO / II1Iiii1111i + O0oo0OO0 - O0OOo
 OooOooooOOoo0 = Ooo . select ( "[COLOR red][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Remove from Favourites[/B][/COLOR]' ] )
 if 29 - 29: i1I + OO0oOoo % iii1I1I
 if OooOooooOOoo0 == 0 :
  I1I11 ( name , IIi1I11I1II , iconimage )
 else :
  II1o0oO00000 = open ( Ooo00O00O0O0O ) . read ( )
  I1IiIii = II1o0oO00000 . replace ( OOoo0O , '\n' )
  OOOOoo0Oo = open ( Ooo00O00O0O0O , mode = 'w' )
  OOOOoo0Oo . write ( str ( I1IiIii ) )
  OOOOoo0Oo . close ( )
  xbmc . executebuiltin ( "Container.Refresh" )
  quit ( )
  if 14 - 14: o0O0
def I1iI1iIi111i ( name , url , iconimage ) :
 if 44 - 44: Oo0ooO0oo0oO % I1i1iI1i + oOOO00o
 IIi1I11I1II = url
 ooOooo000oOO , Oo0oOOo , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 if 45 - 45: o0O0 / o0O0 + I1i1iii + IiiI11Iiiii
 OooOooooOOoo0 = Ooo . select ( "[COLOR red][B]Please select an option[/B][/COLOR]" , [ '[COLOR pink][B]Watch Video[/B][/COLOR]' , '[COLOR pink][B]Delete Download[/B][/COLOR]' ] )
 if 47 - 47: i1II1I11 + IiiI11Iiiii
 if OooOooooOOoo0 == 0 :
  I1I11 ( name , IIi1I11I1II , iconimage )
 else :
  os . remove ( url )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 82 - 82: I1i1iI1i . ii1I11II1ii1i - O00oOoOoO0o0O - ii1I11II1ii1i * I1i1iI1i
def ooO0oOOooOo0 ( ) :
 if 38 - 38: I1i1iii
 if os . path . isfile ( IIoOoOo00oOo ) :
  OooOooooOOoo0 = xbmcgui . Dialog ( ) . yesno ( Oo0Ooo , '[COLOR white]Would you like to clear all stored history?[/COLOR]' , '' , yeslabel = '[COLOR lime]YES[/COLOR]' , nolabel = '[B][COLOR red]NO[/COLOR][/B]' )
  if OooOooooOOoo0 == 1 :
   os . remove ( IIoOoOo00oOo )
   I1IiIii = open ( IIoOoOo00oOo , 'w' )
   I1IiIii . write ( '#START OF FILE#' )
   I1IiIii . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 84 - 84: O00oOoOoO0o0O % o0O0 / O00oOoOoO0o0O % oOOO00o
def ii ( ) :
 if 84 - 84: i1II1I11 % I1i1iI1i . i11iIiiIii / II1Iiii1111i
 iIIIIii1 = plugintools . get_setting ( "download_location" )
 o0OIiII = xbmc . translatePath ( iIIIIii1 )
 common . addLink ( '[COLOR deeppink]Download Location: [/COLOR]' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( o0OIiII , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '[COLOR red]Change Download Location[/COLOR]' , OoI1Ii11I1Ii1i , 106 , iiiii , O0O0OO0O0O0 )
 common . addLink ( '###########################################' , OoI1Ii11I1Ii1i , 999 , iiiii , O0O0OO0O0O0 )
 if 25 - 25: iii1I1I - iii1I1I * i1II1I11
 OOOO0oo0 = [ '.mp4' ]
 if 35 - 35: IIII - II % i1II1I11 . O0oo0OO0 % IIII
 for file in os . listdir ( o0OIiII ) :
  for I1i1Iiiii in OOOO0oo0 :
   if file . endswith ( I1i1Iiiii ) :
    i1iIi = iiiii
    I1IiIii = open ( OooO0OO , mode = 'r' ) ; oo0O0oOOO00oO = I1IiIii . read ( ) ; I1IiIii . close ( )
    oo0O0oOOO00oO = oo0O0oOOO00oO . replace ( '\n' , '' )
    Oo0OoO00oOO0o = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0O0oOOO00oO )
    for OOO00O in Oo0OoO00oOO0o :
     IIiIi1iI = re . compile ( '<name>(.+?)</name>' ) . findall ( OOO00O ) [ 0 ]
     OOo0oO00ooO00 = re . compile ( '<icon>(.+?)</icon>' ) . findall ( OOO00O ) [ 0 ]
     if file in IIiIi1iI :
      i1iIi = OOo0oO00ooO00
    ooo0O = xbmc . translatePath ( os . path . join ( o0OIiII , file ) )
    if "http" in i1iIi :
     oOO0O00oO0Ooo = file + '|SPLIT|' + ooo0O + '|SPLIT|Downloaded|SPLIT|' + i1iIi + '|SPLIT|' + ooo0O
    else :
     oOO0O00oO0Ooo = file + '|SPLIT|' + ooo0O + '|SPLIT|Downloaded|SPLIT|None|SPLIT|' + ooo0O
    common . addLink ( '[COLOR pink]' + file + '[/COLOR]' , oOO0O00oO0Ooo , 107 , i1iIi , O0O0OO0O0O0 )
    if 67 - 67: II1Iiii1111i - oo0Oo00Oo0
def iI1i11iII111 ( ) :
 if 15 - 15: i11iIiiIii % IIII . O0OOo + i1I
 iIIIIii1 = plugintools . get_setting ( "download_location" )
 OO0OOOOoo0OOO = Ooo . browse ( 3 , Oo0Ooo , 'files' , '' , False , False , i1IIi11111i )
 II1o0oO00000 = open ( o000o0o00o0Oo ) . read ( )
 I1IiIii = II1o0oO00000 . replace ( iIIIIii1 , OO0OOOOoo0OOO )
 OOOOoo0Oo = open ( o000o0o00o0Oo , mode = 'w' )
 OOOOoo0Oo . write ( str ( I1IiIii ) )
 OOOOoo0Oo . close ( )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 27 - 27: IiiI11Iiiii + I1i1iI1i
def o0Oo00 ( name , url , iconimage ) :
 if 32 - 32: i1II1I11 . ii1I11II1ii1i * oOOO00o
 ooOooo000oOO , Oo0oOOo , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 name = ooOooo000oOO
 OOooo0oOO0O = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 o00O0 = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 OOoo0O = '\n<item>\n<date>' + OOooo0oOO0O + '</date>\n<time>' + o00O0 + '</time>\n<name>' + ooOooo000oOO + '</name>\n<link>' + Oo0oOOo + '</link>\n<site>' + OooOoooOo + '</site>\n<icon>' + ii11IIII11I + '</icon>\n</item>\n'
 ooOooo000oOO = open ( IIoOoOo00oOo ) . read ( )
 Oo0oOOo = ooOooo000oOO . replace ( '#START OF FILE#' , '#START OF FILE#' + OOoo0O )
 I1IiIii = open ( IIoOoOo00oOo , mode = 'w' )
 I1IiIii . write ( str ( Oo0oOOo ) )
 I1IiIii . close ( )
 if 83 - 83: IiiI11Iiiii
 if iconimage == "None" :
  iconimage = iiiii
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 13 - 13: O0oo0OO0
def I1I11 ( name , url , iconimage ) :
 if 33 - 33: I1i1iii + o0O0 * OO0oOoo / O00oOoOoO0o0O - II
 ooOooo000oOO , Oo0oOOo , OooOoooOo , ii11IIII11I , url = url . split ( '|SPLIT|' )
 name = ooOooo000oOO
 OOooo0oOO0O = datetime . datetime . now ( ) . strftime ( "%d-%m-%Y" )
 o00O0 = datetime . datetime . now ( ) . strftime ( "%H:%M" )
 OOoo0O = '\n<item>\n<date>' + OOooo0oOO0O + '</date>\n<time>' + o00O0 + '</time>\n<name>' + ooOooo000oOO + '</name>\n<link>' + Oo0oOOo + '</link>\n<site>' + OooOoooOo + '</site>\n<icon>' + ii11IIII11I + '</icon>\n</item>\n'
 ooOooo000oOO = open ( IIoOoOo00oOo ) . read ( )
 Oo0oOOo = ooOooo000oOO . replace ( '#START OF FILE#' , '#START OF FILE#' + OOoo0O )
 I1IiIii = open ( IIoOoOo00oOo , mode = 'w' )
 I1IiIii . write ( str ( Oo0oOOo ) )
 I1IiIii . close ( )
 if 54 - 54: I1i1iii / oo0Oo00Oo0 . OO0oOoo % o0O0
 if iconimage == "None" :
  iconimage = iiiii
  if 57 - 57: i11iIiiIii . i1I - IIII - OO0oOoo + iIii1
 if "highwebmedia" in url :
  Ooo . ok ( Oo0Ooo , '[COLOR pink]Chaturbate links are taken at the time of broadcasting. If this broadcast has ended the link will no longer play. [/COLOR]' )
 oO00Oo0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( url , oO00Oo0O0o , False )
 if 63 - 63: iIii1 * o0O0
def oO00ooo0 ( ) :
 if 69 - 69: iii1I1I . II1Iiii1111i
 OooOooo = common . _get_keyboard ( heading = "Please Set Password" )
 if ( not OooOooo ) :
  Ooo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 O000oo0O = OooOooo
 if 49 - 49: II - oOOO00o
 OooOooo = common . _get_keyboard ( heading = "Please Confirm Your Password" )
 if ( not OooOooo ) :
  Ooo . ok ( Oo0Ooo , "Sorry, no password was entered." )
  sys . exit ( 0 )
 OoOOoOooooOOo = OooOooo
 if 87 - 87: II
 if not os . path . exists ( O0OoOoo00o ) :
  if not os . path . exists ( oo ) :
   os . makedirs ( oo )
  open ( O0OoOoo00o , 'w' )
  if 58 - 58: iIii1 % i1II1I11
  if O000oo0O == OoOOoOooooOOo :
   i1 = base64 . b64encode ( O000oo0O )
   I1IiIii = open ( O0OoOoo00o , 'w' )
   I1IiIii . write ( '<password>' + str ( i1 ) + '</password>' )
   I1IiIii . close ( )
   Ooo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   Ooo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
 else :
  os . remove ( O0OoOoo00o )
  if 51 - 51: O0OOo / iIii1 . oo0Oo00Oo0 * i1II1I11 + II1Iiii1111i * ii1I11II1ii1i
  if O000oo0O == OoOOoOooooOOo :
   i1 = base64 . b64encode ( O000oo0O )
   I1IiIii = open ( O0OoOoo00o , 'w' )
   I1IiIii . write ( '<password>' + str ( i1 ) + '</password>' )
   I1IiIii . close ( )
   Ooo . ok ( Oo0Ooo , 'Your password has been set and parental controls have been enabled.' )
   xbmc . executebuiltin ( "Container.Refresh" )
  else :
   Ooo . ok ( Oo0Ooo , 'The passwords do not match, please try again.' )
   sys . exit ( 0 )
   if 73 - 73: II1Iiii1111i + O0oo0OO0 - iii1I1I - IIII - I1i1iI1i
def O0O ( ) :
 if 80 - 80: IIII * i1II1I11 / i1II1I11
 try :
  os . remove ( O0OoOoo00o )
  Ooo . ok ( Oo0Ooo , 'Parental controls have been disabled.' )
  xbmc . executebuiltin ( "Container.Refresh" )
 except :
  Ooo . ok ( Oo0Ooo , 'There was an error disabling the parental controls.' )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 5 - 5: II
def i111IiI1I ( ) :
 if 48 - 48: i1II1I11 - OO0oOoo / O0oo0OO0
 OO0O0 = 0
 if 30 - 30: oo0Oo00Oo0 + i1I * oOOO00o % i11iIiiIii % iIii1
 try :
  common . open_url ( "http://www.google.com" )
 except :
  Ooo . ok ( Oo0Ooo , '[COLOR red]Error: It appears you do not currently have an active internet connection. This will cause false positives in the test. Please try again with an active internet connection.[/COLOR]' )
  return
  if 97 - 97: i1I % i1I % OO0oOoo / o0O0 - O00oOoOoO0o0O
 o0oOoO00o . create ( Oo0Ooo , "Checking for repository updates" , '' , 'Please Wait...' )
 o0oOoO00o . update ( 0 )
 ooOooo000oOO = open ( O0OoO000O0OO ) . read ( )
 Oo0oOOo = ooOooo000oOO . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 Oo0OoO00oOO0o = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( Oo0oOOo ) )
 for OOO00O in Oo0OoO00oOO0o :
  o0oOoO00o . update ( 25 )
  ooooo0O0000oo = float ( OOO00O ) + 0.01
  ooo0O = IIooOoOoo0O + str ( ooooo0O0000oo ) + '.zip'
  try :
   iIii1II11 = common . open_url ( ooo0O )
   if "Not Found" not in iIii1II11 :
    O0OOO = 1
    o0oOoO00o . update ( 75 )
    OooOo0ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( OooOo0ooo ) :
     os . makedirs ( OooOo0ooo )
    o00oo0 = os . path . join ( OooOo0ooo , 'repoupdate.zip' )
    try : os . remove ( o00oo0 )
    except : pass
    o0oOoO00o . update ( 100 )
    o0oOoO00o . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( ooo0O , o00oo0 , o0oOoO00o )
    I11ii1IIiIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    o0oOoO00o . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( o00oo0 , I11ii1IIiIi , o0oOoO00o )
    try : os . remove ( o00oo0 )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    OO0O0 = 1
    Ooo . ok ( Oo0Ooo , "ECHO XXX repository was updated to " + str ( ooooo0O0000oo ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 54 - 54: O00oOoOoO0o0O % i1I - oo0Oo00Oo0 / OO0oOoo - II1Iiii1111i . oOOO00o
 o0oOoO00o . update ( 75 , "Checking for addon updates" )
 ooOooo000oOO = open ( oOOoO0 ) . read ( )
 Oo0oOOo = ooOooo000oOO . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 Oo0OoO00oOO0o = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( Oo0oOOo ) )
 for OOO00O in Oo0OoO00oOO0o :
  ooooo0O0000oo = float ( OOO00O ) + 0.01
  ooo0O = iiI1IiI + str ( ooooo0O0000oo ) + '.zip'
  try :
   iIii1II11 = common . open_url ( ooo0O )
   if "Not Found" not in iIii1II11 :
    O0OOO = 1
    o0oOoO00o . update ( 75 )
    OooOo0ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
    if not os . path . exists ( OooOo0ooo ) :
     os . makedirs ( OooOo0ooo )
    o00oo0 = os . path . join ( OooOo0ooo , 'xxx_o_dus_update.zip' )
    try : os . remove ( o00oo0 )
    except : pass
    o0oOoO00o . update ( 100 )
    o0oOoO00o . update ( 0 , "" , "Downloading Update Please Wait" , "" )
    downloader . download ( ooo0O , o00oo0 , o0oOoO00o )
    I11ii1IIiIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
    o0oOoO00o . update ( 0 , "" , "Extracting Update Please Wait" , "" )
    extract . all ( o00oo0 , I11ii1IIiIi , o0oOoO00o )
    try : os . remove ( o00oo0 )
    except : pass
    xbmc . executebuiltin ( "UpdateLocalAddons" )
    xbmc . executebuiltin ( "UpdateAddonRepos" )
    o0oOoO00o . update ( 100 )
    o0oOoO00o . close
    OO0O0 = 1
    Ooo . ok ( Oo0Ooo , "XXX-O-DUS was updated to " + str ( ooooo0O0000oo ) + ', you may need to restart the addon for changes to take effect' )
    time . sleep ( 2 )
  except : pass
  if 11 - 11: i1I . II1Iiii1111i * ii1I11II1ii1i * O0oo0OO0 + IiiI11Iiiii
 if o0oOoO00o . iscanceled ( ) :
  o0oOoO00o . close ( )
  if 33 - 33: iii1I1I * i1II1I11 - I1i1iii % I1i1iii
 return OO0O0
 if 18 - 18: I1i1iii / O0OOo * I1i1iii + I1i1iii * i11iIiiIii * i1I
def I1II1 ( url ) :
 if 86 - 86: O00oOoOoO0o0O / iIii1 . I1i1iI1i
 I1IiIii = open ( url , mode = 'r' ) ; oo0O0oOOO00oO = I1IiIii . read ( ) ; I1IiIii . close ( )
 common . TextBoxes ( "%s" % oo0O0oOOO00oO )
 if 19 - 19: i1I % O0oo0OO0 % ii1I11II1ii1i * i1II1I11 % iii1I1I
 if url == OOoO00o :
  return
  if 67 - 67: II . Oo0ooO0oo0oO
def i1i1iI1iiiI ( ) :
 if 51 - 51: II % I1i1iii . OO0oOoo / O00oOoOoO0o0O / oOOO00o . OO0oOoo
 try :
  I1II1 ( OOoO00o )
  if 42 - 42: i1II1I11 + Oo0ooO0oo0oO - IIII / ii1I11II1ii1i
  OooOooooOOoo0 = xbmcgui . Dialog ( ) . yesno ( "[COLOR red][B]RESET XXX-O-DUS?[/B][/COLOR]" , '[COLOR white]ARE YOU SURE YOU WANT TO RETURN XXX-O-DUS TO THE DEFAULT STATE AND LOSE ALL YOUR INFORMATION?[/COLOR]' , '' , yeslabel = '[COLOR green]YES[/COLOR]' , nolabel = '[COLOR red]NO[/COLOR]' )
  if OooOooooOOoo0 == 1 :
   iIIIIii1 = plugintools . get_setting ( "download_location" )
   o0OIiII = xbmc . translatePath ( iIIIIii1 )
   if 9 - 9: iii1I1I % iii1I1I - i1II1I11
   OOOO0oo0 = [ '.mp4' ]
   if 51 - 51: II . O00oOoOoO0o0O - i1I / iii1I1I
   for file in os . listdir ( o0OIiII ) :
    for I1i1Iiiii in OOOO0oo0 :
     if file . endswith ( I1i1Iiiii ) :
      try :
       OooOo0ooo = xbmc . translatePath ( os . path . join ( o0OIiII , file ) )
       os . remove ( OooOo0ooo )
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
  if 52 - 52: i1II1I11 + iii1I1I + o0O0 + O0OOo % o0O0
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
    if 50 - 50: oo0Oo00Oo0 * II % O00oOoOoO0o0O + IIII + o0O0 + II
 return Ii1iI111II1I1
 if 71 - 71: i1I * i1I * Oo0ooO0oo0oO . OO0oOoo / I1i1iii
i1II1 = OO ( ) ; ooo0O0o00O = None ; ooo0O = None ; I1i11 = None ; i1iIi = None ; IiIi1I1 = None
try : ooo0O0o00O = urllib . unquote_plus ( i1II1 [ "name" ] )
except : pass
try : ooo0O = urllib . unquote_plus ( i1II1 [ "url" ] )
except : pass
try : I1i11 = int ( i1II1 [ "mode" ] )
except : pass
try : i1iIi = urllib . unquote_plus ( i1II1 [ "iconimage" ] )
except : pass
try : IiIi1I1 = urllib . quote_plus ( i1II1 [ "fanartimage" ] )
except : pass
if 39 - 39: I1i1iI1i + iIii1 - IiiI11Iiiii . iIii1
if I1i11 == None or ooo0O == None or len ( ooo0O ) < 1 : I1I1i ( )
if 84 - 84: II1Iiii1111i + Oo0ooO0oo0oO - I1i1iI1i . i1I * O0oo0OO0 + II
elif I1i11 == 10 : xhamster . MAIN_MENU ( )
elif I1i11 == 11 : xhamster . GET_CONTENT ( ooo0O )
elif I1i11 == 12 : xhamster . SEARCH ( )
elif I1i11 == 13 : xhamster . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 20 : chaturbate . MAIN_MENU ( )
elif I1i11 == 21 : chaturbate . GET_CONTENT ( ooo0O )
elif I1i11 == 22 : chaturbate . SEARCH ( )
elif I1i11 == 23 : chaturbate . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 30 : xnxx . MAIN_MENU ( )
elif I1i11 == 31 : xnxx . GET_CONTENT ( ooo0O )
elif I1i11 == 32 : xnxx . SEARCH ( )
elif I1i11 == 33 : xnxx . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 34 : xnxx . PICTURE_MENU ( )
elif I1i11 == 35 : xnxx . PICTURE_CONTENT ( ooo0O )
elif I1i11 == 36 : xnxx . SCRAPE_GALLERY ( ooo0O )
elif I1i11 == 37 : xnxx . DISPLAY_PICTURE ( ooo0O )
elif I1i11 == 38 : xnxx . STORY_MENU ( )
elif I1i11 == 39 : xnxx . LIST_STORIES ( ooo0O )
elif I1i11 == 40 : xnxx . DISPLAY_STORY ( ooo0O )
elif I1i11 == 41 : redtube . MAIN_MENU ( )
elif I1i11 == 42 : redtube . GET_CONTENT ( ooo0O )
elif I1i11 == 43 : redtube . SEARCH ( )
elif I1i11 == 44 : redtube . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 50 : pornhd . MAIN_MENU ( )
elif I1i11 == 51 : pornhd . GET_CONTENT ( ooo0O )
elif I1i11 == 52 : pornhd . SEARCH ( )
elif I1i11 == 53 : pornhd . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 60 : porncom . MAIN_MENU ( )
elif I1i11 == 61 : porncom . GET_CONTENT ( ooo0O )
elif I1i11 == 62 : porncom . SEARCH ( )
elif I1i11 == 63 : porncom . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 70 : youporn . MAIN_MENU ( )
elif I1i11 == 71 : youporn . GET_CONTENT ( ooo0O )
elif I1i11 == 72 : youporn . SEARCH ( )
elif I1i11 == 73 : youporn . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 80 : pornfun . MAIN_MENU ( )
elif I1i11 == 81 : pornfun . GET_CONTENT ( ooo0O )
elif I1i11 == 82 : pornfun . SEARCH ( )
elif I1i11 == 83 : pornfun . PLAY_URL ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 100 : OO0oOoOO0oOO0 ( )
elif I1i11 == 101 : o0o ( )
elif I1i11 == 102 : II1I ( )
elif I1i11 == 103 : iiIiI ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 104 : ooO0oOOooOo0 ( )
elif I1i11 == 105 : ii ( )
elif I1i11 == 106 : plugintools . open_settings_dialog ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
elif I1i11 == 107 : I1iI1iIi111i ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 800 : I1I11 ( ooo0O0o00O , ooo0O , i1iIi )
elif I1i11 == 900 : III1iII1I1ii ( )
elif I1i11 == 901 : oO00ooo0 ( )
elif I1i11 == 902 : O0O ( )
elif I1i11 == 997 : i1i1iI1iiiI ( )
elif I1i11 == 998 : I1II1 ( ooo0O )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
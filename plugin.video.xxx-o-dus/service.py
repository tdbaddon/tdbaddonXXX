import xbmc,urllib,urllib2,os,re,sys,time
from resources.lib.modules  import plugintools
from resources.lib.modules  import common
from resources.lib.modules  import kodi
from resources.lib.modules  import log_utils

addon_id            = 'plugin.video.xxx-o-dus'
DATA_FOLDER         = xbmc.translatePath(os.path.join('special://profile/addon_data/', addon_id))
CHATURBATE_FILE     = xbmc.translatePath(os.path.join(DATA_FOLDER , 'chaturbate.xml'))
CHATURBATE_CACHE    = xbmc.translatePath(os.path.join(DATA_FOLDER , 'chaturbate_cache.xml'))

i = 0
j = 0
if os.path.exists(CHATURBATE_CACHE): os.remove(CHATURBATE_CACHE)
chat_on_off = 'false'
#log_utils.log('Checking for Chaturbate Monitoring Setting.', log_utils.LOGNOTICE)
chat_on_off  = plugintools.get_setting("chaturbate_setting")

if chat_on_off != 'true': 
    log_utils.log('Chaturbate Monitoring Disabled, Exiting Script.', log_utils.LOGNOTICE)
    quit()
else: time.sleep(30)

log_utils.log('Started Chaturbate Monitoring!', log_utils.LOGNOTICE)

while not xbmc.abortRequested:
    
    if not i:
        if os.path.exists(CHATURBATE_FILE):
            f = open(CHATURBATE_FILE,mode='r'); msg = f.read(); f.close()
            if not '<item>' in msg:
                log_utils.log('No Chaturbate cams found to monitor. Exciting script now.', log_utils.LOGWARNING)
                quit()
            msg = msg.replace('\n','')
            match = re.compile('<item>(.+?)</item>').findall(msg)
            for item in match:
                title=re.compile('<name>(.+?)</name>').findall(item)[0]
                link=re.compile('<url>(.+?)</url>').findall(item)[0]
                iconimage=re.compile('<icon>(.+?)</icon>').findall(item)[0]
                if not os.path.exists(CHATURBATE_CACHE): f = open(CHATURBATE_CACHE,'w'); f.write('#START OF FILE#'); f.close()
                a=open(CHATURBATE_CACHE).read()
                if not title in a:
                    try:
                        r = common.open_url(link)
                        if '.m3u8' in r:
                            kodi.notify(msg=title + ' is online!', duration=9000, sound=True, icon_path=iconimage)
                            xbmc.sleep(3500)
                            #log_utils.log(title + ' is on Chaturbate now! Notification sent.', log_utils.LOGNOTICE)
                            b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(title)+'</name>\n</item>\n')
                            f= open(CHATURBATE_CACHE, mode='w')
                            f.write(str(b))
                            f.close()
                    except: 
                        pass

    xbmc.sleep(5000)

    if i >= 2879:
        log_utils.log('Chaturbate has been monitored for 4 hours. Removing cache file.', log_utils.LOGNOTICE)
        if os.path.exists(CHATURBATE_CACHE): 
            try:
                os.remove(CHATURBATE_CACHE)
                log_utils.log('Chaturbate cahche file has been removed.', log_utils.LOGNOTICE)
            except:
                log_utils.log('Error removing Chaturbate cache file.', log_utils.LOGWARNING)
                pass
    #if i == 0:
        #log_utils.log('Checked Chaturbate for whos online. Trying again in 5 minutes.', log_utils.LOGNOTICE)
        #log_utils.log('Chaturbate Cache status is at - ' + str(j) + ' (Cache reset at 2780)', log_utils.LOGNOTICE)
    i = (i + 1) % 60
    j = (j + 1) % 2880
import xbmc,os,re
from resources.lib.modules  import common
from resources.lib.modules  import dom_parser

addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

def LIVE_CHANNELS():

    url = 'http://www.freeiptvlinks.net/category/iptv-links/adult/'
    response = common.open_url(url)

    content = dom_parser.parse_dom(response, 'div', {'class': 'entry-summary'})

    for item in content[:1]:
        list = dom_parser.parse_dom(item, 'a', ret='href')[0]

    response = common.open_url(list)
    response = response.replace('#AAASTREAM:','#A:').replace('#EXTINF:','#A:').replace('<br />','').replace('<h4>','')
    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)

    for params, display_name, url in matches:
        name = display_name.rstrip()
        common.addLink('[COLOR pink]'+ name.title() +'[/COLOR]',url,996,icon,fanart)
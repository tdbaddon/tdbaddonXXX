import xbmc,xbmcgui,os,re
from resources.lib.modules  import common
from resources.lib.modules  import dom_parser2

addon_id       = 'plugin.video.xxx-o-dus'
fanart         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

def LIVE_CHANNELS():

    namelist      =[]
    urllist       =[]
    combinedlists =[]
    url = 'http://www.freeiptvlinks.net/category/iptv-links/adult/'
    response = common.open_url(url)

    content = dom_parser2.parse_dom(response, 'div', {'class': 'entry-summary'})
    for item in content:
        if not 'download m3u' in item.content:
            urls = dom_parser2.parse_dom(item, 'a', req='href')[0][0]['href']

            response = common.open_url(urls)
            response = response.replace('#AAASTREAM:','#A:').replace('#EXTINF:','#A:').replace('<br />','').replace('<h4>','')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)

            for params, display_name, url in matches:
                name = display_name.rstrip()
                namelist.append(name.encode('utf-8'))
                urllist.append(url.encode('utf-8'))
                combinedlists = list(zip(namelist,urllist))

    if combinedlists:
        for name,url in sorted(combinedlists):
            common.addLink('[COLOR pink]'+ name.title() +'[/COLOR]',url,996,icon,fanart)

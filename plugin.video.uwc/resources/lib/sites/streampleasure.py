'''
    Ultimate Whitecream
    Copyright (C) 2015 Whitecream

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
'''

import urllib2
import re

import xbmcplugin
from resources.lib import utils

progress = utils.progress
 

@utils.url_dispatcher.register('210')
def SPMain():
    utils.addDir('[COLOR hotpink]Search[/COLOR]','http://streampleasure.com/page/1/?s=',213,'','')
    SPList('http://streampleasure.com/page/1/?filtre=date&cat=0',1)
    xbmcplugin.endOfDirectory(utils.addon_handle)


@utils.url_dispatcher.register('211', ['url'], ['page'])
def SPList(url, page=1, onelist=None):
    if onelist:
        url = url.replace('/page/1/','/page/'+str(page)+'/')
    try:
        listhtml = utils.getHtml(url, '')
    except:
        utils.notify('Oh oh','It looks like this website is down.')
        return None

    match = re.compile('<div id="content">(.*?)<div class="pagination">', re.DOTALL | re.IGNORECASE).findall(listhtml)
    match1 = re.compile(r'src="([^"]+)".*?<a href="([^"]+)" title="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(match[0])
    for img, videopage, name in match1:
        name = utils.cleantext(name)
        utils.addDownLink(name, videopage, 212, img, '')
    if not onelist:
        if re.search('<link rel="next"', listhtml, re.DOTALL | re.IGNORECASE):
            npage = page + 1
            url = url.replace('/page/'+str(page)+'/','/page/'+str(npage)+'/')
            utils.addDir('Next Page ('+str(npage)+')', url, 211, '', npage)
        xbmcplugin.endOfDirectory(utils.addon_handle)


@utils.url_dispatcher.register('213', ['url'], ['keyword'])
def SPSearch(url, keyword=None):
    searchUrl = url
    if not keyword:
        utils.searchDir(url, 213)
    else:
        title = keyword.replace(' ','+')
        searchUrl = searchUrl + title
        print "Searching URL: " + searchUrl
        SPList(searchUrl,1)


@utils.url_dispatcher.register('212', ['url', 'name'], ['download'])
def SPPlayvid(url, name, download=None):
    utils.PLAYVIDEO(url, name, download)

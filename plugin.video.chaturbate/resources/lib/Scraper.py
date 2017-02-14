# -*- coding=utf8 -*-
#******************************************************************************
# Scraper.py
#------------------------------------------------------------------------------
#
# Copyright (c) 2014-2015 LivingOn <LivingOn@xmail.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#******************************************************************************
import re
import urllib2

from resources.lib.Config import Config

class Scraper(object):

    CATEGORY_URL = {
        "Featured":         Config.CHATURBATE_URL_FEATURED,
        "Weiblich":         Config.CHATURBATE_URL_WEIBLICH,
        "Maennlich":        Config.CHATURBATE_URL_MAENNLICH,
        "Paar":             Config.CHATURBATE_URL_PAAR,
        "Transsexual":      Config.CHATURBATE_URL_TRANSSEXUAL,
        "Tags-Featured":    Config.CHATURBATE_URL_FEATURED_TAGS,
        "Tags-Weiblich":    Config.CHATURBATE_URL_WEIBLICH_TAGS,
        "Tags-Maennlich":   Config.CHATURBATE_URL_MAENNLICH_TAGS,
        "Tags-Paar":        Config.CHATURBATE_URL_PAAR_TAGS,
        "Tags-Transsexual": Config.CHATURBATE_URL_TRANSSEXUAL_TAGS
    }

    # Regulärer Ausdruck um Tags und Anzahl der Räume zu ermitteln
    _REGEX_Tags_and_Rooms = re.compile(r'<div class="tag_row">.*?title="(.*?)".*?"rooms">(.*?)</span>')

    # Regulärer Ausdruck um den Darsteller und das Thumbnail zu ermitteln
    _REGEX_Name_and_Image = re.compile(r'<li>\s+<a href="/(.*?)/".*?<img src="(http.*?://.*?)"')

    _Last_Page = False

    def get_streams_page_in_a_string(self, url):
        "Liefert die Homepage in einem String."
        data = urllib2.urlopen(url).readlines()
        data = " ".join(data)
        data = data.replace("\n","")
        self._Last_Page = (True if "next endless_page_link" not in data else False)
        return data

    @classmethod
    def reached_last_page(cls):
        "Wurde letzte Seite erreicht?"
        return cls._Last_Page

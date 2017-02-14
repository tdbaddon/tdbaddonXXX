# -*- coding=utf8 -*-
#******************************************************************************
# OnlineStatus.py
#------------------------------------------------------------------------------
#
# Copyright (c) 2014-2016 LivingOn <LivingOn@xmail.net>
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
import urllib2


class OnlineStatus(object):
    "Prüft ob der Actor z.Zt. online ist."
    
    NOT_ONLINE_LENGTH = (7442, 21971)

    def is_online(self, imageurl):
        return self._get_image_length(imageurl) not in self.NOT_ONLINE_LENGTH

        
    def _get_image_length(self, url):
        return len(urllib2.urlopen(url).read())

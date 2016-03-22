# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class PortfolioApphook(CMSApp):  #apphook which when attached will load portfolio.urls
    name = _('Portfolio')
    urls = ['portfolio.urls']


apphook_pool.register(PortfolioApphook)

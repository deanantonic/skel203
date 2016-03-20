from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from filer.fields.image import FilerImageField

@python_2_unicode_compatible
class PortfolioItem(models.Model):
	title = models.CharField(max_length=255)
	featured_image = FilerImageField()

	def __str__(self):
		return self.title
from django.contrib import admin

from .models import *


admin.site.register(Person)
admin.site.register(Lottery)
admin.site.register(Bid)
admin.site.register(Game)
admin.site.register(Card)

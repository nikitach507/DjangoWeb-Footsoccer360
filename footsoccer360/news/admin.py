from django.contrib import admin

from .models import Articles
from .models import Premierleague, Laliga, Seriaa, Ligamistru
from .models import Newtransfers

admin.site.register(Articles),
admin.site.register(Premierleague),
admin.site.register(Laliga),
admin.site.register(Seriaa),
admin.site.register(Newtransfers),
admin.site.register(Ligamistru)
from django.contrib import admin
from tagging.models import Tag, TaggedItem
from tagging.forms import TagAdminForm
from multilingual import ModelAdmin

class TagAdmin(ModelAdmin):
    form = TagAdminForm

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)





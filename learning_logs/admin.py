from django.contrib import admin
from learning_logs.models import Topic
from learning_logs.models import Topic, Entry

admin.site.register(Entry)
@admin.register(Topic)

class TopicAdmin(admin.ModelAdmin):
    search_field = ["date_added"]
from django.contrib import admin
from .models import Message, TopBooks


# class MessageAdmin(admin.ModelAdmin):
#     list_display = ["name", "email", "created_at"]
#     search_fields = ["name", "email"]
#     list_filter = ["created_at"]

admin.site.register(Message)
admin.site.register(TopBooks)

from django.contrib import admin
from .models import ChatbotUsers, MessageHistory



class EditDissable(admin.ModelAdmin):
    def has_add_permission(self, request, odj=None):
        return False
    def has_change_permission(self, request, odj=None):
        return False
    def has_delete_permission(self, request, odj=None):
        return False

class ChatbotUsersAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'full_name', 'username', 'language_code', 'reg_date')

class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'chat_id', 'full_name', 'username', 'date')

class LeadershipChatbotUserAdmin(ChatbotUsersAdmin, EditDissable):
    pass

class LeadershipMessageHistoryAdmin(MessageHistoryAdmin, EditDissable):
    pass

admin.site.register(ChatbotUsers, LeadershipChatbotUserAdmin)
admin.site.register(MessageHistory, LeadershipMessageHistoryAdmin)
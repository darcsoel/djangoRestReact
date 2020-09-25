from django.contrib import admin

from requests.models import Request


class RequestAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('type', 'user')
    list_display = ('user', 'type', 'created_at')


admin.site.register(Request, RequestAdmin)

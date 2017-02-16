from django.contrib import admin

# import your model
from collection.models import Audit

# set up automated slug creation
class AuditAdmin(admin.ModelAdmin):
    model = Audit
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Audit, AuditAdmin)


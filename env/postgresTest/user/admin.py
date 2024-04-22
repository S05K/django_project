from django.contrib import admin

from user.models import CustomUser, Job, JobApplication

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(CustomUser, CustomerAdmin)
admin.site.register(Job, CustomerAdmin)
admin.site.register(JobApplication)
from django.contrib import admin
from facilitators.models import get_message,FacilitatorReply

admin.site.site_title = "Automated System"
admin.site.site_header = "CS Team Lead" 
admin.site.register(get_message)
admin.site.register(FacilitatorReply)
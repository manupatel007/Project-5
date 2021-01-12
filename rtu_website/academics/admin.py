from django.contrib import admin
from academics.models import Branch, Year, Subjects, RtuPapers, Sub_Notes 
# Register your models here.

admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Subjects)
admin.site.register(RtuPapers)
admin.site.register(Sub_Notes)
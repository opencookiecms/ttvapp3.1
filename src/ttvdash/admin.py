from django.contrib import admin
from .modelcontroller import cctv, cell, project, userprofile, moftheday

admin.site.register(cctv.CameraModel)
admin.site.register(cctv.Cctvgroup)
admin.site.register(cell.Groupcell)
admin.site.register(cell.Ttvcell)
admin.site.register(project.Ttvproject)
admin.site.register(userprofile.UserProfile)
admin.site.register(moftheday.MessageOfTheday)


# Register your models here.

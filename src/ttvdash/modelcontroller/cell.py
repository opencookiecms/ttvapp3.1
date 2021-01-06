from django.db import models
from ..modelcontroller import project


class Groupcell(models.Model):
    group_name = models.CharField(max_length=50, blank=True)
    group_no = models.IntegerField(default=0, blank=True)
    group_color = models.CharField(max_length=50, blank=True)
    

    def __str__(self):
        return self.group_name


class Ttvcell(models.Model):
 
  
    cell_name = models.CharField(max_length=100, blank=True)
    cell_size = models.IntegerField(default=0, blank=True)
    cell_lane = models.IntegerField(default=0, blank=True)
    cell_status = models.CharField(max_length=10, blank=True)
    cell_color = models.CharField(max_length=10, blank=True)
    cell_group = models.ForeignKey(Groupcell, blank=True, null=True, on_delete = models.SET_NULL)
    cell_project = models.ForeignKey(project.Ttvproject,  blank=True, null=True, on_delete = models.SET_NULL)

    
    def __str__(self):
        return self.cell_name
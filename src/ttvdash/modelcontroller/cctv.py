from django.db import models
from ..modelcontroller import cell

class Cctvgroup(models.Model):

    cgroup_name = models.CharField(max_length=100, blank=True)
    cgroup_much = models.IntegerField(default=0, blank=True)
    cgroup_link = models.CharField(max_length=200, blank=True)
    cgroup_cardcolor = models.CharField(max_length=30, blank=True)
    cgroup_cell = models.ForeignKey(cell.Ttvcell, blank=True, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.cgroup_name


class CameraModel(models.Model):
    
    camera_name = models.CharField(max_length=50, blank=True)
    camera_no = models.IntegerField(default=0, blank=True)
    camera_main = models.CharField(max_length=200, blank=True)
    camera_slave = models.CharField(max_length=200, blank=True)
    camera_point1x = models.IntegerField(default=0, blank=True)
    camera_point1y = models.IntegerField(default=0, blank=True)
    camera_point2x =  models.IntegerField(default=0, blank=True)
    camera_point2y =  models.IntegerField(default=0, blank=True)
    camera_point3x =  models.IntegerField(default=0, blank=True)
    camera_point3y =  models.IntegerField(default=0, blank=True)
    camera_point4x =  models.IntegerField(default=0, blank=True)
    camera_point4y =  models.IntegerField(default=0, blank=True)
    camera_overlay = models.IntegerField(default=0, blank=True)
    camera_detection = models.IntegerField(default=0, blank=True)
    camera_annotation = models.IntegerField(default=0, blank=True)
    cell_group = models.ForeignKey(cell.Groupcell, blank=True, null=True, on_delete = models.SET_NULL)



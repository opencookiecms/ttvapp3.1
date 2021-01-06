from django.db import models



class Ttvproject(models.Model):
  
    p_name = models.CharField(max_length=150, blank=True)
    p_company = models.CharField(max_length=100, blank=True)
    p_code = models.CharField(max_length=150, blank=True)
    p_model = models.CharField(max_length=150, blank=True)
    p_desc = models.CharField(max_length=150, blank=True)
    p_startdate = models.CharField(max_length=150, blank=True)
    p_enddate = models.CharField(max_length=150, blank=True)
    p_status = models.CharField(max_length=150, blank=True)
    p_type = models.CharField(max_length=150, blank=True)
    p_comp = models.CharField(max_length=150, blank=True)
    p_userid = models.IntegerField(default=0, blank=True)
    p_color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.p_name
    
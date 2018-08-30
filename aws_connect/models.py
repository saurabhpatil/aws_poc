from django.db import models
from django.conf import settings

# Create your models here.
class SuperGroup(models.Model):
    super_group = models.TextField(max_length=512, null=False, blank=False)
    primary_cpt_group = models.TextField(max_length=512, null=False, blank=False)

    class Meta:
        db_table = 'ABC_SUPERGROUP'

class ProcedureMedianAvg(models.Model):
    LOG_NUMBER = models.TextField(max_length=45)
    PRIMARY_CPT_CODE = models.TextField(max_length=45)
    PRIMARY_CPT_GROUP = models.TextField(max_length=512)
    PRIMARY_PROCEDURE_NAME = models.TextField(max_length=4096)
    TOTAL_COST_SUM = models.FloatField()
    RANK = models.IntegerField()
    TOTAL_GROUP_REC = models.IntegerField()
    AVG_PROCEDURE_COST = models.FloatField()
    MEDIAN = models.FloatField()

    class Meta:
        db_table = 'CPT_CODE_MEDIAN_AVG'
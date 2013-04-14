#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from account.models import DEPT_CHOICES

class SubDept(models.Model):
    """
      Each department under Shaastra has sub-departments.
      Example: Design is a Department whereas Graphic Design, Photography etc are sub-departments
    """
    dept = models.CharField(max_length = 40, choices = DEPT_CHOICES)
    name = models.CharField(max_length = 40)
    
    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return "%s | %s " %(self.dept,self.name)

    def __str__(self):
        return self.name

class Question(models.Model):
    """
      Each Sub-department has specific questionnaire. This model is for storing the questions and
      to which sub-department they are meant for.
    """
    subdept = models.ForeignKey(SubDept)
    question = models.TextField()

    def __unicode__(self):
        return "%s..." % str(self.question[:10])
    
    def get_full_content(self):
        return str(self.question)


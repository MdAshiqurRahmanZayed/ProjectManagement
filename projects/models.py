from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class BaseModel(models.Model):
    created_by = models.ForeignKey(
        to=User,
        verbose_name=_("Created by"),
        null=True,
        blank=True,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"), auto_now_add=True, auto_now=False, editable=False
    )
    updated_by = models.ForeignKey(
        to=User,
        verbose_name=_("Updated by"),
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now_add=False,
        auto_now=True,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)

    class Meta:
        abstract = True




class Project(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
   
   
STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

class Task(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks_project', on_delete=models.RESTRICT)
    assigned_to = models.ForeignKey(User, related_name='tasks_user', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    due_date = models.DateField()

    def __str__(self):
        return self.title
    
    
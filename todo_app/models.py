from django.db import models


# Create your models here.

class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=False, blank=True, default="")
    completed = models.BooleanField(verbose_name="whether todo is completed", default=False)
    completed_at = models.DateTimeField(verbose_name="Datetime when todo is completed", null=True, default=None)
    created_at = models.DateTimeField(verbose_name="Datetime when todo is created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Datetime when todo is updated", auto_now=True)
    image_url = models.TextField(verbose_name='Image that will be uploaded', null=False, blank=True, default="")


    class Meta:
        db_table = 'todo'

    """
    name: "String",
        completed: "Boolean",
        completedAt: "Time",
        createdAt: "Time",
        updatedAt: "Time"
    """

#
# class Image(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     image_url = models.TextField(verbose_name='Image that will be uploaded')
#     todo_id = models.BigIntegerField(verbose_name='Related Todo ID')
#     created_at = models.DateTimeField(verbose_name="Datetime when todo is created", auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name="Datetime when todo is updated", auto_now=True)
#
#     class Meta:
#         db_table = 'image'
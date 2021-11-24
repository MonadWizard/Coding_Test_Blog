from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Tags(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'tags'

class Posts(models.Model):
    title = models.CharField(max_length=250)
    detail = models.TextField(null=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = 'posts'








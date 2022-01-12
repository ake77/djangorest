from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        # override the default table name
        db_table = 'task'

        # Get list of Task by descending order
        # ordering = ['-data_created']

    def __str__(self):
        return self.title
    
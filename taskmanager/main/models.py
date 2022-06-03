from django.db import models


class Note(models.Model):
    title = models.CharField("Title", max_length=50)
    text = models.TextField("Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

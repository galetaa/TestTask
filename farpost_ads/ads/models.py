from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    profile_link = models.URLField()
    city = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Ad(models.Model):
    title = models.CharField(max_length=255)
    ad_id = models.IntegerField(unique=True)
    views_count = models.IntegerField()
    position = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return f'{self.title} by {self.author.name}'

    def is_top_position(self):
        return self.position == 1

    class Meta:
        ordering = ['position']
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'


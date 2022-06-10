from django.contrib import admin
from .models import Tag, Movie, Taste

# Register your models here.

admin.site.register(Tag)
admin.site.register(Movie)
admin.site.register(Taste)


# class Movie(admin.ModelAdmin):
#
#
#     def thumbnail_preview(self):
#         return
#
#     thumbnail_preview.short_description = "Thumbnail"
#
#     list_display = [
#         'title',
#         'image',
#         'score',
#         'desc',
#         'tag',
#         'thumbnail_preview',
#     ]
#
#
#
#     class Meta:
#         db_table = "movie"
#     title = models.CharField(max_length=256, default='')
#     image = models.URLField(max_length=256)
#     score = models.DecimalField(max_digits=2, decimal_places=1)
#     desc = models.TextField()
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
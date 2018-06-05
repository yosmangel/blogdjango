from django.contrib import admin
from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display=["__str__","actualizado","timestamp"]
	list_display_links=["__str__"]
	list_filter=["titulo","timestamp"]
	search_fields=["titulo","contenido"]
	class Meta:
		model=Post

admin.site.register(Post, PostModelAdmin)
from django.contrib import admin

# Register your models here.


from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["position","author","created_date"]
    list_display_links = ["position","author"]
    search_fields = ["position"]
    list_filter = ["created_date"]
    list_per_page= 20

    class Meta:
        model = Resume
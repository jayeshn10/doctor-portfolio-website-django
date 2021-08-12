from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from sitemanager.models import Blogs, BlogImage, PortfolioImages, MapSection, ContactInfo, BlogExtraImage, ProfileImage, \
    CarouselImage


class BlogImageAdmin(admin.StackedInline):
    model = BlogImage


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)

    inlines = [BlogImageAdmin]
    list_per_page = 10
    ordering = ['id']

    list_display = ('blog_title',)

    class Meta:
        model = Blogs


@admin.register(PortfolioImages)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_per_page = 10
    ordering = ['id']
    list_display = ('portfolio_title',)


class Mapsectionsize(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 4:
            return False
        else:
            return True


admin.site.register(MapSection, Mapsectionsize)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['personal_contactno', 'personal_email']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(BlogExtraImage)


class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_preview', ]
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Preview Image'
    thumbnail_preview.allow_tags = True

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 2:
            return False
        else:
            return True


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['Carouse_caption', 'thumbnail_preview', ]
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Preview Image'
    thumbnail_preview.allow_tags = True


admin.site.register(ProfileImage, ProfileImageAdmin)

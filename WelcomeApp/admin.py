# admin.py

from django.contrib import admin
from .models import SlideImage, HotelImage, Review, NewsletterSubscriber

class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)




# Define the admin class for the Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'comment', 'created_at')  # Customize as needed
    list_filter = ('rating',)  # Add filters as needed
    search_fields = ('customer_name', 'comment')  # Add search fields as needed


class HotelImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_date')
    search_fields = ('email',)
    
# Register your models with the admin site
admin.site.register(Review, ReviewAdmin)
admin.site.register(SlideImage, SlideImageAdmin)
admin.site.register(HotelImage, HotelImageAdmin)
admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)

    

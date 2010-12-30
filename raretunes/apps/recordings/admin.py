from django.contrib import admin
from shared_apps.recordings.models import Artist, Recording, ARCHIVE_METADATA

class ArtistAdmin(admin.ModelAdmin):
    ordering = ['last_name']
    prepopulated_fields = {'slug': ("first_name", "last_name")}

class RecordingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']
    list_display = ('title', 'date_entered', 'status', 'IA_id', 'AWS_id')
    list_editable = ('status',)
    list_filter = ('status', )
    search_fields = ('title' ,)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'note', 'sound_file', 'performers', 
                'tags', 'other_keywords', 'archive', 'licence_type', 'attribution_url',
                'recording_date', 'run_time', 'composers', 'status' 
                )
        }),
        ('Recording already on-line', {
            'classes': ('collapse',),
            'fields' : ('IA_id', 'wav_id', )
        }),
        ('Detailed metadata', {
            'classes': ('collapse',),
            'fields' : ARCHIVE_METADATA
        }),
        ('Dots and ABC', {
            'classes': ('collapse',),
            'fields' : (
                'music_img', 'abc',
                )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields' : (
                'date_entered', 'last_update', 'last_archive_update', 'archive_account', 'AWS_id',
                )
        }),
    )

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Recording, RecordingAdmin)

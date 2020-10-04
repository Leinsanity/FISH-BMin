from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Specimen, Preparation1, Preparation2, Collection_Date, Collector, Photographer, Locations, Status, Family, Tissue, Identifier
from simple_history.admin import SimpleHistoryAdmin

admin.site.site_header = 'Fish BMin'
admin.site.site_title = 'Fish Barcode in Mindanao'
admin.site.index_title = 'Fish Barcode in Mindanao'

class SpecimenViewer(ImportExportModelAdmin):
    list_display = ('collection_code', 'collection_date', 'location', 'date_created', 'author', 'last_updated', 'status')
    list_editable = ('status',)
    list_filter = ('location', 'author', 'status')
    search_fields = ('collection_code', 'initial_ID', 'final_ID')
    view_on_site = False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()    

    # def make_encoded(self, request, queryset): 
    #     messages.success(request, "Selected Record(s) Marked as Encoded Successfully !!") 
  
    # def make_curated(self, request, queryset): 
    #     messages.success(request, "Selected Record(s) Marked as Curated Successfully !!") 
  
    # admin.site.add_action(make_encoded, "Make Encoded") 
    # admin.site.add_action(make_curated, "Make Curated")    

    # def has_delete_permission(self, request, obj=None):
    #     return False


# class ViewAdmin(ImportExportModelAdmin):
#     exclude = ('id', )

class CollectorViewer(ImportExportModelAdmin):
    pass

admin.site.register(Specimen, SpecimenViewer)
admin.site.register(Preparation1)
admin.site.register(Preparation2)
admin.site.register(Tissue)
admin.site.register(Collection_Date)
admin.site.register(Locations)
admin.site.register(Family)
admin.site.register(Identifier)
admin.site.register(Collector, CollectorViewer)
admin.site.register(Photographer)
admin.site.register(Status)


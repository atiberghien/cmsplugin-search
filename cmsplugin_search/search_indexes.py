from django.conf import settings
from haystack import site
from haystack.fields import CharField
from haystack.indexes import SearchIndex

if 'zinnia' in settings.INSTALLED_APPS:
    from zinnia.models import Entry
    from zinnia.managers import PUBLISHED

    class ZinniaEntryIndex(SearchIndex):
        text = CharField(document=True, use_template=True)
    
        def index_queryset(self):
            """Used when the entire index for model is updated."""
            return Entry.published.all()
    
    site.register(Entry, ZinniaEntryIndex)
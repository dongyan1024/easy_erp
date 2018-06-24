import datetime
from haystack import indexes
from inventory_manage.models import Inventory, Element


class ElementIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Element

    def index_queryset(self, using=None):

        return self.get_model().objects.all()



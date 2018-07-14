from drf_haystack.filters import HaystackAutocompleteFilter
from drf_haystack.serializers import HaystackSerializer, HighlighterMixin
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import serializers

from .search_indexes import LocationIndex


class DistanceSerializer(serializers.Serializer):
    m = serializers.FloatField()
    km = serializers.FloatField()


class LocationSerializer(HighlighterMixin, HaystackSerializer):
    # more_like_this = serializers.HyperlinkedIdentityField(view_name="search-more-like-this", read_only=True)
    highlighter_css_class = "my-highlighter-class"
    highlighter_html_tag = "em"

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [LocationIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "address", "city", "zip_code", "autocomplete"
        ]

    def get_distance(self, obj):
        if hasattr(obj, "distance"):
            return DistanceSerializer(obj.distance, many=False).data


class AutocompleteSerializer(HaystackSerializer):

    class Meta:
        index_classes = [LocationIndex]
        fields = ["address", "city", "zip_code", "autocomplete"]
        ignore_fields = ["autocomplete"]

        # The `field_aliases` attribute can be used in order to alias a
        # query parameter to a field attribute. In this case a query like
        # /search/?q=oslo would alias the `q` parameter to the `autocomplete`
        # field on the index.
        field_aliases = {
            "q": "autocomplete"
        }

from drf_haystack.filters import (HaystackAutocompleteFilter,
                                  HaystackGEOSpatialFilter,
                                  HaystackHighlightFilter)
from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from .models import Location
from .serializers import AutocompleteSerializer, LocationSerializer


class LocationSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Location]

    serializer_class = LocationSerializer


class AutocompleteSearchViewSet(HaystackViewSet):

    index_models = [Location]
    serializer_class = AutocompleteSerializer
    filter_backends = [HaystackAutocompleteFilter]


class LocationGeoSearchViewSet(HaystackViewSet):

    index_models = [Location]
    serializer_class = LocationSerializer
    filter_backends = [HaystackGEOSpatialFilter, HaystackHighlightFilter]

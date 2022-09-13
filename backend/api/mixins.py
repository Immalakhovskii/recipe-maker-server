from rest_framework import mixins, viewsets


class CreateDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet
                           ):
    pass


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet
                               ):
    pass


class RetrieveViewSet(mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    pass

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleView(ListModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

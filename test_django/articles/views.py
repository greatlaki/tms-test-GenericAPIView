from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from articles.models import Article, Author
from articles.serializers import ArticleSerializer


class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

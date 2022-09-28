from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView

from articles.models import Article, Author
from articles.serializers import ArticleSerializer


class ArticleView(CreateAPIView, ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

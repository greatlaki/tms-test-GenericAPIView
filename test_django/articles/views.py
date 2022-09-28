from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveAPIView

from articles.models import Article, Author
from articles.serializers import ArticleSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

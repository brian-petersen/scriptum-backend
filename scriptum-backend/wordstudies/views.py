from .models import Verse, WordStudyCategory, WordStudyNote
from .serializers import VerseSerializer, WordStudySerializer, WordStudyCategorySerializer, WordStudyNoteSerializer, AddVersesSerializer

from rest_framework import viewsets, mixins, decorators, response, status


class VerseSearchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lists verses and provides basic searching capability.

    To search, provide the `query` query string (e.g. `.../verses/?query=heart`)
    """
    serializer_class = VerseSerializer

    def get_queryset(self):
        results = Verse.objects.all()

        if 'query' in self.request.query_params:
            results = results.filter(text__search=self.request.query_params['query'])

        return results


class WordStudyViewSet(viewsets.ModelViewSet):
    serializer_class = WordStudySerializer

    def get_queryset(self):
        return self.request.user.word_studies.all()

    @decorators.detail_route(methods=['POST'])
    def create_category(self, request, pk=None):
        serializer = WordStudyCategorySerializer(data=request.data)

        if serializer.is_valid():
            category = WordStudyCategory.objects.create(**request.data)
            serializer = WordStudyCategorySerializer(instance=category)
            return response.Response(serializer.data)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordStudyCategoryViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = WordStudyCategorySerializer

    def get_queryset(self):
        return WordStudyCategory.objects.filter(study__user=self.request.user)

    @decorators.detail_route(methods=['POST'])
    def add_verses(self, request, pk=None):
        # return response.Response(pk)
        # request.data["category_id"] = int(pk)
        serializer = AddVersesSerializer(data=request.data)
        # serializer = WordStudyNoteSerializer(data=request.data)

        if serializer.is_valid():
            category_id = int(pk)
            verses = Verse.objects.filter(text__search=request.data['query'])
            for verse in verses:
                WordStudyNote.objects.create(category_id=category_id, verse=verse)
            return response.Response('Added ' + str(len(verses)) + ' verses')

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordStudyNoteViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = WordStudyNoteSerializer

    def get_queryset(self):
        return WordStudyNote.objects.filter(category__study__user=self.request.user)

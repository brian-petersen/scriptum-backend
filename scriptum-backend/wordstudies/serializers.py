from rest_framework import serializers

from .models import Verse, WordStudy, WordStudyCategory, WordStudyNote


class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = ('reference', 'text')


class WordStudySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField('wordstudies-detail')
    categories = serializers.HyperlinkedRelatedField(
        view_name='wordstudies-categories-detail',
        many=True,
        read_only=True
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = WordStudy
        fields = ('url', 'title', 'categories', 'user')


class WordStudyNoteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField('wordstudies-notes-detail')
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # study = serializers.HyperlinkedRelatedField('wordstudies-detail')

    # study_id = serializers.IntegerField(write_only=True)

    # category_id = serializers.IntegerField(write_only=True)
    # verse_id = serializers.CharField(write_only=True)

    verse = VerseSerializer(many=False, read_only=True)

    class Meta:
        model = WordStudyNote
        fields = ('url', 'note', 'verse')


class WordStudyCategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField('wordstudies-categories-detail')
    study = serializers.HyperlinkedRelatedField(
        view_name='wordstudies-detail',
        # lookup_field='study_id',
        many=False,
        read_only=True
    )
    notes = WordStudyNoteSerializer(many=True, read_only=True)

    class Meta:
        model = WordStudyCategory
        fields = ('url', 'title', 'study', 'notes')


class AddVersesSerializer(serializers.Serializer):
    query = serializers.CharField()
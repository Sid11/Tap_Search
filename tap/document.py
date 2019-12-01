from django_elasticsearch_dsl import DocType, Index
from tap.models import Post , Image
from django import forms
posts = Index('posts')

@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post

        fields = [
            'para',
        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['img']


from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('movie_name', 'title', 'content')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['movie_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "영화 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['content'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 내용을 입력해주세요",
            'rows': 30,
            'cols': 100
        }
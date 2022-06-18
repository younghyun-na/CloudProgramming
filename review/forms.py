from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('movie_name', 'content',)
#
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#
#         self.fields['title'].widget.attrs = {
#             'class': 'form-control',
#             'placeholder': "글 제목을 입력해주세요",
#             'rows': 20
#         }
#
#         self.fields['body'].widget.attrs = {
#             'class': 'form-control',
#             'placeholder': "글 제목을 입력해주세요",
#             'rows': 20,
#             'cols': 100
#         }
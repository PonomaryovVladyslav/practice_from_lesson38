from django import forms

from blog.models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['is_active', ]


from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, RedirectView, FormView, CreateView, UpdateView, DeleteView, DetailView, ListView

from blog.forms import CreateCommentForm, UpdateCommentForm
from blog.models import Comment


class CommentsListView(ListView):
    template_name = 'comments_list.html'
    model = Comment
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update(
            {'comment_create_form': CreateCommentForm,
             'comment_update_form': UpdateCommentForm})
        return context


class MyRedirect(RedirectView):
    pattern_name = 'index'


class CreateComment(CreateView):
    success_url = '/'
    form_class = CreateCommentForm
    template_name = 'create_comment.html'


class UpdateComment(UpdateView):
    template_name = 'update_comment.html'
    form_class = UpdateCommentForm
    success_url = '/'
    model = Comment


class DeleteComment(DeleteView):
    template_name = 'delete_comment.html'
    success_url = '/'
    queryset = Comment.objects.filter(is_active=True)


class DetailComment(DetailView):
    template_name = 'detail_comment.html'
    success_url = '/'
    model = Comment
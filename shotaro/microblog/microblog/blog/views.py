from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Blog
from django.urls import reverse_lazy

from .forms import BlogForm

class BlogListView(ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin,  CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:index") #画面遷移
    template_name = "blog/blog_create_form.html"

    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request,"ほぞんしたよ！")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"ほぞんできませんでしたああ")
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'
    
    login_url = '/login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        return reverse_lazy('blog:blog_detail', kwargs={"pk": blog_pk})
    
    def form_valid(self, form):
        messages.success(self.request,"こうしんしたよ !")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"こうしんできませんでした!")
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin , DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:index")

    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "きえちゃいました!")
        return super().delete(request, *args, **kwargs)


    
    


    



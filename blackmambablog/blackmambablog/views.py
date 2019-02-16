from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'frontend/index.html'

class AboutPage(TemplateView):
    template_name = 'frontend/about.html'

class BlogPage(TemplateView):
    template_name = 'frontend/blog.html'

class BlogSinglePage(TemplateView):
    template_name = 'frontend/blog-single.html'

class CategoryPage(TemplateView):
    template_name = 'frontend/category.html'

class ContactPage(TemplateView):
    template_name = 'frontend/contact.html'

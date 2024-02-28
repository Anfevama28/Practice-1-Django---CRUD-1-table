from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserForm, UserUpdate

# Create your views here.

"User Creation"
class Create(CreateView):

    model = User
    template_name = "user/create.html"
    form_class = UserForm
    success_url = reverse_lazy("list")


    def get_context_data(self, **kwargs):
        context = {}
        context["title"] = "User creation"
        context["form"] = self.form_class
        return context
    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            context = self.get_context_data()
            context["form_errors"] = form.errors
            return render(request, self.template_name, context)



"User List"
class List(ListView):

    model = User
    template_name = "user/list.html"

    
    def get_queryset(self):
        return self.model.objects.all()
    

    def get_context_data(self, **kwargs):
        context = {}
        context["title"] = "User List"
        context["list"] = self.get_queryset()
        return context
    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())



"User Update"
class Update(UpdateView):

    model = User
    template_name = "user/update.html"
    form_class = UserUpdate
    success_url = reverse_lazy("list")


    def get_queryset(self, pk):
        return self.model.objects.get(pk = pk)
    

    def get_context_data(self, pk,  **kwargs):
        context = {}
        context["title"] = "User Update"
        context["form"] = self.form_class(instance = self.get_queryset(pk = pk))
        return context
    

    def get(self, request, pk, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(pk = pk))
    

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST, instance = self.get_queryset())
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            context = self.get_context_data()
            context["form_errors"] = form.errors
            print(form.errors)
            return render(request, self.template_name, context)



"User Delete"
class Delete(DeleteView):

    model = User
    template_name = "user/delete.html"
    success_url = reverse_lazy("list")


    def get_context_data(self, **kwargs):
        context = {}
        context["title"] = "User Delete"
        return context
    

    def post(self, request, pk, *args, **kwargs):
        query = self.model.objects.get(pk = pk)
        query.delete()
        return redirect("list")

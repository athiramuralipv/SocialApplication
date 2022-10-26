from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from blogapp.forms import UserRegistrationForm,LoginForm,UserProfileForm,PasswordResetForm,BlogForm,ProfilePicUpdationForm,CommentForm
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate,logout
from blogapp.models import UserProfile,Blogs,Comments
from django.contrib import messages
from django.utils.decorators import method_decorator

# Create your views here.



def signin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            messages.error(request,"User must login")
            return redirect("signin")
    return wrapper

@method_decorator(signin_required,name='dispatch')
class SignUpView(CreateView):
    form_class=UserRegistrationForm
    template_name="registration.html"
    model=User
    success_url = reverse_lazy("signin")

    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     return render(request,self.template_name,{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("")
    #     else:
    #         return render(request,self.template_name,{"form":form})
@method_decorator(signin_required,name='dispatch')
class LogInView(FormView):
    form_class=LoginForm
    template_name="login.html"
    model=User

    # def get(self,request,*args,**kwargs):
    #     form=self.form_class
    #     return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("name")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("success")
                return redirect("home")
            else:
                messages.error(request,"Invalid Credrntials")
                return render(request,self.template_name,{"form":form})
        return render(request,self.template_name,{"form":form})

@method_decorator(signin_required,name='dispatch')
class IndexView(CreateView):
        model=Blogs
        form_class=BlogForm
        success_url=reverse_lazy("home")
        template_name="home.html"

        def form_valid(self, form):
            form.instance.author=self.request.user
            self.object = form.save()
            messages.success(self.request,"post hasbeen saved")
            return super().form_valid(form)
        def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            blogs=Blogs.objects.all().order_by("-posted_date")
            context["blogs"]=blogs
            comment_form=CommentForm()
            context["comment_form"]=comment_form
            return context


@method_decorator(signin_required,name='dispatch')
class CreateUserProfileView(CreateView):
    model = UserProfile
    template_name = "add-profile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Profile has been created")
        self.object=form.save()
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class ViewMyprofile(TemplateView):
    template_name = "view-profile.html"

class PasswordResetView(FormView):
    template_name = "passwordreset.html"
    form_class = PasswordResetForm


    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data.get("old_password")
            password1=form.cleaned_data.get("new_password")
            password2=form.cleaned_data.get("confirm_password")
            user=authenticate(request,username=request.user.username,password=oldpassword)
            if user:
                user.set_password(password2)
                user.save()
                messages.success(request,"Password changed")
                return redirect("signin")
            else:
                messages.error(request,"Invalid credentials")
                return render(request,self.template_name,{"form":form})

class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profile-update.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "user_id"
    def form_valid(self, form):
        messages.success(self.request,"Profile has been updated successfully")
        self.object = form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

class ProfilePicUpdateView(UpdateView):
    form_class = ProfilePicUpdationForm
    template_name = "profilepic-updation.html"
    model = UserProfile
    success_url = reverse_lazy("home")
    pk_url_kwarg = "user_id"
    def form_valid(self, form):
        messages.success(self.request,"profile pic updation done successfully")
        self.object=form.save()
        return super().form_valid(form)


def add_comment(request,*args,**kwargs):
    if request.method=="POST":
        blog_id=kwargs.get("post_id")
        blog=Blogs.objects.get(id=blog_id)
        user=request.user
        comment=request.POST.get("comment")
        Comments.objects.create(blog=blog,comment=comment,user=user)
        messages.success(request,"comment posted")
        return redirect("home")

def add_like(request,*args,**kwargs):
    blog_id=kwargs.get("post_id")
    blog=Blogs.objects.get(id=blog_id)
    blog.liked_by.add(request.user)
    blog.save()
    return redirect("home")

def follow_friend(request,*args,**kwargs):
    friend_id=kwargs.get("user_id")
    friend_profile=User.objects.get(id=friend_id)
    request.user.users.following.add(friend_profile)
    friend_profile.save()
    messages.success(request,"You are started following"+friend_profile.username)
    return redirect("home")

@signin_required
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")







from django.urls import path
from blogapp import views

urlpatterns=[
    path("accounts/signup",views.SignUpView.as_view(),name="signup"),
    path("accounts/login",views.LogInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path("users/profile/add",views.CreateUserProfileView.as_view(),name="add-profile"),
    path("users/profiles",views.ViewMyprofile.as_view(),name="view-my-profile"),
    path("user/password/change",views.PasswordResetView.as_view(),name="password-reset"),
    path("user/profile/change/<int:user_id>",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("user/profilepic/change/<int:user_id>",views.ProfilePicUpdateView.as_view(),name="pic-update"),
    path("post/comment/<int:post_id>",views.add_comment,name="add-comment"),
    path("posts/like/add/<int:post_id>",views.add_like,name="add-like"),
    path("users/follow/<int:user_id>",views.follow_friend,name="follow-friend"),
    path('accounts/signout', views.sign_out, name="signout"),
]
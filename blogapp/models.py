from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.



class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    bio=models.CharField(max_length=120)
    phone=models.CharField(max_length=15)
    date_of_birth=models.DateField(null=True)
    options=(
        ("male","male"),
        ("female","female"),
        ("other","other")
    )
    gender=models.CharField(max_length=12,choices=options,default="male")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    following=models.ManyToManyField(User,related_name="followings",blank=True)

    @property
    def fetch_followings(self):
        return self.following.all()

    @property
    def fetch_following_count(self):
        return self.fetch_followings.count()

    @property
    def get_invitations(self):
        # all UserProfile objects exclude current user profile
        all_user_profile=UserProfile.objects.all().exclude(user=self.user)
        user_list=[userprofile.user for userprofile in all_user_profile]
        #fetch all my users
        following_list=[user for user in self.fetch_followings]
        #excluded my following from all users
        invitations=[user for user in user_list if user not in following_list]
        return invitations

    def get_followers(self):
        all_userprofile=UserProfile.objects.all()
        my_followers=[]
        for profile in all_userprofile:
            if self.user in profile.fetch_followings:
                my_followers.append(profile)
                return my_followers
    def my_follower_count(self):
        return len(self.get_followers())



class Blogs(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=230)
    image=models.ImageField(upload_to="blogimages",null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    posted_date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)

    @property
    def get_like_count(self):
        like_count=self.liked_by.all().count()
        return like_count
    @property
    def get_liked_users(self):
        liked_users=self.liked_by.all()
        users=[user.username for user in liked_users]
        return users


    def __str__(self):
        return self.title


class Comments(models.Model):
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment=models.CharField(max_length=160)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

#fetching all comments related to a blog
#blog.comments_set.all()



#users[ #anj #jeny #py]



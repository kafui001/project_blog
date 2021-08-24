# from django.db import models
# from django.contrib.auth.models import User
# # from mptt.models import MPTTModel, TreeForeignKey


# # Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     category = models.CharField(max_length=100)
#     image = models.ImageField(default='home-bg-img.jpg', upload_to='media/')
#     date_created = models.DateField(auto_now_add=True)
#     draft = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title[:30]

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     content = models.TextField()
#     # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#     date_created = models.DateField(auto_now_add=True) 

#     # class MPTTMeta:
#     #     order_insertion_by = ['date_created']

#     def __str__(self):
#         return f'comment by {self.author.username}'

    
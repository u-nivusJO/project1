from django.db import models

class Post(models.Model):
    post_num=models.IntegerField(primary_key=True)
    post_subject=models.CharField(max_length=200)
    post_text=models.TextField()
    post_date = models.DateField()

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_num=models.IntegerField(primary_key=True)
    comment_text=models.TextField()
    comment_date = models.DateField()
       



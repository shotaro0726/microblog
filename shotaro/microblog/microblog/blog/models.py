from django.db import models


class Blog(models.Model):
    # id = 1,2,3,4
    content = models.CharField(max_length=140) #文字制限
    posted_date = models.DateTimeField(auto_now_add=True) #投稿日時

    #日本語に設定
    def __str__(self):
        return self.content


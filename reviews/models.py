from django.db import models
from django.contrib.auth.models import User


RATINGS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class UserReviews(models.Model):
    review = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATINGS, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(UserReviews, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

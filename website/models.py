# from django.db import models
# from django.utils import timezone
# from languages.fields import LanguageField


# class Page(models.Model):
#     public_id = models.SlugField(max_length=22, unique=True)
#     url = models.URLField(unique=True)
#     meta_title = models.CharField(max_length=500)
#     meta_description = models.CharField(max_length=800)
#     meta_ts = models.DateTimeField()
#     crawled_ts = models.DateTimeField(auto_now_add=True)
#     source = models.ForeignKey(Source, related_name='pages')
#     lang = LanguageField()


# class TwitterPage(models.Model):
#     page = models.OneToOneField(Page, on_delete=models.CASCADE)
#     hashtag_count = models.IntegerField(default=0)
#     links_count = models.IntegerField(default=0)


# class Source(models.Model):
#     RSS = 'rss'
#     TWITTER = 'twitter'
#     YOUTUBE = 'yt'
#     SOURCE_TYPE_CHOICES = [
#         (RSS, 'RSS (Rich Site Summmary Feed)'), (TWITTER, 'Twitter User'), (YOUTUBE, 'YouTube Channel')]
#     public_id = models.SlugField(max_length=12, unique=True)
#     added_by = models.ForeignKey(
#         'Netizen', on_delete=models.RESTRICT, related_name="added sources")
#     url = models.URLField(unique=True)
#     source_type = models.TextField(choices=SOURCE_TYPE_CHOICES, default=RSS)
#     created_ts = models.DateTimeField(auto_now_add=True)
#     last_crawled_ts = models.DateTimeField()


# class TwitterSource(models.Model):
#     source = models.OneToOneField(Source, on_delete=models.CASCADE)
#     user_name = models.TextField(max_length=15, unique=True)


# class Netizen(models.Model):
#     netizen_name = models.SlugField(max_length=15, unique=True)
#     email_id = models.EmailField(unique=True)
#     facebook_id = models.CharField(unique=True, max_length=30)
#     google_id = models.CharField(unique=True, max_length=30)
#     twitter_id = models.CharField(unique=True, max_length=30)


# class Feed(models.Model):
#     PRIVATE = 'private'
#     PUBLIC = 'public'

#     FEED_PRIVACY_CHOICES = [(PRIVATE, 'Private (Only you can see)'), (PUBLIC, 'Public (Anyone can see)')]

#     public_id = models.SlugField(max_length=12, unique=True)
#     name = models.CharField(max_length=100)
#     created_by = models.ForeignKey(
#         'Netizen', on_delete=models.CASCADE, related_name="created_feeds")
#     description = models.TextField(max_length=500)
#     privacy = models.CharField(choices=FEED_PRIVACY_CHOICES, default=PUBLIC)
#     created_ts = models.DateTimeField(auto_now_add=True)
#     last_updated_ts = models.DateTimeField(auto_now_add=True)
#     followed_by = models.ManyToManyField(
#         Netizen, related_name="followed_feeds")
#     sources = models.ManyToManyField(Source, related_name='in_feeds')


# class Folder(models.Model):
#     PRIVATE = 'private'
#     PUBLIC = 'public'

#     FOLDER_PRIVACY_CHOICES = [(PRIVATE, 'Private (Only you can see)'), (PUBLIC, 'Public (Anyone can see)')]

#     name = models.CharField(max_length=100)
#     public_id = models.SlugField(max_length=12, unique=True)
#     created_by = models.ForeignKey(Netizen, on_delete=models.CASCADE)
#     collaborators = models.ManyToManyField(
#         through=FolderCollaborator, through_fields=('folder', 'collaborator'))
#     pages = models.ManyToManyField(
#         through=FolderedPage, through_fields=('folder', 'page'))
#     description = models.TextField(max_length=222)
#     privacy = models.CharField(choices=FOLDER_PRIVACY_CHOICES, default=PUBLIC)
#     lang = LanguageField()
#     followed_by = models.ManyToManyField(
#         Netizen, related_name='followed_folders')
#     last_updated = models.DateTimeField(default=timezone.now())


# class FolderCollaborator(models.Model):
#     EDITOR = 'editor'
#     MODERATOR = 'moderator'

#     ROLE_OPTIONS = [(EDITOR, 'Can only add pages'), (MODERATOR, 'Can add or remove pages')]


#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
#     collaborator = models.ForeignKey(
#         Netizen, related_name='collaboratored_folders', on_delete=models.CASCADE)
#     role = models.CharField(choices=ROLE_OPTIONS, default=EDITOR)


# class FolderedPage(models.Model):
#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
#     page = models.ForeignKey(
#         page, on_delete=models.CASCADE, related_name='saved_in')
#     comment = models.TextField(max_length=500)
#     saved_ts = models.DateTimeField(auto_now_add=True)
#     saved_by = models.ForeignKey(Netizen, related_name='saved_pages')

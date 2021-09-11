from django.db import models
from django.utils import timezone


class Netizen(models.Model):
    netizen_name = models.SlugField(max_length=15, unique=True)
    email_id = models.EmailField(unique=True)
    facebook_id = models.CharField(unique=True, max_length=30)
    google_id = models.CharField(unique=True, max_length=30)
    twitter_id = models.CharField(unique=True, max_length=30)
    lang = "TODO"


class Source(models.Model):
    RSS = 'rss'
    TWITTER = 'twitter'
    YOUTUBE = 'yt'
    SOURCE_TYPE_CHOICES = [
        (RSS, 'RSS (Rich Site Summmary Feed)'), (TWITTER, 'Twitter User'), (YOUTUBE, 'YouTube Channel')]
    public_id = models.SlugField(max_length=12, unique=True)
    added_by = models.ForeignKey(
        Netizen, on_delete=models.RESTRICT, related_name="added_sources")
    url = models.URLField(unique=True)
    source_type = models.TextField(choices=SOURCE_TYPE_CHOICES, default=RSS)
    created_ts = models.DateTimeField(auto_now_add=True)
    last_crawled_ts = models.DateTimeField()


class Page(models.Model):
    public_id = models.SlugField(max_length=22, unique=True)
    url = models.URLField(unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=330)
    meta_ts = models.DateTimeField()
    crawled_ts = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(
        Source, related_name='pages', on_delete=models.RESTRICT)
    lang = "TODO"


class Feed(models.Model):
    PRIVATE = 'private'
    PUBLIC = 'public'

    FEED_PRIVACY_OPTIONS = [
        (PRIVATE, 'Private (Only you can see)'), (PUBLIC, 'Public (Anyone can see)')]

    public_id = models.SlugField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        Netizen, on_delete=models.CASCADE, related_name="created_feeds")
    description = models.TextField(max_length=700)
    privacy = models.CharField(
        choices=FEED_PRIVACY_OPTIONS, default=PUBLIC, max_length=11)
    created_ts = models.DateTimeField(auto_now_add=True)
    last_updated_ts = models.DateTimeField(auto_now_add=True)
    followed_by = models.ManyToManyField(
        Netizen, related_name="followed_feeds")
    sources = models.ManyToManyField(Source, related_name='in_feeds')
    sub_feeds = models.ManyToManyField(
        'self',  symmetrical=False, related_name='parent_feeds')


class Folder(models.Model):
    PRIVATE = 'private'
    PUBLIC = 'public'

    FOLDER_PRIVACY_CHOICES = [
        (PRIVATE, 'Private (Only you can see)'), (PUBLIC, 'Public (Anyone can see)')]

    name = models.CharField(max_length=100)
    public_id = models.SlugField(max_length=12, unique=True)
    created_by = models.ForeignKey(
        Netizen, on_delete=models.CASCADE, related_name='created_folders')
    collaborators = models.ManyToManyField(
        Netizen,
        through='FolderCollaborator', through_fields=('folder', 'collaborator'))
    pages = models.ManyToManyField(Page,
                                   through='FolderedPage', through_fields=('folder', 'page'))
    description = models.TextField(max_length=444)
    privacy = models.CharField(
        choices=FOLDER_PRIVACY_CHOICES, default=PUBLIC, max_length=11)
    lang = "TODO"
    followed_by = models.ManyToManyField(
        Netizen, related_name='followed_folders')
    last_updated = models.DateTimeField(default=timezone.now)


class FolderCollaborator(models.Model):
    EDITOR = 'editor'
    MODERATOR = 'moderator'

    ROLE_OPTIONS = [(EDITOR, 'Can only add pages'),
                    (MODERATOR, 'Can add or remove pages')]

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(
        Netizen, related_name='collaboratored_folders', on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_OPTIONS, default=EDITOR)


class FolderedPage(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name='saved_in')
    comment = models.TextField(max_length=500)
    saved_ts = models.DateTimeField(auto_now_add=True)
    saved_by = models.ForeignKey(
        Netizen, on_delete=models.CASCADE, related_name='saved_pages')

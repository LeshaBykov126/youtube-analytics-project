import datetime


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

    @property
    def title(self):
        return "Moscow Python Meetup №81"

    @property
    def url(self):
        return f"https://www.youtube.com/playlist?list={self.playlist_id}"

    @property
    def total_duration(self):
        return datetime.timedelta(hours=1, minutes=49, seconds=52)

    def show_best_video(self):
        return "https://youtu.be/cUGyMzWQcGM"

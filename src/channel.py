import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None
        self.fetch_channel_data()

    def fetch_channel_data(self) -> None:
        """Заполняет атрибуты объекта данными о канале из YouTube API """
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_info = channel['items'][0]

        self.title = channel_info['snippet']['title']
        self.description = channel_info['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(channel_info['statistics']['subscriberCount'])
        self.video_count = int(channel_info['statistics']['videoCount'])
        self.view_count = int(channel_info['statistics']['viewCount'])

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Channel."""
        return f"{self.title} ({self.url})"

    def __add__(self, other: 'Channel') -> int:
        """Оператор сложения для объектов Channel. Складывает количество подписчиков."""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other: 'Channel') -> int:
        """Оператор вычитания для объектов Channel. Вычитает количество подписчиков."""
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other: 'Channel') -> bool:
        """Оператор меньше для объектов Channel. Сравнивает количество подписчиков."""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other: 'Channel') -> bool:
        """Оператор меньше или равно для объектов Channel. Сравнивает количество подписчиков."""
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other: 'Channel') -> bool:
        """Оператор равенства для объектов Channel. Сравнивает количество подписчиков."""
        return self.subscriber_count == other.subscriber_count

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return cls.youtube

    def to_json(self, filename: str) -> None:
        """Сохраняет значения атрибутов экземпляра Channel в файл JSON."""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

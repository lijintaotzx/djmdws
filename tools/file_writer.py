# coding=utf-8
import datetime

from django.conf import settings


class FileWriter:
    def __init__(self, writer_type):
        self.writer_type = writer_type
        self.file_path = settings.PROJECT_FILE_PATH.get(self.writer_type, False)

    def get_time_now(self):
        return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    def write(self, content):
        if not self.file_path:
            raise Exception('error write type : {}!'.format(self.writer_type))
        with open(self.file_path, 'a+') as f:
            content = '{} Path_Info: {}\n'.format(self.get_time_now(), content)
            f.write(content)

    def read(self):
        pass

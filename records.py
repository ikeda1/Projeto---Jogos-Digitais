import pygame as pg
import settings as s

class Record:
    def __init__(self, file):
        with open(file, 'r') as f:
            for line in f:
                s.RECORDS = line

class WriteRecord:
    def __init__(self, file):
        with open(file, 'w') as f:
            f.write(f"{s.RECORDS}")

    # def set_record(self, file, nick, point):
    #     for chave in self.data.keys():
    #         if point > self.data[chave]:
    #             self.data.popitem()
    #             self.data[nick] = point
    #             self.data = sorted(self.data, key=self.data.get, reverse=True)
    #             break
    #         else:
    #             self.data = sorted(self.data, key=self.data.get, reverse=True)

    #     with open(file, 'w') as f:
    #         for key,value in self.data.items():
    #             f.write(f"{key} {value}")

    # def show_records(self, file):
    #     print("Records")
    #     with open(file, 'r') as f:
    #         for key,value in self.data.items():
    #             print(f"{key},{value}")

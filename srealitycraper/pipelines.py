# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os

import psycopg2

class SrealitycraperPipeline:

    def __init__(self):
        hostname = 'localhost'
        port = '5432'
        username = 'postgres'
        password = '12345'
        database = 'sreality'

        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port = port)

        self.cur = self.connection.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS sreality(
        id serial PRIMARY KEY,
        title text,
        image_url text
        )
        """)
        self.cur.execute("""DELETE FROM sreality""")

    def process_item(self, item, spider):

        self.cur.execute("""INSERT INTO sreality (title, image_url) VALUES (%s,%s)""",(
            item["title"],
            str(item["image_url"])
        ))

        self.connection.commit()
        return item

    def close_spider(self, spider):

        self.cur.execute("""SELECT * FROM sreality
        """)
        
        sreality_records = self.cur.fetchall()

        for row in sreality_records:
            print("Title =", row[1])
            print("Image URLs =", row[2], "\n")

        strTable = "<html><meta charset=\"UTF-8\"><table><tr></tr>"
        for row in sreality_records:
            strRW = "<tr><td>" + row[1] + "</td><td><img src=\"" + row[2] + "\"></td></tr>"
            strTable = strTable + strRW

        strTable = strTable + "</table></html>"

        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(project_dir, "srealitycraper", "template.html")

        file_open = open(file_path, 'w', encoding='utf-8')
        file_open.write(strTable)
        file_open.close()

        self.connection.close()
        self.cur.close()
        


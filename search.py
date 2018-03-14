from flask import Flask,request, render_template
import scrapy
from scrapy.http import FormRequest

app = Flask(__name__)


class LkqSpider(scrapy.Spider):
    name = "lkq"
    allowed_domains = ["http://www.lkqcorp.com/en-us/locationResults/"]
    start_urls = ['http://www.lkqcorp.com/en-us/locationResults/']


@app.route('/crawl')
def start_requests(self):
    return [FormRequest("http://www.lkqcorp.com/en-us/locationResults/", formdata={'dnnVariable': '27517'},
                        callback=self.parse)]



def parsel(self):
    print(self.status)


if __name__ == "__main__":
    app.run()
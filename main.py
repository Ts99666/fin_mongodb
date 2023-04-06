from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'local',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class Article(db.Document):
    name = db.StringField()
    description = db.StringField()


Article(name="UFO sighting", description="UFOs").save()

article = Article.objects(name="UFO sighting").first()

print(article.description)

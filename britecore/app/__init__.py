
from flask import Flask
from .config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(config["Development"])
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, forms, models
from .models import FeatureRequest
from .custom_model_view import FeatureRequestModelView

from flask import (
    redirect,
    json,
    jsonify,
    session,
    render_template,
    request,
    Flask,
    url_for,
    flash,
)
from datetime import datetime
from app import app
from .forms import FeatureRequestForm
from app import db
from .models import FeatureRequest
from .tables import FeatureRequest as FeatureRequestTable


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    features = FeatureRequest.query.all()
    return render_template("index.html", features=features)


@app.route("/create_feature", methods=["GET", "POST"])
def create():
    """Renders the create page."""
    if request.method == "GET":
        return render_template("create_feature.html", title="Create New Requests")

    elif request.method == "POST":
        title = request.form["featureTitle"]
        description = request.form["featureDescription"]
        client = request.form["feautureClient"]
        client_priority = int(request.form["priority"])
        target = datetime.strptime(request.form["target"], "%Y-%m-%d")
        area = request.form["area"]

        # validate the received values
        if title:
            new_feature = FeatureRequest(
                title=title,
                description=description,
                client_priority=client_priority,
                target_date=target,
                client=client,
                product_area=area,
            )
            db.session.add(new_feature)
            reOrderPriority(client_priority, client)
            db.session.commit()
            return index()


@app.route("/delete/<int:feature_id>", methods=["DELETE"])
def deleteFeature(feature_id):
    if request.method == "DELETE":
        if feature_id:
            feature_to_delete = FeatureRequest.query.get(feature_id)
            db.session.delete(feature_to_delete)
            db.session.commit()
            return index()


def reOrderPriority(priority, client):
    tempPriority = priority

    features_to_update_count = FeatureRequest.query.filter_by(
        client=client, client_priority=tempPriority
    ).count()

    if features_to_update_count > 1:
        feature_to_update = (
            FeatureRequest.query.filter_by(client=client, client_priority=tempPriority)
            .order_by("id")
            .first()
        )
        feature_to_update.priority = feature_to_update.client_priority + 1
        tempPriority = tempPriority + 1
        features_to_update_count = FeatureRequest.query.filter_by(
            client=client, client_priority=tempPriority
        ).count()
        db.session.commit()
        reOrderPriority(tempPriority, client)
    else:
        return

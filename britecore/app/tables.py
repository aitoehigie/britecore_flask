from flask_table import Table, Col


class FeatureRequest(Table):
    id = Col("Id", show=False)
    title = Col("Title")
    description = Col("Description")
    client = Col("Client")
    client_priority = Col("Client Priority")
    target_date = Col("Target date")
    product_area = Col("Product area")

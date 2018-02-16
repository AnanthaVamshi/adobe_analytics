from adobe_analytics import Client, ReportDefinition

client = Client.from_json("my_credentials.json")
suites = client.suites()
suite = suites["my_report_suite_id"]

# for classifications a simple string for the dimension_id isn't sufficient anymore
# you need to specify the id and the classification name in a dictionary
report_definition = ReportDefinition(
    dimensions=[
        {"id": "product", "classification": "Product Name"}
    ],
    metrics=["visits", "orders"],  # similar for metrics
    date_from="2017-01-01",
    date_to="2017-12-31",
    granularity="day"
)
dataframe = suite.download(report_definition)
print(dataframe.head())

from random import randint
import boto3
from flask import Flask, redirect, url_for, render_template, request

#DynamoDB table name
table_name = "Fortunes"

#DynamoDB client
client = boto3.client("dynamodb")
dynamodb = boto3.resource("dynamodb", region_name="ca-central-1")
table = dynamodb.Table("Fortunes")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    Fortune = table.get_item(
        Key = {
            "Fortune":"You will prosper!",
            "ID":2
        }
    )["Item"]["Fortune"]
    return render_template("index.html", Fortune=Fortune)
    

if __name__ == "__main__":
    app.run("0.0.0.0",port=8080)

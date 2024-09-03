from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("I am testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("I am testing the logging module")
    return "Testing debug"

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, Response,  send_from_directory, abort, redirect, jsonify, session
import os
import datetime
from google.cloud import storage


bucketName = os.environ.get('BUCKET_NAME','YOU_FORGOT_TO_SET_THE_BUCKET_NAME_ENV_VAR')
client = storage.Client()
bucket = client.get_bucket(bucketName)

app = Flask(__name__, static_url_path='')


@app.route('/public/<path:path>')
def send_file(path):
    return send_from_directory('public', path)


@app.route('/getSignedURL')
def getSignedURL():
    filename = request.args.get('filename')
    action = request.args.get('action')
    blob = bucket.blob(filename)
    url = blob.generate_signed_url(
        expiration=datetime.timedelta(minutes=60),
        method=action, version="v4")
    return url


@app.route('/')
def signedurl():
    return render_template('signedurl.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

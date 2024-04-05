from flask import Flask, request, render_template, redirect, url_for
import boto3
import os

app = Flask(__name__)

# Configure your S3 bucket name
S3_BUCKET = 'test-bucket583749'
AWS_REGION = 'us-east-1'

s3_client = boto3.client('s3', region_name=AWS_REGION)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'csvfile' not in request.files:
        return redirect(request.url)
    file = request.files['csvfile']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        s3_client.upload_fileobj(file, S3_BUCKET, filename)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


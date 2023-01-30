from bottle import Bottle, request, template

app = Bottle()


@app.route('/upload', method='POST')
def do_upload():
    file = request.files.get('file')
    if file:
        file.save(file.filename)
        return 'File Uploaded'
    else:
        return 'No file selected'


@app.route('/')
def upload_form():
    return template('upload_form')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

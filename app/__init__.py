from flask import Flask
import nltk

print 'Downloading nltk.punkt'
# nltk.download('punkt')
print 'Download completed'

UPLOAD_FOLDER = 'client_uploads'
RESULT_FOLDER = 'results'
ALLOWED_EXTENSIONS = set(['txt']) # pdf, doc, epub, fb2, kindle etc.

app = Flask(__name__) # here 'app' is just a variable name
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024

from app import views # but here 'app' is a package name
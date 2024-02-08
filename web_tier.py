# -*- coding: utf-8 -*-


from flask import Flask

app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET','POST'])
def home():
    return "Hello, World! This is Server 1."

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7002)

# import os
# from flask import Flask, request, render_template_string
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Define the upload folder and allowed file extensions
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# # Ensure the upload folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # Function to check if a file has an allowed extension
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # HTML code for the upload form
# upload_form = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Image Upload</title>
# </head>
# <body>
#     <h1>Upload an Image</h1>
#     <form method="POST" action="/upload" enctype="multipart/form-data">
#         <input type="file" name="file">
#         <input type="submit" value="Upload">
#     </form>
# </body>
# </html>
# """

# # Route to display the upload form
# @app.route('/')
# def index():
#     return render_template_string(upload_form)

# # Route to handle image uploads
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file part"
    
#     file = request.files['file']

#     if file.filename == '':
#         return "No selected file"

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(UPLOAD_FOLDER, filename))
#         return "File uploaded successfully"
#     else:
#         return "Invalid file format. Allowed formats are: " + ', '.join(ALLOWED_EXTENSIONS)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=7080)






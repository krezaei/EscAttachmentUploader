
from flask import Flask, request, render_template
import json

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.


@app.route('/')
def index():
     data = {
        "title": 'Home Page',
         "msg":'Hello World from Flask for Python !!!',
         "me": 'Kaveh'
         }
     return render_template('index.html')

#@app.route('/', methods=['POST'])
#def my_form_post():
#    text = request.form['text']
#    processed_text = text.upper()
#    return processed_text

@app.route('/parse_data', methods=['GET', 'POST'])
def parse_data():
    if request.method == "POST":

       # dataform = str(request.data).strip("'<>() ").replace('\'', '\"')
        data = json.loads(request.data)
       # result = request.form

        
        #print(result)
    return render_template("result.html",data = data)



if __name__ == '__main__':
#    # Run the app server on localhost:4449
    app.run('localhost', 5555)


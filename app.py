from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    f = open("storage.txt","a")
    f.write(text+"\n")
    f.close()
    f = open("storage.txt","r")
    contents = f.read()
    f.close()    
    #print(contents)
    return contents

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8000)
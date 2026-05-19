from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello_world(name=None):
    if name==None:
        return "Hello, World! 20220502test"
    return "Hello"+name+"!"
	
@app.route('/hello/')
def hello():
    return 'Hello, Worldasdfsadfasdf'
	
@app.route('/hello2/')
def hello2():
    return 'Hello2, asfsaasdf'
	
@app.route('/eric/')	
def eric():
    return 'eric, asfsaasdf'

@app.route('/add/chi=<num1>&math=<num2>',methods=['GET'])	
def add(num1,num2):
    print(num1 + num2)
    print("add test")
    return str(int(num1) + int(num2))
	
@app.route('/sony/<name>')	
def hello_name(name): 
    return 'hello %s!'%name

@app.route('/page/<path:url>')	
def show_url(url): 
    return 'url %s!'%url

@app.route('/blog/<int:postID>')	
def show_blog(postID): 
    return 'Blog Number %d!'%postID

@app.route('/rev/<float:revNO>')	
def revision(revNO): 
    return 'Revision Number %f!'%revNO

@app.route('/admin')	
def hello_admin(): 
    return 'Hello Admin'

@app.route('/guest/<guest>')	
def hello_guest(guest): 
    return 'Hello %s as Guest' %guest


@app.route('/user/<name>')	
def user(name): 
    if name=="admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))


	
if __name__=="__main__":
	app.run(debug=True,host='0.0.0.0',port='8080')
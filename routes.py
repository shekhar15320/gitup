from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'RAJAT'}
    return '''
<html>
    <head>
       <title>shekharraj Page - Microblog</title>
    </head>
    <body>
       <h1>Hello, ''' + user['username'] + '''!</h1>     
    </body>
</html>'''

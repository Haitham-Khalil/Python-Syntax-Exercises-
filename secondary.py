from flask import Flask

skills_app=Flask(__name__)

@skills_app.route("/")
def homepage():
    return """


 <p>This is the web page of the course</p>
 <p>The slides are available <a href="slides">here</a></p>
"""

@skills_app.route("/slides")
def about():
    return """<html>
 <head>
 <title>SA 2020/2021</title>
 </head>
 <body>
 <h1>Slides</h1>
 <ul>
 <li>Introduction</li>
 <li>What is Software?</li>
 </ul>
 <p>Back to <a href="/">home</a>.</p>
 </body>
</html>"""

if __name__=="__main__":
    skills_app.run(debug=True,port=9000)
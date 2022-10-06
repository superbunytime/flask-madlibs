from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# @app.route('/htmlsnippet')
# def show_html():
#     return """
#       <html>
#       this is a simple html snippet
#       </html>
#       """

# @app.route('/anything')
# def show_html2():
    # return """
    #       <!DOCTYPE html>
    #   <html>
    #     <head>
    #       <title>Hi There!</title>
    #     </head>
    #     <body>
    #       <h2>Hi over there!</h2>
    #       <form action="/greet">
    #         What's your name? <input name="person">
    #         <button>Go!</button>
    #       </form>
    #     </body>
    #   </html>
    #   """


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
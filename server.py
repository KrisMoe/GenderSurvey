from flask import Flask, request, render_template

def create_app():
    app = Flask(__name__)
    
    return app
app = create_app()
@app.route("/")
def home():
    questions = [
        {"id":"question-1","type":"input-text","options":[
            {"id":"question-1-input", "name":"input-1"},
           
       ]
       },
       {"id":"question-2","type":"radio-text","options":[
            {"id":"question-2-trumpet", "name":"Trumpet"},
            {"id":"question-2-clock", "name":"Clock"},
            {"id":"question-2-fish", "name":"Fish"}
       ]
       },
        {"id":"question-3","type":"checkbox-text","options":[
            {"id":"question-3-dawn", "name":"Dawn"},
            {"id":"question-3-dusk", "name":"Dusk"},
            {"id":"question-3-day", "name":"Day"},
            {"id":"question-3-night", "name":"Night"}
       ]
       },    
       {"id":"question-4","type":"color","options":[
            {"id":"question-4-color", "name":"color"},
            
       ]
       },    
       {"id":"question-5","type":"time","options":[
            {"id":"question-5-time", "name":"time"},
            
       ]
       },
       {"id":"question-6","type":"date","options":[
            {"id":"question-6-dates", "name":"time"},
            
       ]
       },
       {"id":"question-7","type":"range","options":[
            {"id":"question-6-range", "name":"number"},
            
       ]
       }      

    ]

    return render_template('questions.html',questions=questions)
@app.route("/createpolygon")
def createpolygon():
    return render_template('createpolygon.html')
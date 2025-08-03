from flask import Flask, render_template
app = Flask(__name__)

POSITIONS = [
    {
        'id': 1,
        'title': 'Flock Member',
        'location': 'Durgapur',        
    },
    {
        'id': 2,
        'title': 'Avian Manager',
        'location': 'Katpadi',        
    },
    {
        'id': 3,
        'title': 'Flock Member',
        'location': 'Kolkata',        
    },
    {
        'id': 4,
        'title': 'Seed Specialist',
        'location': 'Tettu',        
    }
    
]

@app.route("/")
def hello():
    return render_template('home.html', positions=POSITIONS,)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)

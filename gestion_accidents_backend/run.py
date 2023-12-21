from app import app

@app.route('/')
def hello() :
    return "hello"
if __name__ == '__main__':
    app.run(debug=True,port=5000)
from app import create_app
from app.controllers import *

app = create_app()

@app.route("/agenda/<int:id>", methods=['GET', 'POST', 'PUT'])
def users(id):
    return agenda_por_userid(id)

if __name__ == '__main__':
    app.run(debug = True)
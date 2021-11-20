from main import v1_blueprint
from main.resources import create_app

app = create_app()
app.register_blueprint(v1_blueprint)

if __name__ == "__main__":
    app.run(port=5000)

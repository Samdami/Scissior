from api import create_app
from flask_sqlalchemy import SQLAlchemy
from api.config.config import config_dict

app = create_app()

if __name__ == "__main__":
    app.run()
    # app.run(port=8000)

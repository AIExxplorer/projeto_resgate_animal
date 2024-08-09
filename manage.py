from flask import Flask
from flask_migrate import Migrate
from app import create_app, db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    import sys
    from flask.cli import main

    sys.argv[0] = 'flask'
    main(as_module=True)
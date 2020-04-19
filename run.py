from app.api import app
import settings


if __name__ == '__main__':
    app.run(settings.DEBUG)

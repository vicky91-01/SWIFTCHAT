# SWIFTCHAT

SWIFTCHAT is a real-time chat application built with Django and WebSockets using Django Channels.

## Features

- Create or join chat rooms
- Real-time messaging with WebSockets
- Room-based message history stored in the database
- Django templates for the UI
- SQLite database support for local development

## Tech Stack

- **Backend:** Python, Django
- **Real-time layer:** Django Channels, Daphne, WebSockets
- **Frontend:** JavaScript, HTML, CSS
- **Database:** SQLite

## Project Structure

- `chatapp/` — main chat application logic
- `swiftchat/` — Django project configuration
- `templates/` — HTML templates for the UI
- `staticfiles/` — collected static assets
- `db.sqlite3` — local SQLite database

## Requirements

Dependencies are listed in `requirements.txt`.

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/vicky91-01/SWIFTCHAT.git
   cd SWIFTCHAT
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser
   ```bash
   http://127.0.0.1:8000/
   ```

## Deployment Instructions

This project is configured for Django Channels and ASGI, so your deployment should support WebSockets.

### 1) Production settings

Before deploying, update `swiftchat/settings.py`:

- Set `DEBUG = False`
- Add your production domain to `ALLOWED_HOSTS`
- Update `CSRF_TRUSTED_ORIGINS` with your live HTTPS domain
- Set a secure `SECRET_KEY` using environment variables

Example:

```python
DEBUG = False
ALLOWED_HOSTS = ["your-domain.com", "www.your-domain.com"]
CSRF_TRUSTED_ORIGINS = ["https://your-domain.com", "https://www.your-domain.com"]
```

### 2) Database

The project currently uses SQLite for development. For production, use a production-ready database such as PostgreSQL.

Run migrations after updating the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3) Static files

Collect static files before deployment:

```bash
python manage.py collectstatic
```

### 4) ASGI server

Because the app uses WebSockets, deploy it with an ASGI server instead of WSGI.

The project already uses:

```python
ASGI_APPLICATION = "swiftchat.asgi.application"
```

You can run the app locally with Daphne:

```bash
daphne -b 0.0.0.0 -p 8000 swiftchat.asgi:application
```

### 5) Channel layer

The current configuration uses `InMemoryChannelLayer`, which is fine for local development but not ideal for production.

For production deployment, configure a shared channel layer such as Redis.

Example direction:

- Install Redis
- Replace `InMemoryChannelLayer` with a Redis channel layer
- Point all app instances to the same Redis server

### 6) Example deployment flow

1. Push the code to your server or platform
2. Install dependencies
3. Set environment variables
4. Run migrations
5. Collect static files
6. Start the ASGI server
7. Confirm WebSocket connections are working

### 7) If using ngrok for testing

If you expose the app using ngrok, update:

- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`

in `swiftchat/settings.py` to match the ngrok URL.

## How It Works

- A user enters a username and room name on the home page.
- If the room does not exist, it is created automatically.
- Messages are sent in real time using Channels and WebSockets.
- Each message is stored in the `Message` model and shown inside the room.

## Models

### Room
- `room_name`: name of the chat room

### Message
- `room`: related chat room
- `sender`: username of the sender
- `message`: message text

## Notes

- The project is configured for local development with SQLite.
- WebSocket support is handled through `ASGI_APPLICATION` and Django Channels.
- If you use a tunnel such as ngrok, update `CSRF_TRUSTED_ORIGINS` in `swiftchat/settings.py`.

## Language Breakdown

- JavaScript — 46.9%
- CSS — 38.5%
- HTML — 9.7%
- Python — 4.9%

## License

No license has been specified yet.

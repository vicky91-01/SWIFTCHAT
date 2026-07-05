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

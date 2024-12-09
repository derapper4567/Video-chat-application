Video Chat Application

Welcome to the Video Chat Application! This application enables users to connect and communicate through real-time video and audio streaming using Django, WebSocket, Redis, and WebRTC. Perfect for personal chats, business meetings, or virtual gatherings.


Table of Contents
Features
Technologies Used
Installation
Usage
Configuration
Contributing
License
Contact


Features
Real-time video and audio communication
User authentication and profile management
Group video calls
Screen sharing capabilities
Chat functionality
Cross-platform compatibility (Web, Mobile)
User-friendly interface


Technologies Used
Frontend: HTML5, CSS3, JavaScript
Backend: Django, Django Channels
Database: SQLite or PostgreSQL
WebRTC: For real-time communication
Redis: For message brokering
WebSocket: For real-time event handling


Installation
To set up the Video Chat Application locally, follow these steps:

Clone the repository:

Copy code
git clone https://github.com/derapper4567/video-chat-app.git
cd video-chat-app

Set up a virtual environment
python -m venv venv
source venv/bin/activate


Install dependenccies
Copy code
pip install django channels channels_redis
Set up Redis:

Install Redis on your machine or use Docker:
docker run -p 6379:6379 -d redis
Run migrations:
python manage.py migrate

Run the application:
python manage.py runserver
Open your browser and navigate to http://localhost:8000 to access the application.

Usage
Sign Up / Log In: Create a new account or log in to your existing account.
Start a Video Call: Click on the "Start Call" button to initiate a video chat.
Invite Participants: Share the call link with others to join the conversation.
Use Features: Utilize screen sharing, chat, and other features during the call.
Configuration
You can customize various settings in the application by modifying the settings.py file. This includes database settings, Redis configuration, and WebSocket settings.

Contributing
We welcome contributions to the Video Chat Application! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or feedback, please reach out to:

asha.kisonga@eastc.ac.tz
GitHub: derapper4567
Thank you for using the Video Chat Application! We hope you enjoy connecting with others.

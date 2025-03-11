import os
import asyncio
import threading
import sys
from aiohttp import web

# Add the current directory to sys.path to allow importing the AdityaHalder module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Web server routes
routes = web.RouteTableDef()

@routes.get("/")
async def home(request):
    return web.Response(
        text="<h1>Genius-Userbot is Running!</h1><p>Visit <a href='https://t.me/AdityaServer'>@AdityaServer</a> for support.</p>",
        content_type="text/html"
    )

@routes.get("/health")
async def health_check(request):
    return web.Response(text="OK", status=200)

# Create web application
app = web.Application()
app.add_routes(routes)

# Function to start the userbot
def run_bot():
    from AdityaHalder.__main__ import main
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

# Start the bot if called directly
if __name__ == "__main__":
    # Start the bot in a background thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Start the web server in the main thread (if not running under gunicorn)
    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

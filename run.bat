echo Installing packages...

pip install python-dotenv
pip install requests
pip install asyncio
pip install -U discord.py-self

echo Packages installed!
echo Running the bot...

py bot.py
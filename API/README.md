# API Integration Portfolio

This is my portfolio project demonstrating **API integration**.  

I built a **Discord Bot** using the [Discord Developer Portal](https://discord.com/developers/applications) to generate a bot token and connect it to my Python code.  
The bot is able to check discounts of specific games on **Steam** by consuming the **Steam Store API**.

---

## 🔹 How It Works
The bot is created in the **Discord Developer Portal** and connected using a bot token. I wrote the bot using **Python** and the `discord.py` library. When a user types `/diskon` in the Discord server, the bot:  
   - Calls the **Steam Store API**:  
     ```
     https://store.steampowered.com/api/appdetails?appids=<APPID>
     ```
   - Fetches the game details (title, price, discount percentage).  
   - Returns the result back into the Discord chat.  

---

##  The Code
<img width="796" height="257" alt="Image" src="https://github.com/user-attachments/assets/8defcf8a-9450-4f73-bd55-cdc5239a8d83" />

---
##  Example of Steam API Response
<img width="789" height="384" alt="Image" src="https://github.com/user-attachments/assets/ee2c6a67-8db9-46fd-af03-acc3985b2df6" />

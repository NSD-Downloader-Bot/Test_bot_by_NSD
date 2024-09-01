from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try :
        await update.message.reply_text(f'Hello {update.effective_user.first_name}\n')
        print("sended")
    except Exception as e :
        print(f"An Error Occured!\nError : {e} \nPLZ report the bug on xxx Channel")
        
        
if __name__ == "__main__":
    
    app = ApplicationBuilder().token("7445051215:AAFop3_6HqLEvoUscwTJ4EikENtTvlvx3K4").build()


    ################## Handelers 
    app.add_handler(CommandHandler("start", start))
    
    ####### MAIN
    print("Bot is running...")
    app.run_polling()
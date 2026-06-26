import os
from dotenv import load_dotenv
load_dotenv()


from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from app.telegram.handlers import start, help_command, echo, upload_document, upload, list_documents

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )
    application.add_handler(MessageHandler(filters.Document.PDF,upload_document))
    application.add_handler(CommandHandler("upload",upload))
    application.add_handler(CommandHandler("list_documents",list_documents))
    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
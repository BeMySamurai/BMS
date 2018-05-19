import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class DBot:

    def main():

        login, password = '380664582704', '7285729BMS@'
        vk_session = vk_api.VkApi(login, password)
        vk = vk_session.get_api()
        vka = vk_session.auth()
        try:
            vk_session.auth()
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
    
        longpoll = VkLongPoll(vk_session)

        x = "Дикей"

        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW and event.from_chat:
             if event.text == x:
                vk.messages.send(
                    random_id=(),
                    chat_id=event.chat_id,
                    message='Мявк.'
                    )      
             
            if event.type == VkEventType.MESSAGE_NEW and event.from_user:
             if event.text == x:
                vk.messages.send(
                    random_id=(),
                    user_id=event.user_id,
                    message='Мявк..'
                    )
      
        return

    if __name__ == '__main__':
        main()

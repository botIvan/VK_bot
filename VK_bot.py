import vk_api
import random
import time

token = "c463f2cc8874fc33833ac178b141e6b471b89c32255bd23ac26d454bdea6535429a193ec0f1d868445a9a"


vk = vk_api.VkApi(token=token)

vk._auth_token()

greetings_by_user = ["Привет","привет","Привет!","привет!","Хай","хай","Хай!","хай!","Здарова","Здарова!","здарова","здарова!","дратути","дратути!","Дратути","Дратути!"]
goodbyes_by_user = ["Пока","пока","Пока!","пока!"]

dz = "дз нет"

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() in greetings_by_user:
                vk.method("messages.send", {"peer_id": id, "message": str(body.lower()), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == goodbyes_by_user:
                vk.method("messages.send", {"peer_id": id, "message": "пока((", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
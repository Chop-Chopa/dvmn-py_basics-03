from dotenv import load_dotenv
import smtplib
import os
load_dotenv()
massage_sample = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
massage_sample = massage_sample.replace("%website%","https://dvmn.org/profession-ref-program/ignatev2283/WuKkp/")
massage_sample = massage_sample.replace("%friend_name%","Данил")
massage_sample = massage_sample.replace("%my_name%","Евгений Игнатьев")
letter_yandex ="""From: ka1zeroi@yandex.ru
To: evgeny.ignatjev2016@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{0}""".format(massage_sample)
letter_yandex = letter_yandex.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(os.environ["LOGIN"] , os.environ["PASSWORD"])
server.sendmail("ka1zeroi@yandex.ru" , "ka1zeroi@yandex.ru" ,letter_yandex)
server.quit()



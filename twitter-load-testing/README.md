# Отчёт о нагрузочном тестировании

## Исходные данные

**Источник нагрузки:** Яндекс.Танк

**Мишень:** twitter.com

**Пользовательские сценарии:**
- кто-то открывает главную страницу
- кто-то ищет людей с именем *julia*
- кто-то ищет фотографии с котиками
- кто-то ищет по хэш-тегу *#novosibirsk*
- кто-то пытается восстановить свой пароль
- кто-то хочет зарегистрироваться

**Сценарий тестирования:** 
- сначала в течение 1 минуты подаём линейно-возрастающую нагрузку с 1 до 100 RPS
- затем сохраняем нагрузку в 100 RPS и подаём её в течение еще 1 минуты


## Результаты
![Graphics](http://dl1.joxi.net/drive/0006/3401/458057/141112/3bb0f25cdb.jpg)

## Выводы
* График отражает реальность. Чем больше пользователей, тем дольше идет ответ. Для постоянной нагрузки - практически постоянное время ответа. 
* Судя по анализу статус-кодов ответов, записанных в журналы Танка, испытуемый веб-сервис принял и корректно обработал 99,99% запросов (код 302), и лишь 0,01% запросов не были обработаны.
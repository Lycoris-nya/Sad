import datetime
import time
import random

severity = ["INFO", "WARN", "ERROR"]
httpStatus = {'INFO': ["200", "201"], 'WARN': ["400", "401", "402"], 'ERROR': ["501", "502", "503"]}
user = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8","user9", "user10"]
resourcePath = ["/api/books/", "/api/films/", "/api/manga/", "/api/anime/", "/api2/cats/","/api2/dogs/"]

while True:
    date = datetime.datetime.now()
    severityNow = random.randrange(0, 3)
    NewLog = date.strftime("%Y.%m.%d") + " " + severity[severityNow]
    NewLog += " " + httpStatus.get(severity[severityNow])[random.randrange(0, len(httpStatus.get(severity[severityNow])))]
    NewLog = NewLog + " " + user[random.randrange(0, len(user))] + " " + str(random.randrange(1, 101))
    NewLog = NewLog + " " + resourcePath[random.randrange(0, len(resourcePath))] + "\n"
    result = open("result", 'a')
    result.write(NewLog)
    result.close()
    time.sleep(10)
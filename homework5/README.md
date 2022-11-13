## Домашнее задание №5: Backend: Linux

#### Bash script

##### Общее количество запросов (1 балл)

    Реализация - cat access.log | wc -l > bash_result
    Результат: 225133
    
##### Общее количество запросов (1 балл)

    Реализация - cat access.log | awk '{print$6}' | sort | uniq -c | sort -n | awk '{print$2" "$1}' >> bash_result
    Результат: 
    "g369g=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2bfCIpOztlY2hvKCJlNTBiNWYyYjRmNjc1NGFmMDljYzg0NWI4YjU4ZTA3NiIpOztlY2hvKCJ8PC0iKTs7ZGllKCk7GET 1
    "PUT 6
    "HEAD 528
    "POST 102503
    "GET 122095
##### Топ 10 самых частых запросов (1 балл)

    Реализация - cat access.log | awk '{print$7}' | sort | uniq -c -d | sort -n -r|head -10  |awk '{print$1" "$2}' >> bash_result
    Результат: 
    103932 /administrator/index.php
    26336 /apache-log/access.log
    6940 /
    4980 /templates/_system/css/general.css
    3199 /robots.txt
    2356 http://almhuette-raith.at/administrator/index.php
    2201 /favicon.ico
    1644 /wp-login.php
    1563 /administrator/
    1287 /templates/jp_hotel/css/template.css

##### Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой (1 балл)

    Реализация - cat access.log | awk '{print$1" "$9" "$10" "$7}' |  awk '$2=="404"||$2=="400"||$2=="403"||$2=="405"||$2=="412"' | sort -n -r -k 3 | head -5 >> bash_result
    Результат: 
    189.217.45.73 404 1417 /index.php?option=com_phocagallery&view=category&id=7806&Itemid=53
    189.217.45.73 404 1417 /index.php?option=com_phocagallery&view=category&id=4025&Itemid=53
    189.217.45.73 404 1417 /index.php?option=com_phocagallery&view=category&id=%28SELECT%20%28CASE%20WHEN%20%289168%3D4696%29%20THEN%209168%20ELSE%209168%2A%28SELECT%209168%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%29%20END%29%29&Itemid=53
    189.217.45.73 404 1417 /index.php?option=com_phocagallery&view=category&id=%28SELECT%20%28CASE%20WHEN%20%281753%3D1753%29%20THEN%201753%20ELSE%201753%2A%28SELECT%201753%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%29%20END%29%29&Itemid=53
    95.82.195.206 404 1397 //index.php?option=com_users&view=registration

##### Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой (1 балл)

    Реализация - cat access.log | awk '{print$1" "$9}' | sort -n -k 2 | uniq -c | grep ' 500' | sort -n -r -k1 | head -5 | awk '{print$2" "$1}'>> bash_result
    Результат: 
    189.217.45.73 225
    82.193.127.15 4
    91.210.145.36 3
    198.38.94.207 2
    195.133.48.198 2

Результат работы скрипта записывается в файл bash_result

#### Python script

##### Общее количество запросов (1 балл)

    Реализация: 
    print('\n')
    nginx_re = re.compile(r"(?P<ip>\d+\.\d+\.\d+\.\d+) - - (?P<datetime>\[.+\]) \"(?P<method>\w+) (?P<url>.+?) (?P<protocol>.+?)\" (?P<responce>\d+) (?P<size>\d+)")
    log = []
    exclude = 0
    with open("access.log") as f:
        for row in f.readlines():
            if parsed := nginx_re.findall(row):
                log.append(parsed)
            else:
                exclude+=1

    Результат: 223799
    
##### Общее количество запросов (1 балл)

    Реализация:
    count, post, get, head, put ,other = 0, 0, 0, 0, 0, 0
    for i in range(len(log)):
        count+=1
        if log[i][0][2]=="POST":
            post +=1
        elif log[i][0][2]=="GET":
            get+=1
        elif log[i][0][2]=="HEAD":
            head+=1
        elif log[i][0][2]=="PUT":
            put+=1
        else:
            other+=1
    print(f"Общее число запросов - {count}",'\n') 
    print(f"Количество запросов POST - {post}") 
    print(f"Количество запросов GET - {get}") 
    print(f"Количество запросов HEAD - {head}") 
    print(f"Количество запросов PUT - {put}") 
    print(f"Количество запросов OTHER - {other}",'\n') 
    Результат: 
    Количество запросов POST - 102500
    Количество запросов GET - 120765
    Количество запросов HEAD - 528
    Количество запросов PUT - 6
    Количество запросов OTHER - 0 
##### Топ 10 самых частых запросов (1 балл)

    Реализация:
    buf = []
    counter= []
    for i in range(len(log)):buf.append(log[i][0][3])
    uniq = numpy.unique(buf)
    for i in range(len(uniq)):
        if buf.count(uniq[i])>1000:counter.append(buf.count(uniq[i]))
    counter.sort()
    for i in range(len(uniq)):
        if buf.count(uniq[i])>=min(counter[-10:]):print(uniq[i],"\n",buf.count(uniq[i]))
    print('\n')
    Результат: 
    / 
     6939
    /administrator/ 
     1563
    /administrator/index.php 
     103929
    /apache-log/access.log 
     26333
    /favicon.ico 
     2201
    /robots.txt 
     3198
    /templates/_system/css/general.css 
     4980
    /templates/jp_hotel/css/template.css 
     1240
    /wp-login.php 
     1644
    http://almhuette-raith.at/administrator/index.php 
     2356


##### Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой (1 балл)

    Реализация:
    ips = []
    ips_counter = []
    for i in range(len(log)):
        if log[i][0][5]=="500":ips.append(log[i][0][0])  
    uniq_ips = numpy.unique(ips)
    for i in range(len(uniq_ips)):
        ips_counter.append(ips.count(uniq_ips[i]))
        if ips_counter[i]>min(ips_counter):print(uniq_ips[i],'\n',ips_counter[i])
    Результат: 
    189.217.45.73 
     225
    194.87.237.6 
     2
    195.133.48.198 
     2
    198.38.94.207 
     2
    82.193.127.15 
     4
    91.210.145.36 
     3

### Итог

Парсинг и работа с логами проще реализуема с помощью bash, поскольку там существуют утилиты, способные упростить работу в несколько раз, при условии, что ты их знаешь. С Python все немного иначе. В моем случае, работа с ним была в разы сложнее, скорее всего из-за неправильного подхода к задаче. Реализация на python супер не оптимизированная, поскольку я работал чисто со списками. Скорее всего нужно было использовать lambda функции и map. 
Хотелось бы, при условии что проверяющему не лень, уже после мерджа, увидеть оптимизированный код, что бы в дальнейшем иметь прецедент качественного кода
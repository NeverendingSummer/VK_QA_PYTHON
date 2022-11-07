import re
import numpy

print('\n')
nginx_re = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+) - - (?P<datetime>\[.+\]) \"(?P<method>\w+) (?P<url>.+?) (?P<protocol>.+?)\" (?P<responce>\d+) (?P<size>\d+)")
log = []
exclude = 0
with open("access.log") as f:
    for row in f.readlines():
        if parsed := nginx_re.findall(row):
            log.append(parsed)
        else:
            exclude += 1

count, post, get, head, put, other = 0, 0, 0, 0, 0, 0
for i in range(len(log)):
    count += 1
    if log[i][0][2] == "POST":
        post += 1
    elif log[i][0][2] == "GET":
        get += 1
    elif log[i][0][2] == "HEAD":
        head += 1
    elif log[i][0][2] == "PUT":
        put += 1
    else:
        other += 1
print(f"Общее число запросов - {count}", '\n')
print(f"Количество запросов POST - {post}")
print(f"Количество запросов GET - {get}")
print(f"Количество запросов HEAD - {head}")
print(f"Количество запросов PUT - {put}")
print(f"Количество запросов OTHER - {other}", '\n')

print("Топ 10 самых частых запросов\n")
buf = []
counter = []
for i in range(len(log)): buf.append(log[i][0][3])
uniq = numpy.unique(buf)
for i in range(len(uniq)):
    if buf.count(uniq[i]) > 1000: counter.append(buf.count(uniq[i]))
counter.sort()
for i in range(len(uniq)):
    if buf.count(uniq[i]) >= min(counter[-10:]): print(uniq[i], "\n", buf.count(uniq[i]))
print('\n')

print("Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n")
ips = []
ips_counter = []
for i in range(len(log)):
    if log[i][0][5] == "500": ips.append(log[i][0][0])
uniq_ips = numpy.unique(ips)
for i in range(len(uniq_ips)):
    ips_counter.append(ips.count(uniq_ips[i]))
    if ips_counter[i] > min(ips_counter): print(uniq_ips[i], '\n', ips_counter[i])

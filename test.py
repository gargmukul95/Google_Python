import pprint
import re
import operator

per_user = {}
error = {}

with open('syslog.log') as f:
    lines = f.readlines()
    # pprint.pprint(lines)
    for line in lines:
        s = re.search(r'ticky: ERROR: ([\w ]*)', line)
        # print(line)
        s2 = re.search(r'ticky: ([\w]*): [\w ]*[\[#\d\]]*? \(([\w]*)\)', line)
        if s is not None:
            if s[1] not in error.keys():
                error[s[1]] = 1
            elif s[1] in error:
                error[s[1]] += 1
        if s2 is not None:
            if s2[2] not in per_user.keys():
                per_user[s2[2]] = {}
                per_user[s2[2]]['INFO'] = 0
                per_user[s2[2]]['ERROR'] = 0
            if s2[1] == 'INFO':
                per_user[s2[2]]['INFO'] += 1
            if s2[1] == 'ERROR':
                per_user[s2[2]]['ERROR'] += 1
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items())
error.insert(0,("Error", "Count"))
# per_user.insert(0,  ("Username", "INFO", "ERROR"))

# print(per_user, '\n', error)

with open('user_statistics.csv', 'w') as file:
    file.write("Username,INFO,ERROR\n")
    for i in per_user:
        c, d = i
        file.write(str(c) + ',' + str(d['INFO']) + ',' + str(d['ERROR']) + '\n')

with open('error_message.csv', 'w') as f:
    for err in error:
        a, b = err
        f.write(str(a) + ',' + str(b) + '\n')


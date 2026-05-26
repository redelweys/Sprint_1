data = ('1h 45m,360s,25m,30m 120s,2h 60s')
total_minutes = 0

for time in data.split(','):
    time_parts = time.split()
    for part in time_parts:
        if 'h' in part:
            minutes = int(part.replace('h', ''))
            total_minutes += minutes*60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            total_minutes += minutes
        else:
            minutes = int(part.replace('s', ''))
            total_minutes += minutes//60

print('Итоговое количество минут:', total_minutes)
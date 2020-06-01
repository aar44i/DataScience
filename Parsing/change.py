import collections

ctr_dict = collections.defaultdict(list)
countries = ['Singapore', 'Italy', 'Greece', 'Portugal', 'Chile', 'South Africa'] ## Список с названиями стран
populations = [5781110, 60588366, 10741165, 10276617, 17789267, 54956900] ## Список с населениями стран
areas = [725.1, 301340, 131957, 92225.61, 756950, 1219912] ## Список с площадьми стран

for i in range(0,len(countries)):
    ctr_dict[countries[i]].append(( populations[i] / areas[i] ))
    std = {countries[i]:( populations[i] / areas[i] )}
print((ctr_dict))
print(min(ctr_dict))
print(max(ctr_dict))
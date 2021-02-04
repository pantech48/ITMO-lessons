import json


def http_headers_to_json(http, jsn):
    with open(http) as f:
        s = (f.read()).strip('\n ')

    lst_1 = s.split('\n') # список заголовков
    heading = lst_1[0]
    head_lst = heading.split()

    # todo: Преобразовать запрос/ответ заголовок в словарь
    if not heading.startswith('HTTP'):
        version = {
            "method": head_lst[0],
            "uri": head_lst[1],
            "protocol": head_lst[2]
        }
    else:
        if len(head_lst) < 3:
            version = {
                "protocol": head_lst[0],
                "status_code": head_lst[1],
            }
        else:
            msg = ' '.join(head_lst[2:])
            version = {
                "protocol": head_lst[0],
                "status_code": head_lst[1],
                "status_message": msg,
            }

    # todo: Преобразовать остальные заголовки в словарь

    wo_head = lst_1[1:] # список заголовков без запроса/ответа

    for i,p in enumerate(wo_head):
        wo_head[i] = p.split(": ", 1)

    # todo: найти одинаковые ключи и объеденить их значения

    def unique_keys(iterable):
        for index_one, item_one in enumerate(iterable):
            for index_two, item_two in enumerate(iterable):
                if not index_one == index_two:
                    if item_one[0] == item_two[0]:
                        item_one.append(item_two[1])
                        iterable.pop(index_two)
                        values = list(item_one[1:])      
                        key = item_one[:1]
                        key.insert(1, values)
                        iterable[index_one] = key
        return iterable

    unique_keys(wo_head)          
    wo_head_dict = dict(wo_head) # словарь (заголовок: значение)
    version.update(wo_head_dict)


    with open(jsn, 'w') as a:
            json.dump(version, a)

















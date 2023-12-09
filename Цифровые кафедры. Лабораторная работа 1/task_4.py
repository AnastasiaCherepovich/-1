users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
set_=set(users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dic_={"Общее количество":len(users),"Уникальные посещения":len(set_)}
print(dic_)
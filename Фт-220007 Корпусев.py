import logging
# Добавление логирования
logging.basicConfig(filename='num.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

logger = logging.getLogger('logger')
logger = logging.LoggerAdapter(logger,{'app': 'тестовое приложение'})
# Добавление списков
num = [] # Мешок с бочонками
numdel = [] # Отложенные в сторону бочонки
while True:
    logger.info('Программа запущена')
    try:
        N = int(input('Введите количество бочек: ')) # Ввод количества бочонков в мешке(количества элементов для списка num)
        logger.info(f'Пользователь ввел количество бочек: {N}')
        # Добаление элементов в список num
        for i in range(1, N+1):
            num.append(i)
        while True:
            try:
                c = int(input('Введите количество бочек, которые хотите вытянуть и убрать в сторону: ')) # Ввод количества бочонков, которые надо вытянуть и убрать в сторону
                logger.info(f'Пользователь ввел количество бочек,которые надо вытянуть и убрать в сторону: {c}.')
                # Проверка правильного ввода
                if c > 0 and (N > c or N == c):
                    while True:
                        # По запросу пользователя производится удаление элементов из списка num и добавление этих же элементов в список numdel
                        for i in range(c):
                            n = int(input('Введите номер бочонка, который хотите вытянуть и убрать в сторону: '))
                            logger.info(f'Пользователь ввел номер бочонка: {n}')
                            if n in num:
                                num.remove(n)
                                numdel.append(n)
                                logger.info(f'Пользователь вытянул и убрал бочонок {n} в {numdel}.')
                            else:
                                print('Этого бочонка нет в мешке!')
                                logger.info(f'Бочонка {n} нет в мешке!')
                        # Проверка правильности ввода 
                        if c != len(numdel):
                            logger.error(f'Количество бочонков, которое пользователь убрал в {numdel} не равно {c}.')
                            num.clear()
                            numdel.clear()
                            for i in range(1, N+1):
                                num.append(i)
                            print('Были введены неверные значения!')
                            input('\n Нажмите ENTER чтобы начать заново.')
                            logger.error('Выбор бочонков производится заново!')
                            continue
                        else:
                            break
                else:
                    print('Неверное значение!')
                    logger.error('Данные введены некоректно!')
                    continue
                break
            except ValueError:
                print('Неверное значение!')
                logger.error('Данные введены некоректно!')
                continue  
    except ValueError:
        print('Неверное значение!')
        logger.error('Данные введены некоректно!')
        continue
    break
# Вывод элементов списка numdel на экран
input('\nНажмите ENTER чтобы чтобы вывести номера бочонков, убранных в сторону, на экран.')
for i in numdel:
     print(i)  
logger.info('Программа завершила работу.')   
       

        

        



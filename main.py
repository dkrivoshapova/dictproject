def main():
    print('''Доступные операции:
    1. Регистрация новых пользователей.
    2.Снятие наличных.
    3.Внесение наличных.
    4.Переводы клиентам банка.''' )
    print('''Параметры ввода:
    1.Для регистрации новых пользователей введите любую команду 2-3
    2.Снятие наличных: withdrow/w и сумму через пробел
    3.Внесение наличных: deposit/d и сумму через пробел
    4.Перевод: transfer/t Ваше имя, имя получателя и сумма перевода''')
    d = {}
    actions(d)


def actions(d):
    n = inp(d)
    l = len(n)
    if l == 3:
        if n[0][0] == 'w':
            d[n[1]] = withdraw(int(d[n[1]]), int(n[2]))
        else:
            d[n[1]] = deposit(int(d[n[1]]), int(n[2]))

    elif l == 4:
        print('Перевод от',n[1],'для',n[2],'в размре',n[3],' рублей' )
        d[n[1]],d[n[2]]=transfer(int(d[n[1]]), int(d[n[2]]), int(n[3]))
    print(n[1], ', Ваша операция выполнена.Баланс:', d[n[1]])
    return actions(d)


def inp(d):
    n = input().lower().split()
    if len(n) < 2 or len(n) > 4:
        print('Некорректный ввод')
        return inp(d)
    if n[0][0] in 'bwdt':
        if n[1] in d:
            return n
        if n[2] not in d and len(n)==4:
            print('Пользователь',n[2], 'не является клиентом банка. Перевод невозможен')
        return problem(d, n)
    print('Некорректное имя операции.Попробуйте снава')
    return inp(d)


def problem(d, n):
    print('Ваше имя не найдено в базе данных.')
    i = input('Отправьте 0 для повторной попытки или 1 для подтвержения создания нового счета')
    if i == '1':
        d[n[1]] = 0
        print('Ваш аккаунт успешно создан.Теперь вам доступно снятие, внесения наличных и переводы другим клиентам')
    return actions(d)

def withdraw(user_s, s):
    if user_s > s:
        user_s -= s
        return user_s
    else:
        print('На вашем счету недостаточно средств.Повторите попытку')
        return user_s


def deposit(user_s, s):
    user_s += s
    return user_s


def transfer(user1_s, user2_s, s):
    if user1_s >= s:
        user2_s += s
        user1_s -= s
        return user1_s, user2_s
    print('Недостаточно средств. Ваш баланс', user1_s, 'рублей.')
    return None


if __name__ == '__main__':
    main()

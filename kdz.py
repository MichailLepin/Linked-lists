# Лепин Михаил вариант 2 (linear singly linked list with head and tail)
NEXT = 1
VALUE = 0


def add_to_back_2(value, head, tail):
    item = [value, None]
    if head is None:
        head = item
    else:
        tail[NEXT] = item
    tail = item
    return head, tail


print('Функция добавления в конец:')
head = tail = None
head, tail = add_to_back_2(10, head, tail)
head, tail = add_to_back_2(20, head, tail)
head, tail = add_to_back_2(30, head, tail)
print(head, tail)
print()
# Этот head более не используется


def add_to_front_2(value, head, tail):
    item = [value, None]
    if tail is None:
        tail = item
    item[NEXT] = head
    head = item
    return head, tail


print('Функция добавления в начало:')
head = tail = None
head, tail = add_to_front_2(10, head, tail)
head, tail = add_to_front_2(20, head, tail)
head, tail = add_to_front_2(30, head, tail)
print(head, tail)
print()
# Далее все функции будут возвращать значения по этому head


def one_by_one_2(head):
    value = head
    while value is not None:
        print(value[VALUE])
        value = value[NEXT] # я не возвращаю и не запрашиваю tail, так как он не влияет на результат



print('Функция вывода элементов:')
one_by_one_2(head)
print()


def get_by_index(index, head):
    internal_index = 0
    value = head
    while value is not None:
        if internal_index == index:
            return (value[VALUE])
        internal_index += 1
        value = value[NEXT]
    if value is None:
        print('Введен некорректный индекс, функция вернет None, попробуйте снова')  # Я не возвращаю tail


print('Функция нахождения элемента по индексу:')
index = int(input('Введите необходимый индекс: '))
print(get_by_index(index, head))
print()


def remove_from_end(head):
    value = head
    output_head = None
    while value is not None:
        item_value = [value[VALUE], None]
        if output_head is None:
            output_head = item_value
        else:
            output_head[NEXT] = item_value
        value = value[NEXT]
        if value[NEXT] is None:
            break
    return output_head  # Я возвращаю здесь другую переменную вместо head,
    # чтоб не портить его для других функций


print('Функция удаления с конца:')
print(remove_from_end(head))
print()


def remove_from_front(head):
    value = head[NEXT]
    return value  # Я возвращаю здесь другую переменную вместо head, чтоб не портить его для других функций


print('Функция удаления с начала:')
print(remove_from_front(head))
print()


def search(searching_value, head):
    print(head)
    value = head
    while value is not None:
        print(value[VALUE], searching_value)
        if value[VALUE] == searching_value:
            print(True)
            break
        value = value[NEXT]
    if value is None:
        print(False)


print('Функция поиска значения:')
searching_value = int(input('Введите искомое значение:'))
search(searching_value, head)
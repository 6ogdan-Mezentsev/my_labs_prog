import re
ALL_ORDERS_PATH = 'orders.txt'
VALID_ORDERS_PATH = 'order_country.txt'
NOT_VALID_PATH = 'non_valid_orders.txt'


def get_all_orders(ALL_ORDERS_PATH):
    """Считывает данные о всех заказах в файле orders.txt"""
    with open(ALL_ORDERS_PATH, 'r') as file:
        orders = []
        for line in file:
            line = line.strip()
            order_data = line.split(';')
            orders.append(order_data)
    return orders


def check_valid_orders(orders):
    """Проверяет валидность заказов"""
    valid_orders = []
    not_valid_orders = []
    for order in orders:
        # Проверяем адрес
        if len(order[3].split('.')) != 4 or len(order[3].strip()) == 0:
            not_valid_orders.append([order[0], '1', order[3] if order[3].strip() else 'no data'])
            continue

        # Проверяем номер
        if not re.match(r"^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$", order[4]):
            not_valid_orders.append([order[0], '2', order[4]])
            continue

        valid_orders.append(order)

    return valid_orders, not_valid_orders


def get_country(address):
    """Возвращает страну из адреса заказа"""
    return address.split(',')[0].strip()


def sort_orders_by_country(valid_orders):
    """Сортирует заказы по стране"""
    sorted_orders = sorted(valid_orders, key=lambda x: (
        0 if "Россия" in get_country(x[3]) else 1,
        get_country(x[3])
    ))

    return sorted_orders


def write_orders_to_files(valid_orders, not_valid_orders, VALID_ORDERS_PATH, NOT_VALID_PATH):
    """Записывает valid_orders и not_valid_orders в разные файлы"""

    sorted_valid_orders = sort_orders_by_country(valid_orders)

    with open(VALID_ORDERS_PATH, 'w') as valid_file:
        for line in sorted_valid_orders:
            valid_file.write(';'.join(line) + '\n')

    with open(NOT_VALID_PATH, 'w') as not_valid_file:
        for line in not_valid_orders:
            not_valid_file.write(';'.join(map(str, line)) + '\n')


orders = get_all_orders(ALL_ORDERS_PATH)
valid_orders, not_valid_orders = check_valid_orders(orders)
write_orders_to_files(valid_orders, not_valid_orders, VALID_ORDERS_PATH, NOT_VALID_PATH)

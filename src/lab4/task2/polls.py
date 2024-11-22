class Respondent:
    """Класс для представления респондента."""
    def __init__(self, full_name, age):
        """Инициали"""
        self.name = full_name
        self.age = age

    def __repr__(self):
        """Позволяет выводить респондента в формате: "ФИО (возраст)"."""
        return f"{self.name} ({self.age})"


class AgeGroup:
    """Класс для распределения респондентов по возрастным группам."""
    def __init__(self, borders):
        self.borders = borders

        # группа 0-18 лет
        self.groups = {f"0-{self.borders[0]}": []}

        # остальные группы 19 - 100 лет
        for i in range(len(self.borders) - 1):
            self.groups[f"{self.borders[i] + 1}-{self.borders[i + 1]}"] = []

        # группа 100+ лет
        self.groups[f"{self.borders[-1] + 1}+"] = []

    def add_respondent(self, respondent):
        """Добавляет респондента в соответствующую возрастную группу."""
        # Перебираем возрастные группы
        for group_name, group in self.groups.items():
            if '+' in group_name:
                if respondent.age >= int(group_name[:-1]):
                    group.append(respondent)
                    break
            else:
                min_age, max_age = map(int, group_name.split('-'))
                if min_age <= respondent.age <= max_age:
                    group.append(respondent)
                    break


def read_age_borders():
    """Считывает введённые возрастные группы."""
    while True:
        try:
            borders = list(map(int, input("Введите границы возрастных групп через пробел: ").split()))
            return borders
        except ValueError:
            print("Пожалуйста, введите корректные целые числа, разделенные пробелами.")


def read_respondents():
    """Считывает введённых респондентов."""
    print("Введите респондентов в формате <ФИО>,<возраст>. Введите 'END' для завершения:")
    respondents = []
    while True:
        line = input().strip()
        if line.upper() == "END":
            break
        name, age = line.split(",", 1)
        respondents.append(Respondent(name.strip(), int(age.strip())))
    return respondents


def display_groups(groups):
    """Выводит группы с респондентами в отсортированном по возрасту порядке."""
    for group_name, group in sorted(groups.items(), reverse=True):
        # Сортировка по возрасту (по убыванию) и по имени (по возрастанию)
        sorted_group = sorted(group, key=lambda x: (-x.age, x.name))
        if sorted_group:
            print(f"{group_name}: {', '.join(map(str, sorted_group))}")


if __name__ == "__main__":
    # Считываем возрастные границы
    age_borders = read_age_borders()

    # Считываем респондентов
    respondents = read_respondents()

    # Создаём объект, пренадлежащий классу AgeGroup, для распределения респондентов по группам
    age_groups = AgeGroup(age_borders)

    # Добавление респондентов в группы
    for respondent in respondents:
        age_groups.add_respondent(respondent)

    # Выводим результат
    display_groups(age_groups.groups)

# 18 25 35 45 60 80 100
# Иванов Иван Иванович,34
# Петров Петр Петрович,45
# Сидоров Сидор Сидорович,19
# Кошельков Захар Брониславович,105
# Соколов Андрей Сергеевич,15
# end


import os
import time

def counting (n):

    if n < 1:
        return 0
    
    # Кэш с предыдущего расчета
    cache = []

    def get_sum (array):
        return sum(map(lambda x: x ** 2, array))
    
    # Cчитаем по порядку для 1-значных, потом для 2-значных, и т.д.
    for digit_count in range(1,n + 1):
        if digit_count == 1:
            cache = [1]*(digit_count*9 + 1)
        else:
            # Cоздаем матрицу (таблицу) и заполняем нулями
            table =  [[0] * (n*9+1) for _ in range(10)]
            # Заполняем таблицу значениями из кэша (каждую строку сдвигаем на 1)
            for string in range(10):
                for column in range (0, n*9+1):
                    if 0 <= column - string < len(cache):
                        table[string][column] = cache[column - string]
                    else:
                        table[string][column] = 0 
            # Cчитаем сумму по столбцам (инвертируем и считаем сумму по строкам)
            cache = [sum(column) for column in zip(*table)]
    
    return get_sum(cache)


def counting2 (n):

    if n < 1:
        return 0
    
    previous_result = []

    # Функция подсчета результата
    def get_sum (array):
        return sum(map(lambda x: x ** 2, array))

    # Cчитаем по порядку для 1-значных, потом для 2-значных, и т.д.
    for digit_count in range(1,n + 1):
        # Если 1-значные - то заполняем массив от 0 до 9 индекса единицами
        if digit_count == 1:
            previous_result = [1]*(digit_count*9 + 1)
        else:
            # Находим длину результирующего массива
            new_previous_result_length = digit_count*9+1
            # Определяем четный/нечетный
            even = new_previous_result_length%2 == 0
            # Задаем середину (относительно нее правая и левая часть будут зеркальными)
            middle = 0

            # Вычисляем середину
            if even:
                middle = new_previous_result_length//2
            else:
                middle = (new_previous_result_length+1)//2

            # Задаем сумму элементов массива до текущего индекса (кэшируем просто, чтобы каждый раз не считать)
            row_previous_sum = 0
            # Создаем половинный массив (заполнен нулями)
            half_result = [0]*middle

            # Заполняем половинный массив (каждый элемент - равен элемент из предыдущего результата + сумме всех предыдущих элементов строки)
            for index in range (0, middle):

                # Считаем только окно из 10 значений (от 0 до 9)
                if index >= 10:
                    # окно отъезжает и из суммы вычитаем первый элемент
                    row_previous_sum -= previous_result[index - 10]

                new_element = previous_result[index] + row_previous_sum
                half_result[index] = new_element
                row_previous_sum = new_element

            if even:
                # Если четный, то массив = половинка + зеркальная половинка
                previous_result = half_result + half_result[::-1]
            else:
                # Если нечетный - то массив = массив + зеркальная половинка без 1 элемента
                previous_result = half_result + half_result[:-1][::-1] 
    
    return get_sum(previous_result)


def testing (fun):
    folder_path = './data/Tickets/'

    files = os.listdir(folder_path)
    test_files = list(filter(lambda x: 'test' in x, files))
    input_files = list(filter(lambda x: 'in' in x, test_files))

    def extract_number(name):
        return int(name.split('.')[1])

    sorted_input_files = sorted(input_files, key=extract_number)

    for filename in sorted_input_files:
        test_number = filename.split('.')[1]

        test_input_file_path = os.path.join(folder_path, filename)
        test_output_file_path = os.path.join(folder_path, filename.replace('.in', '.out'))
        
        with open(test_input_file_path, 'r') as input_file:
            input = int(input_file.read())

        with open(test_output_file_path, 'r') as output_file:
            output = int(output_file.read())

        start_time = time.time()
        real_output = fun(input)
        end_time = time.time()
        execution_time = end_time - start_time
        
        if real_output == output:
            print('Тест ' + test_number + ' пройден')
            print('Время выполнения:', execution_time)
        else:
            print('Тест ' + test_number + ' провален')


        print('Входное значение:', input,', Ожидаемое значение:', output, ', Получено:', real_output)
        print('---------------')
            

print('Тест первого варианта')
testing(counting)
print(' ')
print(' ')
print(' ')
print('Тест второго варианта')
testing(counting2)

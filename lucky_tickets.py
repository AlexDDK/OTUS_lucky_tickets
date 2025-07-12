import os

def counting (n):

    if n < 1:
        return 0
    
    cache = []
    def get_sum (array):
        return sum(map(lambda x: x ** 2, array))

    if n == 1:
        cache = [1]*(n*9 + 1)
        return get_sum(cache)
    

    for digit_count in range(1,n + 1):
        if digit_count == 1:
            cache = [1]*(digit_count*9 + 1)
        else:
            table =  [[0] * (n*9+1) for _ in range(10)]
            for string in range(10):
                for column in range (0, n*9+1):
                    if 0 <= column - string < len(cache):
                        table[string][column] = cache[column - string]
                    else:
                        table[string][column] = 0 
            cache = [sum(column) for column in zip(*table)]
    
    return get_sum(cache)


def testing ():
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

        real_output = counting(input)
        
        if real_output == output:
            print('Тест ' + test_number + ' пройден')
        else:
            print('Тест ' + test_number + ' провален')


        print('Входное значение:', input,', Ожидаемое значение:', output, ', Получено:', real_output)
            

testing()

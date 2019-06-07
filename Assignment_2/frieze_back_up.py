import os
from copy import deepcopy

class FriezeError(Exception):
    def __init__(self, message):
        self.message = message

class Frieze:
    '''
    >>> f = Frieze('frieze_1.txt')
    >>> f.analyse()
    >>> f = Frieze('frieze_2.txt')
    >>> f.analyse()
    >>> f = Frieze('frieze_3.txt')
    >>> f.analyse()
    >>> f = Frieze('frieze_4.txt')
    >>> f.analyse()
    >>> f = Frieze('frieze_5.txt')
    >>> f.analyse()
    >>> f = Frieze('frieze_6.txt')
    >>> f.analyse()
    >>> f = Frieze('frieze_7.txt')
    >>> f.analyse()
    
    '''

    def __init__(self, file_name = None):
        self.file_name = file_name
        self._open_and_read_file()
        self._process_data()
        self.height = len(self.translated_file) - 1
        self.length = len(self.translated_file[0]) - 1
        self._is_correct_input()

    def _open_and_read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                self.file_content = file.readlines()
        except FileNotFoundError:
            print('No such file...')

    def _process_data(self):
        for i in range(len(self.file_content)):
            self.file_content[i] = self.file_content[i].replace('\n', '')
            self.file_content[i] = self.file_content[i].split()
        self.translated_file = []
        for i in self.file_content:
            if len(i) > 0:
                self.translated_file.append(i)
        for i in range(len(self.translated_file)):
            for j in range(len(self.translated_file[i])):
                self.translated_file[i][j] = bin(int(self.translated_file[i][j]))
                self.translated_file[i][j] = '0' * (4 - (len(self.translated_file[i][j]) - 2))\
                                                + self.translated_file[i][j][2:]

    def _is_correct_input(self):
        if self.height > 16 or self.height < 2:
            raise FriezeError('Incorrect input. ')
        if self.length > 50 or self.length < 4:
            raise FriezeError('Incorrect input. ')
        for i in self.translated_file:
            if len(i) != self.length + 1:
                raise FriezeError('Incorrect input. ')
        for i in self.translated_file:
            for j in range(self.length + 1):
                if int(i[j], 2) > 15 or int(i[j], 2) < 0:
                    raise FriezeError('Incorrect input. ')
        self.compute_period()
        if self.period < 2:
            raise FriezeError('Input does not represent a frieze. ')
        for i in self.translated_file[0][:-1]:
            if int(i, 2) not in {4, 5, 6, 7, 12, 13, 14, 15}:
                raise FriezeError('Input does not represent a frieze. ')
        for i in self.translated_file[self.height][:-1]:
            if int(i, 2) not in {4, 5, 6, 7, 12, 13, 14, 15}:
                raise FriezeError('Input does not represent a frieze. ')
        for i in self.list_vertical:
            if all([int(i[j], 2) in {1, 3, 5, 7, 9, 11, 13, 15} for j in range(1, self.height)]):
                raise FriezeError('Input does not represent a frieze. ')

    def compute_period(self):
        self.list_vertical = []
        col = 0
        for i in range(self.length + 1):
            self.list_vertical.append([])
            for j in range(self.height + 1):
                self.list_vertical[col].append(self.translated_file[j][i])
            col += 1
        for period in range(1, int(self.length / 2) + 1):
            temp = 0
            for i in range(1, int(self.length / period + 1)):
                if self.list_vertical[0: period] == self.list_vertical[i * period: i * period + period]:
                    temp += 1
            if temp == int(self.length / period) - 1:
                self.period = period
                return
        self.period = 0


    def is_vertical_reflection(self):
        north_south = deepcopy(self.list_vertical)
        west_east = deepcopy(self.list_vertical)
        all_flag = 0
        for i in range(len(west_east)):
            for j in range(len(west_east[i])):
                if west_east[i][j][-1] == '1':
                    west_east[i][j] = 1
                else:
                    west_east[i][j] = 0

        for i in range(len(north_south)):
            for j in range(len(north_south[i])):
                if north_south[i][j][-3] == '1':
                    north_south[i][j] = 1
                else:
                    north_south[i][j] = 0
        
        for i in range(self.period):
            temp_1 = 0
            temp_2 = 0
            for j in range(1, int(self.period / 2 + 1)):
                if north_south[i - j + 1] == north_south[i + j]:
                    temp_1 += 1
                if north_south[i - j] == north_south[i + j]:
                    temp_2 += 1
            if temp_1 == int(self.period / 2):
                axis = i
                type = 1
                all_flag += 1
                break
            if temp_2 == int(self.period / 2):
                axis = i
                type = 2
                all_flag += 1
                break
        if all_flag == 0:
            return False
        print(type, axis)
        if type == 1:
            temp = 0
            for j in range(1, int(self.period / 2 + 1)):
                if west_east[axis - j] == west_east[axis + j - 1]:
                    temp += 1
            if temp == int(self.period / 2):
                all_flag += 1
        if type == 2:
            temp = 0
            for j in range(1, int(self.period / 2 + 1)):
                if west_east[axis - j + 1] == west_east[axis + j]:
                    temp += 1
            if temp == int(self.period / 2):
                all_flag += 1
            
                
        
        
        print(all_flag)
                    
                
            

    def is_horizontal_reflection(self):
        return False

    def is_glided_horizontal_reflection(self):
        return False
    
    def is_rotation(self):
        return False


    def compute_north_to_south(self):
        list_north_to_south = []
        for i in range(len(self.translated_file)):
            for j in range(len(self.translated_file[i])):
                if self.translated_file[i][j][-1] == '1':
                    list_north_to_south.append([j, i])
        list_north_to_south_arrange = []
        index = 0
        for i in range(self.length + 1):
            for j in range(self.height + 1):
                if [i, j - 1] not in list_north_to_south and [i, j] in list_north_to_south:
                    list_north_to_south_arrange.append([[i, j]])
                if [i, j] in list_north_to_south and [i, j + 1] not in list_north_to_south:
                    list_north_to_south_arrange[index].append([i, j])
                    index += 1
        for i in range(len(list_north_to_south_arrange)):
            list_north_to_south_arrange[i][0][1] -= 1
        return list_north_to_south_arrange

    def compute_northwest_to_southeast(self):
        list_northweast_to_southeast = []
        for i in range(len(self.translated_file)):
            for j in range(len(self.translated_file[i])):
                if self.translated_file[i][j][0] == '1':
                    list_northweast_to_southeast.append([j, i])
        list_northwest_to_southeast_arrange = []
        index = 0
        for i in range(self.height - 1 + 1, -1, -1):
            for j in range(self.height - i + 1):
                if [j, j + i] in list_northweast_to_southeast and [j - 1, j + i - 1] not in list_northweast_to_southeast:
                    list_northwest_to_southeast_arrange.append([[j, j + i]])
                if [j, j + i] in list_northweast_to_southeast and [j + 1, j + i + 1] not in list_northweast_to_southeast:
                    list_northwest_to_southeast_arrange[index].append([j, j + i])
                    index += 1

        for i in range(1, self.length - self.height + 1):
            for j in range(self.height + 1):
                if [i + j, j] in list_northweast_to_southeast and [i + j - 1, j - 1] not in list_northweast_to_southeast:
                    list_northwest_to_southeast_arrange.append([[i + j, j]])
                if [i + j, j] in list_northweast_to_southeast and [i + j + 1, j + 1] not in list_northweast_to_southeast:
                    list_northwest_to_southeast_arrange[index].append([i + j, j])
                    index += 1
        for i in range(self.length - self.height + 1, self.length + 1):
            for j in range(self.length - i + 1):
                if [i + j, j] in list_northweast_to_southeast and [i + j - 1, j - 1] not in list_northweast_to_southeast:
                    list_northwest_to_southeast_arrange.append([[i + j, j]])
                if [i + j, j] in list_northweast_to_southeast and [i + j + 1, j + 1] not in list_northweast_to_southeast:
                    list_northwest_to_southeast_arrange[index].append([i + j, j])
                    index += 1
        for i in range(len(list_northwest_to_southeast_arrange)):
            list_northwest_to_southeast_arrange[i][1][0] += 1
            list_northwest_to_southeast_arrange[i][1][1] += 1
        list_northwest_to_southeast_arrange = sorted(list_northwest_to_southeast_arrange, key = lambda x: x[0][1])
        return list_northwest_to_southeast_arrange

    def compute_west_to_east(self):
        list_west_to_east = []
        for i in range(len(self.translated_file)):
            for j in range(len(self.translated_file[i])):
                if self.translated_file[i][j][1] == '1':
                    list_west_to_east.append([j, i])
        list_west_to_east_arrange = []
        index = 0
        for i in range(self.height + 1):
            for j in range(self.length + 1):
                if [j, i] in list_west_to_east and [j - 1, i] not in list_west_to_east:
                    list_west_to_east_arrange.append([[j, i]])
                if [j, i]  in list_west_to_east and [j + 1, i] not in list_west_to_east:
                    list_west_to_east_arrange[index].append([j, i])
                    index += 1
        for i in range(len(list_west_to_east_arrange)):
            list_west_to_east_arrange[i][1][0] += 1
        return list_west_to_east_arrange

    def compute_southwest_to_northeast(self):
        list_southwest_to_northeast = []
        for i in range(len(self.translated_file)):
            for j in range(len(self. translated_file[i])):
                if self.translated_file[i][j][2] == '1':
                    list_southwest_to_northeast.append([j, i])
        list_southwest_to_northeast_arrange = []
        index = 0
        for i in range(self.height + 1):
            for j in range(i + 1):
                if [j, i - j] in list_southwest_to_northeast and [j - 1, i - j + 1] not in list_southwest_to_northeast:
                    list_southwest_to_northeast_arrange.append([[j, i - j]])
                if [j, i - j] in list_southwest_to_northeast and [j + 1, i - j - 1] not in list_southwest_to_northeast:
                    list_southwest_to_northeast_arrange[index].append([j, i - j])
                    index += 1
        for i in range(self.height + 1, self.length + 1):
            for j in range(self.height - 1 + 1, -1, -1):
                if [i - j, j] in list_southwest_to_northeast and [i- j - 1, j + 1] not in list_southwest_to_northeast:
                    list_southwest_to_northeast_arrange.append([[i - j, j]])
                if [i - j, j] in list_southwest_to_northeast and [i - j + 1, j - 1] not in list_southwest_to_northeast:
                    list_southwest_to_northeast_arrange[index].append([i - j, j])
                    index += 1
        for i in range(self.length + 1, self.length + self.height + 1):
            for j in range(self.height + 1, i - self.length, -1):
                if [i - j, j] in list_southwest_to_northeast and [i- j - 1, j + 1] not in list_southwest_to_northeast:
                    list_southwest_to_northeast_arrange.append([[i - j, j]])
                if [i - j, j] in list_southwest_to_northeast and [i - j + 1, j - 1] not in list_southwest_to_northeast:
                    list_southwest_to_northeast_arrange[index].append([i - j, j])
                    index += 1
        for i in range(len(list_southwest_to_northeast_arrange)):
            list_southwest_to_northeast_arrange[i][1][0] += 1
            list_southwest_to_northeast_arrange[i][1][1] -= 1
        list_southwest_to_northeast_arrange = sorted(list_southwest_to_northeast_arrange, key = lambda x: x[0][1])
        return list_southwest_to_northeast_arrange

    def analyse(self):
        self.list_north_to_south = self.compute_north_to_south()
        self.list_northwest_to_southeast = self.compute_northwest_to_southeast()
        self.list_west_to_east = self.compute_west_to_east()
        self.list_southwest_to_northeast = self.compute_southwest_to_northeast()
        if not self.is_vertical_reflection() and not self.is_horizontal_reflection() and not self.is_glided_horizontal_reflection() and not self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation only. ')
        if self.is_vertical_reflection() and not self.is_horizontal_reflection() and not self.is_glided_horizontal_reflection() and not self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('\t\tand vertical reflection only. ')
        if not self.is_vertical_reflection() and self.is_horizontal_reflection() and not self.is_glided_horizontal_reflection() and not self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('\t\tand horizontal reflection only. ')
        if not self.is_vertical_reflection() and not self.is_horizontal_reflection() and self.is_glided_horizontal_reflection() and not self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('\t\tand glided horizontal reflection only. ')
        if not self.is_vertical_reflection() and not self.is_horizontal_reflection() and not self.is_glided_horizontal_reflection() and self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('\t\tand rotation only. ')
        if self.is_vertical_reflection() and not self.is_horizontal_reflection() and self.is_glided_horizontal_reflection() and self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation, ')
            print('\t\tglided horizontal and vertical reflections, and rotation only. ')
        if self.is_vertical_reflection() and self.is_horizontal_reflection() and not self.is_glided_horizontal_reflection() and self.is_rotation():
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation, ')
            print('\t\thorizontal and vertical reflections, and rotaion only. ')
            

    def display(self):
        list_north_to_south_for_print = self.compute_north_to_south()
        list_northwest_to_southeast_for_print = self.compute_northwest_to_southeast()
        list_west_to_east_for_print = self.compute_west_to_east()
        list_southwest_to_northeast_for_print = self.compute_southwest_to_northeast()
        tex_file_name = self.file_name[:-4] + '.tex'
        if os.path.isfile(tex_file_name):
            os.remove(tex_file_name)
        with open(tex_file_name, 'w') as tex_file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage{tikz}\n'
                  '\\usepackage[margin=0cm]{geometry}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\vspace*{\\fill}\n'
                  '\\begin{center}\n'
                  '\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]', file = tex_file)
            print('% North to South lines', file = tex_file)
            for i in list_north_to_south_for_print:
                print('    ' + f'\draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});', file = tex_file)
            print('% North-West to South-East lines', file = tex_file)
            for i in list_northwest_to_southeast_for_print:
                print('    ' + f'\draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});', file = tex_file)
            print('% West to East lines', file = tex_file)
            for i in list_west_to_east_for_print:
                print('    ' + f'\draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});', file = tex_file)
            print('% South-West to North-East lines', file = tex_file)
            for i in list_southwest_to_northeast_for_print:
                print('    ' + f'\draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});', file = tex_file)

            print('\\end{tikzpicture}\n'
                  '\\end{center}\n'
                  '\\vspace*{\\fill}\n'
                  '\n'
                  '\\end{document}', file = tex_file)
        os.system('pdflatex ' + tex_file_name)
        for file in (self.file_name[:-4] + ext for ext in ('.aux', '.log')):
            os.remove(file)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
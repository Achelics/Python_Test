#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''


if __name__ == '__main__':

    si_list = []
    name_list = []
    result_list = []

    with open("D:\Users\Achelics\PycharmProjects\LiuSongTest\student_work\sishi-number\ll_students.txt") as f:
        for line in f:
            line = line.strip('\n')
            list = line.split('\t')
            number_name = {}
            if list[0]=="2015" and list[4]=="4":
                number = list[2]
                name = list[3]
                number_name['number'] = number
                number_name['name'] = name
                si_list.append(number_name)


    with open("D:\Users\Achelics\PycharmProjects\LiuSongTest\student_work\sishi-number\sishi_shuoshi.txt") as h:
        for line in h:
            line = line.strip('\n')
            name_list.append(line)

    for id_name in si_list:
        for name in name_list:
            if id_name['name'] == name:
                name_str = id_name['number'] + '\t' + id_name['name']
                result_list.append(name_str)

    rf = open("D:\Users\Achelics\PycharmProjects\LiuSongTest\student_work\sishi-number\esult.txt", "a")
    for id_name_str in result_list:
        rf.write(id_name_str)
        rf.write('\n')


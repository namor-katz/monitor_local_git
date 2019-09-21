#!/usr/bin/env python
# -*- coding: utf-8 -*-
# namor925@gmail.com
#  monitor_g.py
# this is simple monitor from status local git repos


import os
import argparse
import git
import shutil
import pickledb


#define base variables
home_dir = os.path.expanduser('~')
git_dir = "gits"
full_path = os.path.join(home_dir, git_dir)


# base work git
def get_git_status(dir_path):
    '''
    берем абсолютный путь, смотрим, есть ли незатреканное, а теперь
    и немодифицированное, если ЕСТЬ то возвращаем TRUE
    '''
    tmp2 = os.path.join(full_path, dir_path)
    if tmp2 is None:
        return False
    # untracked
    '''
    repo = git.Repo(tmp2,  search_parent_directories=True)
    a = repo.untracked_files # это только неотслеживаемые. измененные оно не видит!!
    print("Я мощныа А ", a)
    print("перед лен")
    if len(a) > 0:
        return True
    else:
        return False
        '''
    # modified, пока только для файлов missing
    #print("после лен")
    g = git.cmd.Git(tmp2)
    e = g.execute(['git', 'status'])
    if 'modified' in e:
        print(tmp2, 'модифицирован!')
        return True
    else:
        return False

#base work files
def get_time(fname):
    ''' принять полный путь к файлу, вернуть (видимо) namedtuple'''
    try:
        time_atime = os.stat(fname)
        return fname, time_atime
        #keystore.set(fname, time_atime)
    except:
        print("не могу получить данные для {}".format(fname))
        return fname, False


if __name__ == "__main__":
    list_dirs = os.listdir(full_path)
    #TODOS: обрабатывать если гитов нет.
    for i in list_dirs:
        get_git_status(i)


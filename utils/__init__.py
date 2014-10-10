#coding:utf-8
__author__ = 'zhanglong'

import datetime
import sys
import os
import traceback
import time
import cPickle as pickle
import itertools

def get_date_str(dt=None):
    if dt is None:
        dt = datetime.datetime.now()

    return dt.strftime('%Y-%m-%d')

def parse_date_str(date_str):
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return d

def get_time_str(dt=None):
    if dt is None:
        dt = datetime.datetime.now()

    return dt.strftime('%Y-%m-%d %H:%M:%S')

def parse_time_str(date_str):
    t = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    return datetime.datetime(*t[0:6])



def datetime2time(dt):
    return time.mktime(dt.timetuple())

def time2datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)



def time_less_months(timestamp_big , timestamp_small):
    db = time2datetime(timestamp_big)
    ds = time2datetime(timestamp_small)
    return datetime_less_months(db,ds)


def datetime_less_months(dt_big , dt_small):
    return (dt_big.year*12 + dt_big.month) - (dt_small.year * 12  + dt_small.month)




def print_err():
    sys.stderr.write('==' * 30 + os.linesep)
    sys.stderr.write('err time: ' + str(datetime.datetime.now()) + os.linesep)
    sys.stderr.write('--' * 30 + os.linesep)
    traceback.print_exc(file=sys.stderr)
    sys.stderr.write('==' * 30 + os.linesep)



def age_comput(birth_date , dn=None):
    dn = datetime.datetime.now() if dn == None else parse_date_str(dn)
    db = parse_date_str(birth_date)
    months = (dn.year - db.year) * 12 + (dn.month - db.month)  + ( 0  if dn.day - db.day >0 else -1)
    age , month = divmod(months , 12)
    if month == 0:
        age_str =  "%s岁" % (age)
    else :
        age_str =  "%s岁%s月" % (age , month)

    return {"age" : age , "month" : month , "months" : months ,"age_str":age_str}


def deepcopy(x):
    return pickle.loads(pickle.dumps(x))



def html_color_font(text ,color="red"):
    return "<font color=""%s"">%s</font>" % (color , text)


def slice_list(iterable,sep_count,fill_default=False,default=None):
    "切分数组"
    rt = []
    start=0
    end = sep_count

    iter_count,remain  = divmod(len(iterable),sep_count)
    iter_count = iter_count+1 if remain else iter_count

    for x in range(iter_count) :
        it = iterable[start:end]
        to_append = list(it)
        rt.append(to_append)
        start += sep_count
        end += sep_count

    if fill_default :
        last = rt[-1]
        last.extend([default]*3)
        rt[-1] = last[0:sep_count]
    return rt





def group_list(l):
    ret = []
    for x in l[0]:
        ret.append([])
    for index, item in enumerate(l):
        for index2, y in enumerate(item):
            ret[index2].append(y)
    return ret



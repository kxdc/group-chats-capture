import os
import re
from datetime import date, datetime, timedelta
from collections import Counter

def exists_file(filename):

    if not os.path.exists(filename):
        print(filename, " is empty")
        return False
    else:
        print("processing ", filename)
        return True

def update_dict(f_dict, line, c_stop, is_today):

    if line[0] != '[':
        return

    messages = re.split('\[|\]', line)
    if len(messages) < 7:
        return
    else:
        if messages[3] == '' or messages[5] == '':
            return
    user_name = messages[3]
    send_time = messages[5].split()[3]
    c_send_time = datetime.strptime(send_time, '%H:%M:%S').time()

    if is_today:
        if c_send_time > c_stop:
            return
    else:
        if c_send_time < c_stop:
            return

    if user_name not in frequency_dict:
        frequency_dict[user_name] = 1
    else:
        count = frequency_dict[user_name] + 1
        frequency_dict[user_name] = count

def process_files(today_filename, past_filename, stop_time):

    c_stop_time = datetime.strptime(stop_time, '%H:%M:%S').time()

    exists = exists_file(today_filename)
    if exists:
        today_f = open(today_filename, 'r')
        for today_line in today_f:
            update_dict(frequency_dict, today_line, c_stop_time, True)

    exists = exists_file(past_filename)
    if exists:
        past_f = open(past_filename, 'r')
        for past_line in past_f:
            update_dict(frequency_dict, past_line, c_stop_time, False)

    sorted_result = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_result

if __name__=='__main__':

    last_date = datetime.now() - timedelta(5)
    last_path = datetime.strftime(last_date, "%b-%d-%Y")
    today_path = date.today().strftime("%b-%d-%Y")
    stop_time_str = '16:00:00'
    target_groups = ['a', 'b', 'c']
    today_result = []
    last_result = []
    suffex = '.txt'

    for single_group in target_groups:
        single_file = single_group + suffex
        frequency_dict = {}
        today_file = today_path + '/' + single_file
        last_file = last_path + '/' + single_file
        print("------------------------------------------")
        result = process_files(today_file, last_file, stop_time_str)
        print(result)
    print("------------------------------------------")

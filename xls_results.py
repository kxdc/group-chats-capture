import os
import xlrd

verses_list = ["aavbb", "ccvdd",
               "eevff", "ggvhh",
               "iivjj", "kkvll",
               "mmvnn", "uuvww"]

def exists_file(filename):

    if not os.path.exists(filename):
        print(filename, " is empty")
        return False
    else:
        print("processing ", filename)
        return True


def check_same_status(user_guess, true_fact):

    same_num = 0
    status = ''

    for i in range(len(true_fact)):
        if user_guess[i] == "X":
            # return "null"
            status += "N"
        elif user_guess[i] == true_fact[i]:
            same_num += 1
            status += "Y"
        else:
            status += "N"

    status = status + ':' + str(same_num)
    # print(user_guess, "&", true_fact, " -- ", status)
    return status


def result_of_single_match(user_input, match_index):

    if len(user_input) == 0: 
        return "_";

    team_A = verses_list[match_index].split('v')[0]
    team_B = verses_list[match_index].split('v')[1]

    if team_A in user_input:
        return "A"
    elif team_B in user_input:
        return "B"
    else:
        return "X"


def generate_user_guess(worksheet, rows, cols):

    for i in range(rows):
        single_row = worksheet.row_values(i)

        # print(single_row)
        user_guess = ""
        user_index = single_row[0]
        user_name = single_row[1]
        if type(user_index) == str:
            continue

        for j in range(len(final_results)):
            user_guess += result_of_single_match(single_row[j+3], j)

        user_result = check_same_status(user_guess, final_results)

        correct_num = int(user_result.split(':')[1])
        tuple_to_save = (int(user_index), user_name, correct_num)
        final_list[correct_num].append(tuple_to_save)
        print(int(user_index), user_name, " -- ", user_result)

    
def process_sheet(worksheet):

    ws_rows = worksheet.nrows
    ws_cols = worksheet.ncols
    user_res = generate_user_guess(worksheet, ws_rows, ws_cols)

    
def process_file(filename):

    if exists_file(filename):
        workbook = xlrd.open_workbook(filename)
    else:
        return

    process_sheet(workbook.sheet_by_index(0))


if __name__ == '__main__':

    xls_name = "./all_user_results.xls"
    final_results = "BAAABAAA"
    final_list = []
    list_pd= []
    
    final_list = [[] for _ in range(len(final_results)+1)]
    print(final_list)

    process_file(xls_name)
    print(final_list[len(final_results)-3])
    print(final_list[len(final_results)-4])
    

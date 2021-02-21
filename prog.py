import csv
import random


def HT_chart():

    #opens file and creates initial variables
    filename = 'HT_chart.txt'
    with open(filename, 'r') as data:
        csv_reader = csv.reader(data)
        chart_dict = []

        #adds file data to list array
        for line in csv_reader:
            chart_dict.append(line)

        #testing logic begins
        while True:

            #random selection
            row_num = random.randint(1,len(chart_dict)-1)
            col_num = random.randint(1,len(chart_dict[0])-1)
            tester = chart_dict[row_num][col_num]

            #user interaction
            print('\nYOUR HAND IS ' + str(21 - row_num) + ' AND DEALER HAND IS ' + str(1 + col_num))
            user_ans = input('WHAT THE MOVE BOSS: (H/S/D/Q) ').lower()

            #continuation logic
            if user_ans == str(tester):
                print('CONGRATS FUCKER, YOU GOT SOMETHING RIGHT\n')
                continue
            elif user_ans == 'q':
                print('HARD TOTALS TESTING TERMINATED\n')
                break
            else:
                print('YOU ARE OFFICIALLY RETARDED\n')
                continue


def ST_chart():

    #opens file and creates initial variables
    filename = 'ST_chart.txt'
    with open(filename, 'r') as data:
        csv_reader = csv.reader(data)
        chart_dict = []

        #adds file data to list array
        for line in csv_reader:
            chart_dict.append(line)

        #testing logic begins
        while True:

            #tester selection
            row_num = random.randint(1,len(chart_dict)-1)
            col_num = random.randint(1,len(chart_dict[0])-1)
            tester = chart_dict[row_num][col_num]

            #user interaction
            print('\nYOUR HAND IS: A,' + str(1 + row_num) + ' AND DEALER HAND IS: ' + str(1 + col_num))
            user_ans = input('WHAT THE MOVE BOSS: (H/S/D/Q) ').lower()

            #continuation logic
            if user_ans == str(tester):
                print('CONGRATS FUCKER, YOU GOT SOMETHING RIGHT\n')
                continue
            elif user_ans == 'q':
                print('SOFT TOTALS TESTING TERMINATED\n')
                break
            else:
                print('YOU ARE OFFICIALLY RETARDED\n')
                continue

def PS_chart():

    #opens file and creates initial variables
    filename = 'PS_chart.txt'
    with open(filename, 'r') as data:
        csv_reader = csv.reader(data)
        chart_dict = []

        #adds file data to list array
        for line in csv_reader:
            chart_dict.append(line)

        #testing logic begins
        while True:

            #random selection
            row_num = random.randint(1,len(chart_dict)-1)
            col_num = random.randint(1,len(chart_dict[0])-1)
            tester = chart_dict[row_num][col_num]

            #handle case where index is 10/Aces
            if row_num == 10:
                print('\nYOUR HAND IS ' + 'AA'  + ' AND DEALER HAND IS ' + str(1 + col_num))
                user_ans = input('WHAT THE MOVE BOSS, SPLIT OR NAH: (Y/N/D/Q) ').lower()

                #continuation logic
                if user_ans == str(tester):
                    print('CONGRATS FUCKER, YOU GOT SOMETHING RIGHT\n')
                    continue
                elif user_ans == 'q':
                    print('PAIR SPLITTING TESTING TERMINATED\n')
                    break
                else:
                    print('YOU ARE OFFICIALLY RETARDED\n')
                    continue
            else:

                #user interaction
                print('\nYOUR HAND IS ' + str(1 + row_num) + ' AND DEALER HAND IS ' + str(1 + col_num))
                user_ans = input('WHAT THE MOVE BOSS, SPLIT OR NAH: (Y/N/D/Q) ').lower()

                #continuation logic
                if user_ans == str(tester):
                    print('CONGRATS FUCKER, YOU GOT SOMETHING RIGHT\n')
                    continue
                elif user_ans == 'q':
                    print('PAIR SPLITTING TESTING TERMINATED\n')
                    break
                else:
                    print('YOU ARE OFFICIALLY RETARDED\n')
                    continue

while True:
    def_selector = input('\nSELECT AN OPTION \'HT\',\'ST\', \'PS\', OR \'Q\' ').upper()
    if def_selector == 'HT':
        print('\nHARD TOTALS TESTING BEGINNING\nPRESS \'Q\' AT ANYTIME TO QUIT\n')
        print('H = Hit, S = Stand, D = Double')
        HT_chart()
    elif def_selector == 'ST':
        print('\nSOFT TOTALS TESTING BEGINNING\nPRESS \'Q\' AT ANYTIME TO QUIT\n')
        print('H = Hit, S = Stand, D = Double(Also double otherwise stand)')
        ST_chart()
    elif def_selector == 'PS':
        print('\nPAIR SPLITTING TESTING BEGINNING\nPRESS \'Q\' AT ANYTIME TO QUIT\n')
        print('Y = Yes, N = No, D = Yes if DAS')
        PS_chart()
    elif def_selector == 'Q':
        break
print('\nPROGRAM SUCCESSFULLY TERMINATED\nHAVE A WONDERFUL DAY FUCKTARD\n')

import json

def calc_profit(rev, costs):
    profit = int(rev) - int(costs)
    return profit

def calc_avr_profit(list):
    loss_count = 0
    total_profit = 0
    avr_profit = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            total_profit = total_profit + list[i]
        else:
            loss_count += 1
    if (len(list) - loss_count) > 0:
        avr_profit = total_profit / (len(list) - loss_count)
    else:
        print('There are no profitable companies in the list.')
    return avr_profit

with open('7_file.txt') as f:
    profits_list = []
    profit_dict = {}
    loss_dict = {}
    avr_profit_dict = {}
    for line in f:
        if len(line.strip()) != 0:
            line_list = line.split()
            firm_profit = calc_profit(line_list[2], line_list[3])
            profits_list.append(firm_profit)
            if firm_profit > 0:
                profit_dict.update({line_list[0]: firm_profit})
            else:
                loss_dict.update({line_list[0]: firm_profit})
    avr_profit_dict.update({'average profit': round(calc_avr_profit(profits_list), 2)})
    list_dict = [profit_dict, loss_dict, avr_profit_dict]

with open('7_file.json', 'w') as f:
    json.dump(list_dict, f)

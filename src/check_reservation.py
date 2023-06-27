import unittest
from datetime import datetime, date



def make_reserv(date_in, date_out, room):
    new_reservation = [date_in, date_out, room]
    file = open('Reservations.txt', "r")
    reservations = file.read().splitlines()

    if check_date_format(date_in,date_out) == False:
        print("Wrong date format. Try DD.MM.YYYY")
        return False

    if str(new_reservation) in reservations:
        print("The room is already reserved. Take another one!")
        return False



    else:
        #str to date
        list1 = date_in.split(".")
        list2 = date_out.split(".")
        list1 = [int(i) for i in list1]
        list2 = [int(i) for i in list2]
        list1.reverse()
        list2.reverse()
        start_date = datetime(*list1).date()
        end_date = datetime(*list2).date()
        for i in reservations:
            i = i.replace("'", "")
            i = i.strip('[]')
            i = i.replace(" ", "")
            list_check_in,list_check_out,check_room = i.split(",",3)

            if check_room == room:
                list_check_in = list_check_in.split(".")
                list_check_out = list_check_out.split(".")
                list_check_in = [int(i) for i in list_check_in]
                list_check_out = [int(i) for i in list_check_out]
                list_check_in.reverse()
                list_check_out.reverse()
                check_start_date = datetime(*list_check_in).date()
                check_end_date = datetime(*list_check_out).date()
                if (start_date > check_start_date and end_date < check_end_date) \
                        or (start_date < check_start_date and end_date > check_start_date and end_date < check_end_date) \
                        or (start_date > check_start_date and start_date < check_end_date and end_date > check_start_date)\
                        or start_date == check_start_date or start_date == check_end_date or end_date == check_start_date or end_date == check_end_date:
                    print("The room is already reserved for this period.")
                    return False
            else:
                continue
        file.close()
        new_reservations = open('Reservations.txt', "a")
        new_reservations.write((str(new_reservation)))
        new_reservations.write('\n')
        new_reservations.close()
        print("The room is yours. Thank you!")
        return True


def check_date_format(datein, dateout):
    list1 = datein.split(".")
    list2 = dateout.split(".")
    if len(list1)!=3:
        return False
    if len(list2)!=3:
        return False
    try:
        list1 = [int(i) for i in list1]
        list2 = [int(i) for i in list2]
        if list1[0] > 31 or list1[0] < 1 or list2[0] > 31 or list2[0] < 1 \
                or list1[1] > 12 or list1[1] < 1 or list2[1] > 12 or list2[1] < 1\
                or list1[2] < 2022 or list2[2] < 2022 or list2[2] < list1[2]\
                or (list1[2] == list2[2] and list1[1] == list2[1] and list1[0] > list2[0])\
                or (list1[2] == list2[2] and list1[1] > list2[1]):
            return False
        else:
            return True
    except:
        return False
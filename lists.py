def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) == 5:
        del list_to_remove_elements[5]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif 0 < len(list_to_remove_elements) < 5:
        del list_to_remove_elements[0]
        return list_to_remove_elements    
    else:
        return(list_to_remove_elements)

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.insert(6, "Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    if not list_to_check:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):

    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    list1 = list_of_lists_to_modify [0]
    list2 = list_of_lists_to_modify [1]
    list3 = list_of_lists_to_modify [2]

    if len(list1) >= 2 and len(list2) >= 4 and len(list3) >= 2:
        list10 = list1 [0]
        list11 = list1 [1] 
        list12 = [list10, list11]

        list20 = list2 [1]
        list21 = list2 [2]
        list22 = list2 [3]
        list23 = [list20, list21, list22]

        list30 = list3 [-2]
        list31 = list3 [-1]
        list32 = [list30, list31]

        new_list = [list12, list22, list32]
        return new_list

    elif 0 < len(list1) < 2 and len(list2) >= 4 and len(list3) >= 2:

        list11 = list1 [0] 
        list12 = [list11]

        list20 = list2 [1]
        list21 = list2 [2]
        list22 = list2 [3]
        list23 = [list20, list21, list22]

        list30 = list3 [-2]
        list31 = list3 [-1]
        list32 = [list30, list31]

        new_list = [list12, list22, list32]
        return new_list

    elif len(list1) == 0 and len(list2) >= 4 and len(list3) >= 2:

        list20 = list2 [1]
        list21 = list2 [2]
        list22 = list2 [3]
        list22 = [list20, list21]

        list30 = list3 [-2]
        list31 = list3 [-1]
        list32 = [list30, list31]

        new_list = [list22, list32]
        return new_list

    elif len(list1) >= 2 and len(list2) < 4 and len(list3) >= 2:
        list10 = list1 [1]
        list11 = list1 [0] 
        list12 = [list10, list11]

        list20 = list2 [1]
        list21 = list2 [2]
        list22 = list2 [3]
        list23 = [list20, list21, list22]

        list30 = list3 [-2]
        list31 = list3 [-1]
        list32 = [list30, list31]

        new_list = [list12, list22, list32]
        return new_list

    elif len(list1) >= 2 and len(list2) < 2 and len(list3) >= 2:
        list10 = list1 [1]
        list11 = list1 [0] 
        list12 = [list10, list11]

        list30 = list3 [-2]
        list31 = list3 [-1]
        list32 = [list30, list31]

        new_list = [list22, list32]
        return new_list

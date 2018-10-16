# 将文件内容转化为可操作的二维列表tab[row][col]
def file_to_table(table_name, avlb_tab):
    table = []
    filename = avlb_tab[table_name]
    f = open(filename, 'r', encoding='utf-8')
    for line in f:
        table.append(line.strip().split(","))
    f.close()
    return table


# 将表写回文件
def table_to_file(table_name, avlb_tab, table):
    filename = avlb_tab[table_name]
    with open(filename, 'w', encoding='utf-8') as f:
        for t in table:
            data = ','.join(t)
            f.write(data+'\n')


# 打印表
def print_table(table):
    for tab in table:
        for t in tab:
            print(t.center(16, " "), end="")
        print()


# where语句中的大于
def op_gt(left_arg, right_arg):
    if left_arg > right_arg:
        return True
    else:
        return False


# where语句中的小于
def op_lt(left_arg, right_arg):
    if left_arg < right_arg:
        return True
    else:
        return False


# where语句中的等于
def op_eq(left_arg, right_arg):
    if left_arg == right_arg:
        return True
    else:
        return False


# where语句中的like
def op_like(left_arg, right_arg):
    if right_arg in left_arg:
        return True
    else:
        return False


# where语句
def where_stat(table, condition):
    table_wherestat = []
    operators = {'>': op_gt,
                 '<': op_lt,
                 '=': op_eq,
                 'like': op_like}
    # 将where后的条件拆分 age > 22
    cond_col = table[0].index(condition[0])          # 要筛选的字段的下标，age
    cond = operators[condition[1]]                   # 筛选条件， >
    cond_val = condition[2]                          # 筛选值， 22
    table_wherestat.append(table[0])
    for tab in table[1:]:
        if cond(tab[cond_col], cond_val):
            table_wherestat.append(tab)
    return table_wherestat


# set语句
def set_stat(table, condition):
    table_setstat = table
    cond_col = table_setstat[0].index(condition[0])
    cond_val = condition[2]
    for tab in table_setstat[1:]:
        tab[cond_col] = cond_val
    return table_setstat


# 查询语句
def find_stat(table, condition):
    table_findstat = []
    if condition == "*":
        table_findstat = table
    else:
        cond = condition.split(",")                 # ['name', 'age']
        table_findstat.append(cond)
        a = []
        for i in cond:
            a.append(table[0].index(i))
        for tab in table[1:]:
            b = []
            for i in a:
                b.append(tab[i])
            table_findstat.append(b)
    print("查询出了{}条数据".format(len(table)))
    return table_findstat


# 添加语句
def add_stat(table, data):
    table_addstat = table
    for i in data:
        d = i.split(",")
        d.insert(0, str(int(table_addstat[-1][0])+1))
        table_addstat.append(d)
    print("增加了{}条数据".format(len(data)))
    return table_addstat


# 删除语句
def delete_stat(table_fromstat, table_wherestat):
    for tab in table_wherestat[1:]:
        table_fromstat.remove(tab)
    print("删除了{}条数据".format(len(table_wherestat)-1))
    return table_fromstat


# 更新语句
def update_stat(table_fromstat, table_setstat):
    for tab in table_setstat:
        for i in range(len(table_fromstat)):
            if table_fromstat[i][0] == tab[0]:
                table_fromstat[i] = tab
                break
    print("修改了{}条数据".format(len(table_setstat)-1))
    return table_fromstat


# 分析用户输入的语句
def statement_parser(statement, avlb_tab):
    stat = statement.split()
    if stat[:3:2] == ['find', 'from'] and len(stat) >= 4 and stat[3] in avlb_tab:
        # 说明用户输入的是完整的find语句
        # 第一步，将要操作的表从文件格式转化为二维列表格式
        table_fromstat = file_to_table(stat[3], avlb_tab)
        # 第二步，若有where语句则进行筛选
        if len(stat) == 8 and stat[4] == "where":
            table_wherestat = where_stat(table_fromstat, stat[-3:])
            table_findstat = find_stat(table_wherestat, stat[1])
            print_table(table_findstat)
        else:
            table_findstat = find_stat(table_fromstat, stat[1])
            print_table(table_findstat)
    elif stat[0] == 'add' and len(stat) >= 3:
        # 说明是完整的add语句
        # 第一步，获得要添加数据的表
        table_fromstat = file_to_table(stat[1], avlb_tab)
        # 第二步，将数据添加到表中
        table_addstat = add_stat(table_fromstat, stat[2:])
        # 第三步，将新表写会到文件中
        table_to_file(stat[1], avlb_tab, table_addstat)
    elif stat[0:2] == ['delete', 'from'] and stat[3] == 'where' and len(stat) >= 7:
        # 说明是完整的删除语句
        # 第一步，获得要删除的数据表
        table_fromstat = file_to_table(stat[2], avlb_tab)
        # 第二步，查询满足where条件的数据
        table_wherestat = where_stat(table_fromstat, stat[-3:])
        # 第三步，将满足where条件的数据删除
        table_deletestat = delete_stat(table_fromstat, table_wherestat)
        # 第四步，将新数据写入文件中
        table_to_file(stat[2], avlb_tab, table_deletestat)
    elif stat[:3:2] == ['update', 'set'] and stat[6] == 'where' and len(stat) >= 10:
        # 说明是完整的更新语句
        # 第一步，获得要更新的数据表
        table_fromstat = file_to_table(stat[1], avlb_tab)
        # 第二步，查询满足where条件的数据
        table_wherestat = where_stat(table_fromstat, stat[-3:])
        # 第三步，对满足条件的数据按照set语句修改
        table_setstat = set_stat(table_wherestat, stat[3:6])
        # 第四步，将修改完成的数据update到表中
        table_updatestat = update_stat(table_fromstat, table_setstat)
        # 第五步，将update的新表写回文件
        table_to_file(stat[1], avlb_tab, table_updatestat)


# 初始程序，获得用户输入，退出等
def main():
    """
    statement : 用户输入的语句
    exit_flag : 退出标志位
    avlb_tab : 用户可操作的数据表的名称列表
    :return:
    """
    avlb_tab = {'staff_table': '员工信息表（utf-8）.txt', }          # 假设这是通过遍历数据库获得的所有数据表的名称的列表
    exit_flag = False
    while not exit_flag:
        print("请在下方输入您的操作语句(e:退出)")
        statement = input(">>: ").strip()
        if not statement:
            continue
        elif statement == 'e' or statement == 'E':
            exit_flag = True
        else:
            statement_parser(statement, avlb_tab)


if __name__ == '__main__':
    main()

    

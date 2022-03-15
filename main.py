import get_data
import get_config

if __name__ == "__main__":

    qos_constraint = get_config.qos_constraint()
    demand, client_list = get_data.demand()
    site_bandwidth, site_list = get_data.site_bandwidth()
    qos = get_data.qos()
    # qos_site = [site_list for i in range(len(qos))]
    result = []

    # for i in range(len(qos)):
    #     qos[i].sort()
    for ctime in range(len(demand)):
        for i in range(len(client_list)):
            index = 0
            value = qos[i][0]
            for j in range(len(qos[i])):
                if qos[i][j] < value:
                    index = j
                    value = qos[i][j]
            # site_bandwidth[site_list[j]][i] -= demand[ctime][i]
            if demand[ctime][i] == 0:
                temp = client_list[i] + ":"
            else:
                temp = client_list[i] + ":<" + site_list[index] + "," + demand[ctime][i] + ">"
            result.append(temp)

    file = open('output/solution.txt', 'a')
    for i in range(len(result)):
        print(result[i])
        # s = str(result[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        # s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        s = str(result[i]) + '\n'
        file.write(s)
    file.close()
    print("保存文件成功")
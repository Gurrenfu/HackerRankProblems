if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

second_lowest = sorted(set([score for name, score in records]))[1]
second_lowest_names = [record[0] for record in records if record[1] == second_lowest]
second_lowest_names = sorted(second_lowest_names)
for name in second_lowest_names:
    print(name)

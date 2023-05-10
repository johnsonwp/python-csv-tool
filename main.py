from csvfile import (csv_to_rows, get_initials_dic, get_distinct_artist, rows_to_csv)


def main():
    # load csv
    csv_data = csv_to_rows("artworks.csv")
    artists = get_distinct_artist(csv_data)
    # get unique artists initials as initials_dic[key]
    initials_dic = get_initials_dic(csv_data)

    # zfill map_artists
    map_artists = {}
    for item in artists:
        map_artists[item] = 0

    sheet_data = []
    for i, item in csv_data:
        row_item = item
        if row_item['Artist'].strip() != "":
            map_artists[row_item['Artist']] += 1
            stock_number = initials_dic[row_item['Artist']]
            row_item['Stock number'] = "{} {}".format(stock_number, str(map_artists[row_item['Artist']]).zfill(3))
            print(row_item['Stock number'])
            sheet_data.append(row_item)
        else:
            row_item['Stock number'] = ''
            sheet_data.append(row_item)

    csv2dict = {str(i): {
        'Artist': rows['Artist'],
        'ID': rows['ID'],
        'Stock number': rows['Stock number'],
        'Title': rows['Title'],
        'Dimensions': rows['Dimensions']
    } for i, rows in enumerate(sheet_data)}

    rows_to_csv('Sheet.csv', csv2dict.items(), ['Artist', 'ID', 'Stock number', 'Title', 'Dimensions'])


if __name__ == '__main__':
    main()

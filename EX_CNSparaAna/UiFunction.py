import os


def read_ANdb():
    '''
    폴더에서 Andb.txt 파일을 찾고 없으면 빈 딕셔너리 반환하고 없다는 메시지 출력
    :return:
    '''
    if os.path.isfile('Andb.txt'):
        ANdb = {}
        with open('Andb.txt', 'r') as f:
            while True:
                temp = f.readline().split('\n')[0].split('\t')
                if temp[0] == '':
                    break
                ANdb[temp[0]] = {
                    'SYS': temp[1], 'TYPE': temp[2], 'ONECONT': temp[3], 'OnManOpen': temp[4],
                    'OffAutoClose': temp[5], 'Purpose': temp[6]
                }
    else:
        print('No Andb.txt file!!')
        ANdb = {}
    return ANdb
#各変数を時系列プロットする

def plot_many_time(DF,COLUMNS_TOPLOT):
    
    '''
    COLUMNS_TOPLOT:可視化したい変数リスト
    時間情報は'Time'カラムに格納されているのが前提
    '''
    
    #データを指定
    DF_ = DF.copy()

    #プロットする変数の指定
    COLUMNS_TOPLOT_ = COLUMNS_TOPLOT

    #グラフスタイル
    plt.style.use('fivethirtyeight')

    # フォント指定（日本語文字化け防止）
    plt.rcParams['font.family'] = 'IPAPGothic' 

    #グラフサイズ
    plt.figure(figsize=(80,10*len(COLUMNS_TOPLOT)))

    for col_num, col in enumerate(COLUMNS_TOPLOT):
        plt.subplot(len(COLUMNS_TOPLOT),1, col_num+1)
        plt.plot(DF['Time'],DF[col])
        plt.xlabel('Time', size=50)
        plt.ylabel('{}'.format(col), size=50)
        plt.tick_params(labelsize = 50)

    plt.show()

#ヒストグラムの作図関数。TARGETのクラス別（2クラス）で色分けして表示
def plot_many_hist_comparison2(DF,TARGET,TARGET1,TARGET2,COLUMN_COUNT):
    
    '''
    TARGET1,2:TARGETのクラス名
    '''

    #データ指定
    DF_ = DF.copy()

    #プロットする変数の指定 floatとint型の変数のみ
    columns_toplot = DF_.select_dtypes(['float','int64']).columns.tolist()

    #横方向に何個グラフを並べるか指定
    COLUMN_COUNT_ = COLUMN_COUNT

    #縦方向に何個グラフを並べるか算出
    line_count = math.ceil(len(columns_toplot)/COLUMN_COUNT_)

    #グラフスタイル
    plt.style.use('fivethirtyeight')

    # フォント指定（日本語文字化け防止）
    plt.rcParams['font.family'] = 'IPAPGothic'

    #グラフサイズ
    plt.figure(figsize=(7*COLUMN_COUNT,5*len(columns_toplot)))

    #作図
    for col_num, col in enumerate(columns_toplot):
        plt.subplot(line_count,COLUMN_COUNT_,col_num+1)

        s1 = DF[DF[TARGET]==TARGET1][col].dropna()
        plt.hist(s1,color='b',bins=30,label=TARGET1,density=True,alpha=0.5)

        s2 = DF[DF[TARGET]==TARGET2][col].dropna()
        plt.hist(s2,color='r',bins=30,label=TARGET2,density=True,alpha=0.5)

        plt.legend()
        plt.title(col)    
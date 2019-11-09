#目的変数と各説明変数との散布図を作成する。
def plot_scatter_Y_Xs(DF,TARGET,Xs,COLUMN_COUNT):
    
    '''
    Xs:説明変数をリストで事前に作成しておく。
    '''
    
    
    #データ指定
    DF_ = DF.copy()
    
    #説明変数はこの関数外で設定する。
    columns_toplot = Xs
    
    #横方向に何個グラフを並べるか指定
    COLUMN_COUNT_ = COLUMN_COUNT
    
    #縦方向に何個グラフを並べるか算出
    line_count = math.ceil(len(columns_toplot)/COLUMN_COUNT_)
    
    #グラフスタイル
    plt.style.use('fivethirtyeight')

    # フォント指定（日本語文字化け防止）
    plt.rcParams['font.family'] = 'IPAPGothic'

    #グラフサイズ
    plt.figure(figsize=(7*COLUMN_COUNT,4*len(columns_toplot)))
    
    # 分析対象の絞り込み
    TARGET_ = TARGET

    for x_num, x in enumerate(xs):
        plt.subplot(line_count,COLUMN_COUNT_,x_num+1)
        plt.scatter(x=DF[x], y=DF[TARGET_] , s=100, alpha=0.3)
        plt.xlabel(x, size=10)
        plt.ylabel(TARGET_, size=10)
        plt.tick_params(labelsize = 10)
        #plt.title('{} and {}'.format(target,x), size=50)

    plt.show()

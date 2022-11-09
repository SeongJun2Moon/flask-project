import pandas as pd


def new_fruites_df():
    ls_schema = ['제품', '가격', '판매량'] # 스키마
    l1 = ["사과", "딸기", "수박"]
    l2 = [1800, 1500, 3000]
    l3 = [24, 38, 13]
    ls_apd = [l1, l2, l3]
    dc = {j : ls_apd[i] for i,j in enumerate(ls_schema)}
    df = pd.DataFrame(dc)

    return df

if __name__ == '__main__':
    df = new_fruites_df()
    print(f"{df}\n")
    print(f"가격 평균: {sum(df['가격'])/len(df['가격'])}원")
    print(f"판매량 평균: {int(df['판매량'].mean())}개")

import pandas as pd

# 仮のデータフレーム
df = pd.DataFrame({
    "名前": ["たろう", "じろう", "さぶろう"],
    "点数": [80, 90, 70]
})

# CSVファイルとして保存
df.to_csv("output.csv", index=False)
print("CSVファイルを出力しました！")
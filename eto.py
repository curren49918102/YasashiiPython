prompt_message = 'あなたの生まれた年を西暦４桁で入力してください：'
year_str = input(prompt_message)

# 西暦を数値に変換する
year = int(year_str)

# 干支のデータを定義する
eto_tuple = ('子　ね','丑　うし ','寅　とら','卯　う','辰　たつ','巳　み','午　うま','未　ひつじ','申　さる','酉　とり','戌　いぬ','亥　い')

# 干支の順番(0-11の範囲)を西暦から計算する
number_of_eto = (year + 8) % 12
etho_name = eto_tuple[number_of_eto]
print('あなたの干支の順番は[', etho_name, ']です。')

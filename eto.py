prompt_message = 'あなたの生まれた年を西暦４桁で入力してください：'
year_str = input(prompt_message)
year = int(year_str)
number_of_eto = (year + 8) % 12
print(year,  number_of_eto)

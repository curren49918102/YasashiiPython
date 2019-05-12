bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'おはよう': 'オハヨウ',
    'さようなら': 'サヨウナラ'
}

while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

    if not response:
        response = '何ヲ言ッテルカ、ワカリマセン'
    print(response)

    if 'さようなら' in command:
        break

from PIL import Image, ImageDraw, ImageFont
print('генератор мемов запущен')
top_text = input('введите верхний текст: ')
bottom_text = input('введите нижний текст: ')
print(top_text,bottom_text)
print('список картинок: ')
print('1.плачущий человечек')
print('2.кот маг')
print('3.кот в молоке')
print('4.кот в ресторане')
print('5.кот в очках')
image_number = int(input('введите номер картинки: '))
if image_number == 1:
    image_file = 'pik1.png'
elif image_number == 2:
    image_file = 'pik2.png'
elif image_number == 3:
    image_file = 'pik3.jpg'
elif image_number == 4:
    image_file = 'pik4.png'
elif image_number == 5:
    image_file = 'pik5.png'
else:
    print('такой картинки нет')

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0,0),top_text,font)
text_midth = text[2]
draw.text(((width - text_midth)/2,10),top_text,font=font,fill='black')
text = draw.textbbox((0,0),bottom_text,font)
text_midth = text[2]
text_heigh = text[3]
draw.text(((width - text_midth)/2, height-text_heigh-10),bottom_text,font=font,fill='black')

image.save('new_meme.jpg')
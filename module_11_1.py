import requests
import numpy
from pprint import pprint
from PIL import Image, ImageDraw

'''библиотека requests'''

'''get-запрос'''
response = requests.get('https://api.github.com')
print(response.status_code)
pprint(response.json())

'''head'''
response = requests.head('https://www.google.com')
print(response.status_code)
print(response.headers)

'''ssl'''
response = requests.get('https://www.google.com', verify=True)
if response.status_code == 200:
    print("Сертификат действителен.")
else:
    print("Сертификат не действителен.")


'''библиотека numpy'''

'''создание массива'''
massif = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(massif)

'''умножение массивов'''
rand_massif = numpy.random.rand(3, 3)
product = massif * rand_massif
print("Умножение массивов:")
print(product)

''' Среднее значение массива'''
mean_value = numpy.mean(product)
print("Среднее значение массива:")
print(mean_value)

'''сортировка массивов'''
sorted_massif = numpy.sort(rand_massif, axis=1)
print("Отсортированный массив по строкам:")
print(sorted_massif)

sorted_massif = numpy.sort(rand_massif, axis=0)
print("Отсортированный массив по cстолбцам:")
print(sorted_massif)


'''библиотека pillow'''

'''генерация изображения'''
def linear_gradient(mode: 256) -> Image:
    image = Image.new(mode, (256, 256))     # генерация изображения размером 256x256
    draw = ImageDraw.Draw(image)                 # рисование на изображении

    # Создание линейного градиента от черного к белому сверху вниз
    for y in range(256):
        color = int(255 * y / 255)
        draw.line((0, y, 256, y), fill=(color, color, color))   # рисование горизонтальной линии с текущим цветом

    return image

gener_img = linear_gradient('RGB')
gener_img.show()

'''сохранение изображения'''
gener_img.save('linear_gradient.png')

'''вырезание участка изображения'''
img = Image.open('linear_gradient.png')
box = (0, 0, 80, 80)
region = img.crop(box)

'''обработка вырезанного участка и вставка его обратно'''
region = region.transpose(Image.Transpose.ROTATE_180)
img.paste(region, box)
img.show()

'''уменьшение изображения в 2 раза'''
new_size = img.resize((img.width//2, img.height//2 ))
new_size.show()


from PIL import Image, ImageDraw, ImageFont
from math import cos, sin, pi, sqrt
font = ImageFont.truetype("Roboto-Regular.ttf", 18, encoding='UTF-8')
# Имя в контексте всей буквицы
alf = list('АБВГДеЕЖSZИiЇћКЛМНОПРСТУƔФXѾЦЧШЩЪЫьҌЮЯЭѠѦѪѨѬѮѰӨѴӔ')
name = "ВИКТОР"
# Пустой желтый фон.
width = height = 800
fon_color = (255, 255, 255)
padding = 50
text_padding = 20
im = Image.new('RGB', (width, height), fon_color)
draw = ImageDraw.Draw(im)
n = len(alf)
xc, yc = width // 2, height // 2
r_point = (width // 2) - padding
r_text = (width // 2) - padding + text_padding
fi = -pi/2
points = []
name_points = []
# запоминаем точки многоугольника на окружности
for i in range(n):
    x_p = xc + r_point * cos(fi + (2 * pi * i) / (n))
    y_p = yc + r_point * sin(fi + (2 * pi * i) / (n))
    x_t = xc + r_text * cos(fi + (2 * pi * i) / (n))
    y_t = yc + r_text * sin(fi + (2 * pi * i) / (n))
    points.append((x_p, y_p))
    if alf[i] in name:
        name_points.append((x_p, y_p))
    if alf[i] in name:
        text_color = '#f00'
    else:
        text_color = "#000"
    draw.text(
        (x_t-5,y_t-8),
        alf[i],
        fill=(text_color),
        font=font
    )


for i in range(len(points)):
    for j in range(i + 1, len(points)):
        draw.line((points[i], points[j]), fill='#eee8aa', width=1)
    x,y = points[i]
    draw.ellipse((x-2,y-2,x+2,y+2),"#000")

for i in range(len(name_points)):
    for j in range(i + 1, len(name_points)):
        draw.line((name_points[i], name_points[j]), fill='#f00', width=1)

im.show()

from PIL import Image, ImageDraw, ImageFont
from math import cos, sin, pi, sqrt
font = ImageFont.truetype("Roboto-Regular.ttf", 18, encoding='UTF-8')
alf = [str(i) for i in range(1, 49 + 1)]
alf = list('АБВГДеЕЖSZИiЇћКЛМНОПРСТУƔФXѾЦЧШЩЪЫьҌЮЯЭѠѦѪѨѬѮѰӨѴӔ')
# Пустой желтый фон.
width = height = 800
fon_color = (255, 255, 255)
padding = 50
text_padding = 20
im = Image.new('RGB', (width, height), fon_color)
draw = ImageDraw.Draw(im)
n = len(alf)
xc = width // 2
yc = height // 2
r_point = (width // 2) - padding
r_text = (width // 2) - padding + text_padding
fi = -pi/2
points = []
# запоминаем точки многоугольника на окружности
for i in range(n):
    x_p = xc + r_point * cos(fi + (2 * pi * i) / (n))
    y_p = yc + r_point * sin(fi + (2 * pi * i) / (n))
    x_t = xc + r_text * cos(fi + (2 * pi * i) / (n))
    y_t = yc + r_text * sin(fi + (2 * pi * i) / (n))
    points.append((x_p, y_p))

    draw.text(
        (x_t-5,y_t-8),
        alf[i],
        fill=('#000'),
        font=font
    )
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        draw.line((points[i], points[j]), fill='#eee8aa', width=1)
    x,y = points[i]
    draw.ellipse((x-2,y-2,x+2,y+2),"#000")

im.show()

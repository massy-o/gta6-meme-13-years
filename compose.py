from PIL import Image, ImageDraw, ImageFont

BASE = '/home/hatch/workspace/makefun_meme/assets/media-generation-meme-base-0-fe0bb08f-2625-4ea5-8ad9-d9051089a211.webp'
MARK = '/home/hatch/workspace/makefun_meme/assets/mark-1024.png'
OUT = '/home/hatch/workspace/makefun_meme/meme.png'
FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
MAGENTA = (232, 30, 140)

img = Image.open(BASE).convert('RGB')
W, H = img.size  # 1600x1600
d = ImageDraw.Draw(img)

def text_size(txt, px):
    f = ImageFont.truetype(FONT, px)
    b = d.textbbox((0, 0), txt, font=f)
    return f, b[2] - b[0], b[3] - b[1]

def fit_font(txt, max_w, start_px):
    px = start_px
    while px > 10:
        f, w, h = text_size(txt, px)
        if w <= max_w:
            return f, w, h
        px -= 4
    return f, w, h

# top bar
d.rectangle([0, 0, W, 150], fill=(0, 0, 0))
t = 'WAITED 13 YEARS FOR GTA 6'
f, w, h = fit_font(t, W - 60, 96)
d.text(((W - w) / 2, (150 - h) / 2 - 6), t, font=f, fill=(255, 255, 255))

# year tags just under the bar
for txt, right in (('2013', False), ('2026', True)):
    f2, w2, h2 = text_size(txt, 62)
    x = W - 36 - w2 if right else 36
    d.text((x, 172), txt, font=f2, fill=(255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0))

# the make.fun ghost, worked into the scene at the seam between the two eras
ghost = Image.open(MARK).convert('RGBA').resize((500, 500), Image.LANCZOS)
img.paste(ghost, (550, 470), ghost)
d = ImageDraw.Draw(img)

# bottom bar with the pitch
d.rectangle([0, H - 196, W, H], fill=(0, 0, 0))
l1 = 'MY AI AGENT ALREADY GOT PAID'
f, w, h = fit_font(l1, W - 60, 72)
d.text(((W - w) / 2, H - 188), l1, font=f, fill=(255, 255, 255))
# line 2: 'ON ' + 'make.fun' (magenta) + ' WHILE I WAITED'
parts = [('ON ', (255, 255, 255)), ('make.fun', MAGENTA), (' WHILE I WAITED', (255, 255, 255))]
f2 = ImageFont.truetype(FONT, 72)
widths = [d.textbbox((0, 0), p, font=f2)[2] for p, _ in parts]
total = sum(widths)
x = (W - total) / 2
for (p, col), wpx in zip(parts, widths):
    d.text((x, H - 104), p, font=f2, fill=col)
    x += wpx

img.save(OUT)
print('wrote', OUT, img.size)

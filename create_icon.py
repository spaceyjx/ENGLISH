from PIL import Image, ImageDraw, ImageFont
import os

# 创建一个256x256的淡红色背景图标
width, height = 256, 256
image = Image.new('RGB', (width, height), color='#FFE6E6')  # 淡红色背景

draw = ImageDraw.Draw(image)

# 尝试使用系统字体
try:
    font = ImageFont.truetype('arial.ttf', 40)
except:
    font = ImageFont.load_default()

# 绘制书本图标 (简化版)
draw.rectangle([50, 80, 206, 176], fill='#FFFFFF', outline='#333333', width=3)
draw.rectangle([50, 80, 70, 176], fill='#E6E6E6', outline='#333333', width=3)
draw.line([70, 80, 70, 176], fill='#333333', width=1)

# 绘制文字
text = "单词"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = (width - text_width) // 2
text_y = 190
draw.text((text_x, text_y), text, font=font, fill='#333333')

# 保存为ico文件
icon_path = 'icon.ico'
image.save(icon_path, format='ICO')

print(f"图标已生成: {os.path.abspath(icon_path)}")
# criar_favicon.py
from PIL import Image, ImageDraw
import os

# Criar diretórios
os.makedirs('static/img', exist_ok=True)

# Tamanhos diferentes para o favicon
sizes = [16, 32, 48, 64]

for size in sizes:
    # Cria uma imagem quadrada
    img = Image.new('RGBA', (size, size), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # Calcula o tamanho do quadrado dourado
    margin = size // 4
    draw.rectangle(
        [margin, margin, size - margin, size - margin],
        fill=(255, 215, 0, 255)  # Dourado
    )
    
    # Se for grande o suficiente, desenha "UP"
    if size >= 32:
        # Desenha uma seta para cima
        triangle_margin = margin + (size // 8)
        draw.polygon([
            (size // 2, triangle_margin),  # Topo
            (triangle_margin, size - triangle_margin),  # Esquerda inferior
            (size - triangle_margin, size - triangle_margin)  # Direita inferior
        ], fill=(0, 0, 0, 255))
    
    # Salva individualmente para teste
    img.save(f'static/img/favicon_{size}x{size}.png')

print("✅ Favicons criados em static/img/")
print("📁 Arquivos criados:")
print("   - favicon_16x16.png")
print("   - favicon_32x32.png")
print("   - favicon_48x48.png")
print("   - favicon_64x64.png")
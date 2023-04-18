import qrcode
import os

# Solicita ao usuário o valor do QRCode
qr_value = input("Digite o valor do QRCode: ")

# Cria o QRCode usando o valor especificado
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qr_value)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Solicita ao usuário o caminho onde a imagem deve ser salva
img_path = input("Digite o caminho onde a imagem deve ser salva (exemplo: /caminho/para/imagem.png): ")

# Cria o diretório, se ele não existir
os.makedirs(os.path.dirname(img_path), exist_ok=True)

# Salva a imagem do QRCode no caminho especificado
img.save(img_path)

print(f"QRCode salvo em: {img_path}")

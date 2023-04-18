# Estágio 1 - Imagem de compilação
FROM python:3 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY generate_qr_code.py .

# Estágio 2 - Imagem final
FROM python:3-alpine
RUN apk --no-cache add libqrencode
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/generate_qr_code.py .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "generate_qr_code.py"]

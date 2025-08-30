# 1. Base Image
FROM python:3.11-slim

# 2. Set Working Directory
WORKDIR /app

# 3. Copy Requirements and Install Dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# 4. Copy All Application Code
COPY . .

# 5. Expose the Port Render Uses
ENV PORT 10000

# 6. Start Command
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]

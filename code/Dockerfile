FROM python:3.7-alpine
COPY . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

EXPOSE 5000
CMD flask run --host=0.0.0.0
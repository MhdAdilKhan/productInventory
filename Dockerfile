FROM --platform=linux/amd64 python:3.8.2
ENV PYTHONUNBUFFERED 1
ADD ./productInventory /web
WORKDIR /web
RUN python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /web/requirements.txt
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

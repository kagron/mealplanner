FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend /code/
RUN chmod +x /code/wait-for-it.sh
EXPOSE 8000
CMD ["gunicorn", "--chdir", "mealplanner", "--bind", ":8000", "mealplanner.wsgi:application"]
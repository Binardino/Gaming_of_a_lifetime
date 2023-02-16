FROM python:3.9

#set working directory to /app level
WORKDIR /app

COPY requirements.txt .
#install packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

#set environment variables for SQL database
ENV SQL_DATABASE=mydatabase
ENV SQL_USER=myuser
ENV SQL_PASSWORD=mypassword
    
#set up volume
VOLUME /var/lib/mysql

#Expose port 5000
EXPOSE 5000

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#run app in Streamlit
CMD ["python", "app.py"]
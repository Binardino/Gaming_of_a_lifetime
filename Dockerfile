FROM python:3.9

#set working directory to /app level
WORKDIR /app

COPY requirements.txt .
#install packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

#Expose port 5000
EXPOSE 5000

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#run app in Streamlit
ENTRYPOINT ["streamlit", "run", "app_gaming.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Set the command to run your Streamlit app
CMD ["streamlit", "run", "app_gaming.py"]
FROM strider/strider-docker-slave
USER root

#FROM node:10
FROM python:alpine3.7

# Create app directory
COPY . /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
RUN pip install -r requirements.txt
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "python", "examples-forms.py" ]

FROM node:14
ENV NPM_CONFIG_LOGLEVEL warn
ENV NODE_ENV=development PORT=3000
RUN mkdir -p /code/frontend/cache
WORKDIR /code/frontend
EXPOSE $PORT
ENV PATH /code/frontend/node_modules/.bin:$PATH
COPY package.json /code/frontend/package.json
RUN npm i --production
ADD . /code/frontend
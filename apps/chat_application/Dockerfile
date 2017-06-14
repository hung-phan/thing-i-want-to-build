FROM node:6.11.0

MAINTAINER Hung Phan

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64

RUN chmod +x /usr/local/bin/dumb-init

WORKDIR /usr/src/app

ENV NODE_ENV=production \
    PORT=3000

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

RUN yarn build

CMD ["dumb-init", "npm", "start"]

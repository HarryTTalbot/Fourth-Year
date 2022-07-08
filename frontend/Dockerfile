FROM node:lts-alpine

# From https://github.com/thgh/rollup-plugin-livereload/issues/56#issuecomment-780468246
ENV HOST="0.0.0.0"
EXPOSE 35729

WORKDIR /app
RUN mkdir /.npm
ENTRYPOINT npm install && npm run dev

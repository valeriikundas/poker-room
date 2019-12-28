FROM node:lts-alpine
EXPOSE 8080
RUN npm install -g http-server
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
#CMD ["sh"]
CMD ["npm", "run", "serve"]

# CMD [ "http-server", "dist" ]
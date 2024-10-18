FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install rollup --legacy-peer-deps
COPY . .
CMD ["npm", "run", "dev", "--", "--port", "5173"]
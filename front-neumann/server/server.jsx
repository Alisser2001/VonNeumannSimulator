import axios from 'axios';

const server = axios.create({
    baseURL: "http://127.0.0.1:8000/?x=200&y=55"
})

export default server;
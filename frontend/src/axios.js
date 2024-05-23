// src/axios.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/' // 根据您的后端服务器地址调整
});

export default axiosInstance;

import axios from 'axios';

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
});

export async function uploadReceipt(file) {
  const form = new FormData();
  form.append('file', file);
  const res = await API.post('/upload/', form, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  return res.data;
}

export async function fetchReceipts() {
  const res = await API.get('/analytics/');
  return res.data;
}
import axios from "axios";

const api = axios.create({
  baseURL: "https://wc4bhuqv93.execute-api.us-east-1.amazonaws.com/Prod/",
});

export default api;

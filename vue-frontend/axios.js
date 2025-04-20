import axios from 'axios';
const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:5000'  
});

// Add a request interceptor
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('authToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

apiClient.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        if (error.response && error.response.status === 401) {
            console.error('Unauthorized access - redirecting to login');
        }
        return Promise.reject(error);
    }
);

export default apiClient;
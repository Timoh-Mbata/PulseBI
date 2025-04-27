<template>
  <div class="login-container">
    <h2 class="title">Login to Your Account</h2>
    <form @submit.prevent="loginUser" class="login-form">
      <div class="input-group">
        <label for="email" class="input-label">Email</label>
        <input
          type="email"
          id="email"
          v-model="email"
          class="input-field"
          placeholder="Enter your email"
          required
        />
        <p v-if="errors.email" class="error-message">{{ errors.email }}</p>
      </div>

      <div class="input-group">
        <label for="password" class="input-label">Password</label>
        <input
          type="password"
          id="password"
          v-model="password"
          class="input-field"
          placeholder="Enter your password"
          required
        />
        <p v-if="errors.password" class="error-message">{{ errors.password }}</p>
      </div>

      <button type="submit" class="submit-btn">Login</button>

      <p v-if="loginError" class="error-message login-error">
        {{ loginError }}
      </p>
    </form>

    <div class="register-redirect">
      <p>Don't have an account?</p>
      <router-link to="/sign-up" class="register-link">SignUp Here</router-link>
    </div>

    <div v-if="isLoggedIn" class="success-message">
      {{ username }} You have successfully logged in.
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
      errors: {},
      loginError: '',
      isLoggedIn: false,
      username: '',
      role: '',
      dashboardRoute: '', // New data property to hold the dashboard route
    };
  },
  methods: {
    async loginUser() {
      this.errors = {};
      this.loginError = '';

      // Validate fields
      if (!this.email || !this.password) {
        this.loginError = 'Please fill out all fields.';
        return;
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/auth/login', {
          email: this.email,
          password: this.password,
        });

        if (response.data.access_token) {  // Check if the token is present
          // Store the token in localStorage (or sessionStorage)
          localStorage.setItem('access_token', response.data.access_token);

          this.isLoggedIn = true;
          this.username = response.data.username || 'User'; // Default to 'User' if not provided
          this.role = response.data.role; // Get the role from the response
          this.dashboardRoute = response.data.dashboard; // Get the dashboard route from the response

          // Redirect to the dashboard based on role
          this.$router.push(this.dashboardRoute);
        } else {
          this.loginError = response.data.message;
        }
      } catch (error) {
        this.loginError = 'An error occurred during login. Please try again.';
      }
    },
  },
};
</script>


<style scoped>
.login-container {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  font-size: 1.6rem;
  font-weight: 600;
  margin-bottom: 30px;
  color: #333;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.input-group {
  margin-bottom: 20px;
}

.input-label {
  font-size: 1rem;
  margin-bottom: 8px;
  font-weight: 600;
  color: #333;
}

.input-field {
  padding: 15px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  outline: none;
  transition: border 0.3s;
}

.input-field:focus {
  border-color: #007bff;
}

.input-field::placeholder {
  color: #aaa;
  font-style: italic;
}

.error-message {
  color: #e74c3c;
  font-size: 0.875rem;
}

.submit-btn {
  background-color: #007bff;
  color: white;
  padding: 15px;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #0056b3;
}

.login-error {
  color: #e74c3c;
  font-size: 1rem;
  text-align: center;
  margin-top: 20px;
}

.register-redirect {
  text-align: center;
  margin-top: 20px;
}

.register-link {
  color: #007bff;
  font-weight: bold;
  text-decoration: none;
}

.register-link:hover {
  text-decoration: underline;
}

.success-message {
  text-align: center;
  margin-top: 20px;
  font-size: 1.2rem;
  color: #28a745;
}
.body {
  background-color: #f8f9fa;
  font-family: 'Arial', sans-serif;
  color: #333;
  line-height: 1.6;
}
</style>

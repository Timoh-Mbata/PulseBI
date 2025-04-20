<template>
    <div class="registration-container">
      <h2 class="title">Create Your Account</h2>
      <form @submit.prevent="registerUser" class="registration-form">
        <div class="input-group">
          <label for="username" class="input-label">Username </label>
          <input
            type="text"
            id="username"
            v-model="username"
            class="input-field"
            placeholder="Enter your username "
            required
          />
          <p v-if="errors.username" class="error-message">{{ errors.username }}</p>
        </div>
  
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
            placeholder="Choose a password"
            required
          />
          <p v-if="errors.password" class="error-message">{{ errors.password }}</p>
        </div>
  
        <div class="input-group">
          <label for="confirmPassword" class="input-label">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="confirmPassword"
            class="input-field"
            placeholder="Re-enter your password"
            required
          />
          <p v-if="errors.confirmPassword" class="error-message">{{ errors.confirmPassword }}</p>
        </div>
  
        <button type="submit" class="submit-btn">Register</button>
  
        <p v-if="registrationError" class="error-message registration-error">
          {{ registrationError }}
        </p>
      </form>
  
      <div class="login-redirect">
        <p>Already have an account?</p>
        <router-link to="/login" class="login-link">Login Here</router-link>
      </div>
    </div>
  </template>
  
<script>
import axios from 'axios';

export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      errors: {},
      registrationError: '',
    };
  },
  methods: {
    async registerUser() {
      this.errors = {};
      this.registrationError = '';

      if (this.password !== this.confirmPassword) {
        this.errors.confirmPassword = 'Passwords do not match.';
        return;
      }

      if (!this.username || !this.email || !this.password || !this.confirmPassword) {
        this.registrationError = 'Please fill out all fields.';
        return;
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/auth/register', {
          username: this.username,
          email: this.email,
          password: this.password,
        });

        console.log(response.data); // Check the response data

        if (response.data.success) {
          this.$router.push('/login'); // Redirect to login if registration is successful
        } else {
          this.registrationError = response.data.message;
        }
      } catch (error) {
        this.registrationError = 'An error occurred during registration. Please try again.';
      }
    },
  },
};
</script>
  
  <style scoped>
  .registration-container {
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
  
  .registration-form {
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
  
  .registration-error {
    color: #e74c3c;
    font-size: 1rem;
    text-align: center;
    margin-top: 20px;
  }
  
  .login-redirect {
    text-align: center;
    margin-top: 20px;
  }
  
  .login-link {
    color: #007bff;
    font-weight: bold;
    text-decoration: none;
  }
  
  .login-link:hover {
    text-decoration: underline;
  }
  </style>
  
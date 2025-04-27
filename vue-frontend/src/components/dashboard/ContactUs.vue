<template>
  <div class="contact-container">
    <transition name="fade-slide">
      <h1 v-if="showForm">Contact Us</h1>
    </transition>
    <form @submit.prevent="handleSubmit" v-show="showForm">
      <transition-group name="fade" tag="div">
        <div class="form-group" key="name">
          <label for="name">Name</label>
          <input
            type="text"
            id="name"
            v-model="form.name"
            required
            placeholder="Your full name"
          />
        </div>

        <div class="form-group" key="email">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            required
            placeholder="Your email address"
          />
        </div>

        <div class="form-group" key="message">
          <label for="message">Message</label>
          <textarea
            id="message"
            v-model="form.message"
            required
            placeholder="Your message"
          ></textarea>
        </div>
      </transition-group>

      <button
        type="submit"
        class="submit-button"
        :class="{ success: submitted }"
      >
        {{ submitted ? "✓ Message Sent!" : "Send Message" }}
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ContactUs",
  data() {
    return {
      form: {
        name: "",
        email: "",
        message: "",
      },
      showForm: false,
      submitted: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.showForm = true;
    }, 300); // delay entrance animation
  },
  methods: {
    handleSubmit() {
      console.log("Form Submitted:", this.form);

      this.submitted = true;

      // Reset form after animation
      setTimeout(() => {
        this.form.name = "";
        this.form.email = "";
        this.form.message = "";
        this.submitted = false;
      }, 2000);
    },
  },
};
</script>

<style scoped>
/* Base Layout */
.contact-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 25px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.1);
  animation: fadeIn 1s ease-in-out;
}

/* Headings */
h1 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 28px;
  color: #333;
}

/* Form Group */
.form-group {
  margin-bottom: 20px;
  animation: slideIn 0.4s ease-out;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 6px;
}

input,
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
  transition: border 0.3s ease;
}

input:focus,
textarea:focus {
  border-color: #4caf50;
  outline: none;
}

/* Button */
.submit-button {
  width: 100%;
  padding: 14px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 17px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.submit-button:hover {
  background-color: #43a047;
  transform: translateY(-2px);
}

.submit-button.success {
  background-color: #2ecc71 !important;
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Transitions */
.fade-slide-enter-active {
  transition: all 0.8s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-slide-enter-to {
  opacity: 1;
  transform: translateY(0);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

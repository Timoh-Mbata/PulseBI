<template>
  <div class="settings-panel">
    <h2>User Settings</h2>
    <div class="form-section">
      <!-- Theme Setting -->
      <div class="form-group">
        <label for="theme">Theme</label>
        <select v-model="selectedTheme" @change="changeTheme" id="theme">
          <option value="light">Light</option>
          <option value="dark">Dark</option>
        </select>
      </div>

      <!-- Workspace Setting -->
      <div class="form-group">
        <label for="workspace">Workspace</label>
        <select v-model="selectedWorkspace" id="workspace">
          <option value="default">Default</option>
          <option value="marketing">Marketing</option>
          <option value="sales">Sales</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const selectedTheme = ref(localStorage.getItem('theme') || 'light');
const selectedWorkspace = ref(localStorage.getItem('workspace') || 'default');

const changeTheme = () => {
  if (selectedTheme.value === 'dark') {
    document.documentElement.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light');
  }
};

watch(selectedWorkspace, (newWorkspace) => {
  localStorage.setItem('workspace', newWorkspace);
});

changeTheme();
</script>

<style scoped>
.settings-panel {
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  max-width: 480px;
  margin: 2rem auto;
  font-family: 'Segoe UI', sans-serif;
  transition: background 0.3s ease;
}

.dark-mode .settings-panel {
  background: #1e1e2f;
  color: #f0f0f0;
}

.settings-panel h2 {
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
  color: #2c3e50;
}

.dark-mode .settings-panel h2 {
  color: #ffffff;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
}

.dark-mode label {
  color: #ccc;
}

select {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.dark-mode select {
  background: #333;
  color: #fff;
  border: 1px solid #555;
}
</style>

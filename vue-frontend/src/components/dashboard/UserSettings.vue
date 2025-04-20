<template>
  <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow">
    <h2 class="text-lg font-semibold mb-4">User Settings</h2>
    <div class="space-y-4">
      <!-- Theme Setting -->
      <div>
        <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Theme</label>
        <select v-model="selectedTheme" @change="changeTheme" class="w-full rounded-md border-gray-300 dark:bg-gray-700 dark:text-white">
          <option value="light">Light</option>
          <option value="dark">Dark</option>
        </select>
      </div>

      <!-- Workspace Setting -->
      <div>
        <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Workspace</label>
        <select v-model="selectedWorkspace" class="w-full rounded-md border-gray-300 dark:bg-gray-700 dark:text-white">
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

// Reactive variables for theme and workspace settings
const selectedTheme = ref(localStorage.getItem('theme') || 'light');
const selectedWorkspace = ref(localStorage.getItem('workspace') || 'default');

// Function to change theme and save it to localStorage
const changeTheme = () => {
  if (selectedTheme.value === 'dark') {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
};

// Watch for changes to workspace setting and save it to localStorage
watch(selectedWorkspace, (newWorkspace) => {
  localStorage.setItem('workspace', newWorkspace);
});

// Initialize theme on component mount
changeTheme();
</script>

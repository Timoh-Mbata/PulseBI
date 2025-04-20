<template>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow">
      <h2 class="text-lg font-semibold mb-4">Data Sources</h2>
      <ul class="divide-y divide-gray-200 dark:divide-gray-700">
        <li v-for="source in sources" :key="source.name" class="py-2 flex justify-between">
          <span>{{ source.name }}</span>
          <span :class="source.status === 'Active' ? 'text-green-500' : 'text-red-500'">{{ source.status }}</span>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
export default {
  name: 'DataSources',
  props: {
    sources: {
      type: Array,
      default: () => [
        { name: 'PostgreSQL DB', status: 'Active' },
        { name: 'Google Sheets', status: 'Error' },
      ],
    },
  },
};
</script>
  
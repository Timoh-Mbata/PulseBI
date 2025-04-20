<template>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div v-for="kpi in kpis" :key="kpi.label" class="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow">
        <h2 class="text-sm font-medium text-gray-500 dark:text-gray-300">{{ kpi.label }}</h2>
        <p class="text-2xl font-semibold text-gray-900 dark:text-white">
          {{ kpi.value }}
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'KpiSummary',
    props: {
      kpis: {
        type: Array,
        default: () => [
          { label: 'Revenue', value: '$23,456' },
          { label: 'Expenses', value: '$4,560' },
          { label: 'Users', value: '2,140' },
          { label: 'Growth', value: '+5.8%' },
        ],
      },
    },
  };
  </script>
  
<template>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow">
      <h2 class="text-lg font-semibold mb-4">Live Data</h2>
      <ul class="space-y-2">
        <li v-for="item in liveStats" :key="item.label" class="flex justify-between">
          <span class="text-gray-600 dark:text-gray-300">{{ item.label }}</span>
          <span class="font-semibold">{{ item.value }}</span>
        </li>
      </ul>
    </div>
  </template>
  
  
<script>
export default {
  name: 'LiveData',
  props: {
    liveStats: {
      type: Array,
      default: () => [
        { label: 'Live Sales', value: '120' },
        { label: 'Site Traffic', value: '865' },
        { label: 'Active Users', value: '42' },
      ],
    },
  },
};
</script>
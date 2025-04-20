<template>
  <div class="space-y-3">
    <div
      v-for="alert in alerts"
      :key="alert.id"
      :class="['border-l-4 p-3 rounded shadow-md', alert.color]"
    >
      <div class="text-sm text-gray-700">
        <strong class="block">{{ alert.category }}</strong>
        {{ alert.message }}
      </div>
      <div class="flex justify-end space-x-2 mt-2">
        <button class="text-xs text-blue-500 hover:underline">Acknowledge</button>
        <button class="text-xs text-red-500 hover:underline">Dismiss</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AlertsPanel',
  props: {
    alerts: {
      type: Array,
      default: () => [
        { id: 1, message: 'Revenue dropped 15%', category: 'Finance', color: 'border-red-500' },
        { id: 2, message: 'Server is down', category: 'System', color: 'border-yellow-500' },
      ],
    },
  },
};
</script>

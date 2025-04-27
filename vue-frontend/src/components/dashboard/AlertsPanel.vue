<template>
  <div class="alerts-wrapper">
    <div
      v-for="alert in alerts"
      :key="alert.id"
      class="alert-box"
      :style="{ borderLeftColor: alert.color }"
    >
      <div class="alert-content">
        <strong class="alert-category">{{ alert.category }}</strong>
        <p class="alert-message">{{ alert.message }}</p>
      </div>
      <div class="alert-actions">
        <button class="btn acknowledge">Acknowledge</button>
        <button class="btn dismiss">Dismiss</button>
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
        { id: 1, message: 'Revenue dropped 15%', category: 'Finance', color: '#e74c3c' },
        { id: 2, message: 'Server is down', category: 'System', color: '#f1c40f' },
      ],
    },
  },
};
</script>

<style scoped>
.alerts-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin-top: 1rem;
}

.alert-box {
  display: flex;
  flex-direction: column;
  border-left: 6px solid;
  padding: 1rem;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s ease;
}

.alert-box:hover {
  transform: scale(1.01);
}

.alert-content {
  color: #333;
}

.alert-category {
  display: block;
  font-weight: bold;
  font-size: 0.95rem;
  margin-bottom: 0.25rem;
}

.alert-message {
  font-size: 0.9rem;
  color: #555;
}

.alert-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.btn {
  font-size: 0.75rem;
  border: none;
  background: none;
  cursor: pointer;
  text-decoration: underline;
  transition: color 0.2s ease;
}

.acknowledge {
  color: #3498db;
}

.acknowledge:hover {
  color: #2980b9;
}

.dismiss {
  color: #e74c3c;
}

.dismiss:hover {
  color: #c0392b;
}
</style>

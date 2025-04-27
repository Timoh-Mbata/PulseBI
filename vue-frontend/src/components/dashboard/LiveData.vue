<template>
  <div class="live-dashboard-container">
    <h2 class="live-dashboard-title">📡 Live Dashboard</h2>
    <transition-group name="fade-item" tag="ul" class="live-stats-list">
      <li
        v-for="item in liveStats"
        :key="item.label"
        class="live-stat-item"
      >
        <span class="stat-label">{{ item.label }}</span>
        <span class="stat-value">{{ item.value }}</span>
      </li>
    </transition-group>
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

<style scoped>
/* Gradient background for light and dark modes */
.live-dashboard-container {
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  background: linear-gradient(135deg, #d1fae5, #ffedd5); /* light mode gradient */
  background-color: #1f2937; /* fallback dark background */
}

.dark .live-dashboard-container {
  background: linear-gradient(135deg, #1f2937, #374151); /* dark mode gradient */
  background-color: #1f2937;
}

/* Dashboard title */
.live-dashboard-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2d3748; /* Dark gray for light mode */
  margin-bottom: 16px;
}

.dark .live-dashboard-title {
  color: #fff; /* White for dark mode */
}

/* List of stats */
.live-stats-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

/* Each stat item */
.live-stat-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  padding: 12px;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  margin-bottom: 12px;
}

.dark .live-stat-item {
  background-color: #2d3748; /* Dark gray background for dark mode */
}

.live-stat-item:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Label for each stat */
.stat-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #4a5568; /* Gray text */
}

.dark .stat-label {
  color: #e2e8f0; /* Light gray for dark mode */
}

/* Stat value pill */
.stat-value {
  font-size: 1rem;
  font-weight: 600;
  color: #2c7a7b; /* Teal color for stat value */
  background-color: #e6fffa; /* Light teal background */
  padding: 6px 12px;
  border-radius: 12px;
}

.dark .stat-value {
  color: #38b2ac; /* Light teal color for dark mode */
  background-color: #2f855a; /* Dark teal for dark mode */
}

/* Fade transition */
.fade-item-enter-active {
  transition: all 0.4s ease;
}
.fade-item-enter-from {
  opacity: 0;
  transform: translateY(10px) scale(0.95);
}
.fade-item-enter-to {
  opacity: 1;
  transform: translateY(0) scale(1);
}
</style>

<template>
  <transition name="fade-scale">
    <div class="data-sources-card">
      <h2 class="card-title">Data Sources</h2>
      <ul class="sources-list">
        <transition-group name="list" tag="div">
          <li
            v-for="source in sources"
            :key="source.name"
            class="source-item"
          >
            <span>{{ source.name }}</span>
            <span
              :class="['status', source.status === 'Active' ? 'active' : 'error']"
            >
              {{ source.status }}
            </span>
          </li>
        </transition-group>
      </ul>
    </div>
  </transition>
</template>

<script>
export default {
  name: "DataSources",
  props: {
    sources: {
      type: Array,
      default: () => [
        { name: "PostgreSQL DB", status: "Active" },
        { name: "Google Sheets", status: "Error" },
      ],
    },
  },
};
</script>

<style scoped>
.data-sources-card {
  background-color: #fff;
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
  transition: transform 0.3s ease;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
}

.sources-list {
  border-top: 1px solid #e5e7eb;
}

.source-item {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  font-size: 15px;
  transition: background-color 0.2s ease;
}

.source-item:hover {
  background-color: #f9f9f9;
}

.status {
  font-weight: 600;
  transition: color 0.3s;
}

.status.active {
  color: #10b981; /* green */
}

.status.error {
  color: #ef4444; /* red */
}

/* Transition animations */
.fade-scale-enter-active {
  transition: all 0.4s ease;
}
.fade-scale-enter-from {
  opacity: 0;
  transform: scale(0.9);
}
.fade-scale-enter-to {
  opacity: 1;
  transform: scale(1);
}

.list-enter-active {
  transition: all 0.3s ease;
}
.list-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.list-enter-to {
  opacity: 1;
  transform: translateY(0);
}
</style>

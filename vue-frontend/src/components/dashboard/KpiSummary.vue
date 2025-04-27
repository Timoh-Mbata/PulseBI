<template>
  <transition-group
    name="fade-kpi"
    tag="div"
    class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6"
  >
    <div
      v-for="kpi in kpis"
      :key="kpi.label"
      class="kpi-card transform hover:-translate-y-1 hover:scale-[1.03] transition duration-500 ease-in-out"
    >
      <h2 class="kpi-label">{{ kpi.label }}</h2>
      <p class="kpi-value">{{ kpi.value }}</p>
    </div>
  </transition-group>
</template>

<script>
export default {
  name: "KpiSummary",
  props: {
    kpis: {
      type: Array,
      default: () => [
        { label: "Revenue", value: "$23,456" },
        { label: "Expenses", value: "$4,560" },
        { label: "Users", value: "2,140" },
        { label: "Growth", value: "+5.8%" },
      ],
    },
  },
};
</script>

<style scoped>
.kpi-card {
  background: linear-gradient(135deg, #4f46e5, #0ea5e9); /* Indigo to Sky Blue */
  color: white;
  padding: 20px;
  border-radius: 1rem;
  box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2);
  transition: all 0.4s ease;
}

.kpi-label {
  font-size: 0.95rem;
  font-weight: 500;
  color: #e0f2fe;
  margin-bottom: 6px;
}

.kpi-value {
  font-size: 2rem;
  font-weight: 700;
  color: white;
}

/* Fade + Slide Animation */
.fade-kpi-enter-active {
  transition: all 0.5s ease;
}
.fade-kpi-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.98);
}
.fade-kpi-enter-to {
  opacity: 1;
  transform: translateY(0) scale(1);
}
</style>

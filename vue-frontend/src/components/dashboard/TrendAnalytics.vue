<template>
  <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow">
    <h2 class="text-lg font-semibold mb-4">Trend Analytics</h2>
    <div class="h-64 bg-gray-100 dark:bg-gray-700 rounded-xl flex items-center justify-center">
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart, CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';

// Register necessary components from Chart.js
Chart.register(
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
);

// Reference for the canvas
const chartCanvas = ref(null);

// Sample data for the chart
const chartData = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June'], // X-Axis
  datasets: [
    {
      label: 'Revenue',
      data: [1000, 1200, 1300, 1500, 1700, 2000], // Y-Axis data points
      borderColor: '#4CAF50',
      backgroundColor: 'rgba(76, 175, 80, 0.2)',
      fill: true,
    },
    {
      label: 'Expenses',
      data: [500, 600, 700, 800, 900, 1000], // Y-Axis data points
      borderColor: '#FF6347',
      backgroundColor: 'rgba(255, 99, 71, 0.2)',
      fill: true,
    },
  ],
};

// Create the chart once the component is mounted
onMounted(() => {
  new Chart(chartCanvas.value, {
    type: 'line',
    data: chartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});
</script>

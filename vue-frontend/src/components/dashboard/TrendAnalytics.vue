<template>
  <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow-lg card-container">
    <h2 class="text-lg font-semibold mb-4">Trend Analytics</h2>
    <div class="chart-container">
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>


<script setup>
import { onMounted, ref } from 'vue';
import { 
  Chart, 
  CategoryScale, 
  LinearScale, 
  LineElement, 
  PointElement, 
  Title, 
  Tooltip, 
  Legend, 
  LineController 
} from 'chart.js';

// Register necessary components from Chart.js
Chart.register(
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
  LineController // Make sure to register the LineController
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
    type: 'line', // Chart type
    data: chartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
      animations: {
        tension: {
          duration: 1000,
          easing: 'easeInOutQuad',
        },
        x: {
          duration: 800,
          easing: 'easeOutBounce',
        },
      },
    },
  });
});
</script>



<style scoped>
/* Global Styles for smoother transitions */
body {
  font-family: 'Arial', sans-serif;
  background-color: #f4f7fc;
  margin: 0;
  padding: 0;
}

/* Card container styling */
.card-container {
  animation: fadeIn 1s ease-out;
  transition: box-shadow 0.3s ease;
}

.card-container:hover {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

/* Chart container */
.chart-container {
  height: 300px; /* Adjusted height for better spacing */
  background-color: #f1f5f8;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  animation: scaleUp 1.5s ease-in-out;
}

/* Fade-in animation */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Scale-up effect for the chart container */
@keyframes scaleUp {
  0% {
    transform: scale(0.9);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

/* Styling for the chart (canvas) */
canvas {
  width: 100% !important;
  height: 100% !important;
}

</style>
